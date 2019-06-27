from requests import get, post
from bs4 import BeautifulSoup
from time import sleep
import re

from lingcorpora.params_container import Container
from lingcorpora.target import Target
from lingcorpora.exceptions import EmptyPageException

__doc__ = \
'''
National Corpus of Polish
=========================

API for National Corpus of Polish (http://nkjp.pl/)

**Search Parameters**
-
query: str:
    Search by word.
n_results: int, default 100
    Number of results.
    In case of Polisg Corpus it does NOT work like the less the number the higher speed.
n_left: int, default 5
    Number of words in the left context.
n_right: int, default 5
    Number of words in the right context.
subcorpus: str, default 'nkjp300'
    Subcorpus to search in. Available options:
        * 'nkjp300': balanced NKJP subcorpus (300M segments)
        * 'nkjp1800': the full NKJP sorpus (1800M segments)
        * 'nkjp1M': manually annotated corpus (1.2M segments)
        * 'ipi250': the full IPI PAN corpus (2nd edition, 250M segments)
        * 'ipi030': the IPI PAN corpus sample (2nd edition; 30M segments)
        * 'frequency-dictionary': the Frequency Dictionary Corpus (0.5M segments)
get_analysis: bool, default False
    Whether to download grammatical information if the corpus is annotated.

Example
-------

.. code-block:: python

    corp = lingcorpora.Corpus('pol')
    results = corp.search('żaba', n_results=10)
    for result in results:
        for i, target in enumerate(result):
            print(i+1, target.text)

.. parsed-literal::

    "żaba": 100%|██████████| 10/10 [00:11<00:00,  1.12s/docs]

    1  nie grzbiet, tylko zielona żaba rozpłaszczona na ropusze. Podróżowała
    2  woli skakać po łące jaka żaba . Nie może przestać wierzyć
    3  sobie zapewne, że to żaba błotna. - Tańcio!
    4 . Jak... żaba w raju. - Sprzątanie
    5 , rozdęta, bardzo pryszczata żaba . Brwi maga podjechały do
    6 , czuły na wilgoć jak żaba . Rzeczywiście, ja też
    7  potrafię tego uczynić. Czyż żaba może śpiewać jak skowronek lub
    8  Wpadłaś w kałużę, żaba ? - Nie jestem zadna
    9 em na plecach bezradnie jak żaba , przygnieciony przez Agnieszkę.
    10  opuchlizny. Wyglądał jak rozdeptana żaba . Pomyślałem, że

'''

TEST_DATA = {
    'test_single_query': {'query': 'żaba'},
    'test_multi_query': {'query': ['żaba', 'ropucha']}
}

class PageParser(Container):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tag_variable = 'slt' if self.get_analysis else 's'
        left = 5 if not self.n_left else self.n_left
        right = 5 if not self.n_right else self.n_right
        if not self.subcorpus:
            self.subcorpus = 'nkjp300'
        self.data = {
            'show_in_match': tag_variable,
            'show_in_context': tag_variable,
            'left_context_width': left,
            'right_context_width': right,
            'wide_context_width': '50',
            'results_per_page': self.n_results,
            'next': '/poliqarp/{}/query/'.format(self.subcorpus)
        }
    
    def _get_html(self):
        def _connect():
            r = get('http://nkjp.pl/poliqarp/')
            cookies = {
                'httpOnly': 'true',
                'path': '/',
                'sessionid': r.cookies.get('sessionid'),
            }
            post(
                url='http://nkjp.pl/poliqarp/settings/',
                cookies=cookies,
                data=self.data,
            )
            post(
                url='http://nkjp.pl/poliqarp/query/',
                cookies=cookies,
                data={'query': self.query,
                    'corpus': self.subcorpus},
            )
            html_page = post(
                url='http://nkjp.pl/poliqarp/{}/query/export/'.format(self.subcorpus),
                cookies=cookies,
                data={'format': 'html'},
            )
            return html_page
        i = 0
        while i < 10:
            html_page = _connect()
            if html_page.status_code == 200:
                break
            else:
                if i == 9:
                    raise EmptyPageException
                else:
                    sleep(i)
                    i += 1
        return html_page.text
    
    def _parse(self):
        html = self._get_html()
        soup = BeautifulSoup(html, 'lxml')
        table = soup.find('table')
        rows = table.select('tr')
        results = []
        for row in rows:
            r = row.select('td')
            results.append([r[0].text, r[1].text, r[2].text])
        return results[:self.n_results]
    
    def _parse_analysis(self, word):
        analysis_text = re.findall('\[(.*?)\]', word)[0]
        analysis_list = analysis_text.split(':')
        analysis_dict = {
            'lex': analysis_list[0],
            'gram': analysis_list[1:],
        }
        token = re.findall('(.*?) \[', word)[0]
        return token, analysis_dict
    
    def _new_target(self, r):
        if self.get_analysis:
            with_analysis = self._parse_analysis(r[1])
            r[1] = with_analysis[0]
            analysis = with_analysis[1]
            r[0] = ' '.join([w for w in r[0].split() if not w.startswith('[')])
            r[2] = ' '.join([w for w in r[2].split() if not w.startswith('[')])
        else:
            analysis = {}
        target = Target(
            text='{} {} {}'.format(*r).replace('  ', ' '),
            idxs=(len(r[0]) + 1, len(r[0]) + len(r[1])),
            meta='',
            analysis=analysis,
        )
        return target
    
    def extract(self):
        res = self._parse()
        for r in res:
            yield self._new_target(r)
