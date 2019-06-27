from ..params_container import Container
from ..target import Target
from requests import post
from bs4 import BeautifulSoup

TEST_DATA = {'test_single_query': {'query': 'bezug'},
             'test_multi_query': {'query': ['bezug', 'Mutter']}
            }

__author__ = 'alexeykosh, ustya-k'
__doc__ = \
"""
German Corpus
=============

API for German corpus (https://www.dwds.de).
    
**Search Parameters**

query: str or list([str])
    query or queries
n_results: int, default 100
    number of results wanted
kwic: bool, default True
    kwic format (True) or a sentence (False) (True by default)
subcorpus: str
    subcorpus. Available options:
        * 'kern' (by default)
        * 'tagesspiegel'
        * 'zeit'
        * 'public'
        * 'blogs'
        * 'dingler'
        * 'untertitel'
        * 'spk'
        * 'bz'
        * 'dta'
        * 'korpus21'
        
Example
-------

.. code-block:: python

    corp = lingcorpora.Corpus('deu')
    results = corp.search('gut', n_results=10)
    print(results[0][0].text)

.. parsed-literal::

    "gut": 100%|██████████| 10/10 [00:00<00:00, 17.48docs/s]

    1 Ein in Wien sesshafter Reichsdeutscher, der bisher auch nicht einen Moment daran gedacht hatte, den Wiener Gemeinderath zu einer antipapistischen Liga umzugestalten, behauptete kürzlich, dass er es absolut nicht einsehen könne, warum die Briefe, die ihm seine Mutter aus Berlin schickt, täglich in »amtlich geschlossenem« Zustande an ihn gelangen.
    2 Das arme, alte Mütterlein in der Provinz muss sich's jetzt zweimal überlegen, mit ihren weit, weit in der Stadt im Soldatenrock steckenden Jungen briefliche Zwiesprach zu halten, und auch der hat die Heller nicht gar im Ueberfluss und zwackt jetzt wohl von seinen Ausgaben für schriftliche Mittheilungen an Mutter und Bruder zwei oder drei Karten wöchentlich ab.
    3 Aber vielleicht könnte man Mutter und Sohn anderweitig eine Genugthuung verschaffen; vielleicht entschlösse man sich, auf die vertheuerte Correspondenzkarte die Conterfeis der Herren Bacher, Benedikt, Singer, Glogau und Frischauer zu drucken, damit das Volk wenigstens durch den Anblick der Männer entschädigt wird, zu deren Gunsten es jetzt Zeitungsstempel und erhöhte Postgebür bezahlen muss.
    4 In seinem Tagebuche sprach Krauthauf von seiner Mutter per »Josefine«.
    5 Eine Erzieherin erkrankte und begab sich zu ihrer Mutter in Pflege.
    6 Aber die Klagen einer langen Reihe von Müttern über die Zustände im St. Joseph-Kinderspital haben sie tief erregt.
    7 Und auf seine Frage, was denn dazu gehöre, einem Kinde eine Ohrfeige zu geben, hat ihm der Vertheidiger offenbar namens aller Wiener Väter, Mütter und Lehrer nachdrücklich geantwortet:
    8 Das dauerte so lange, bis der frühreife Sohn der Königin sein Interesse für die Hofdame seiner Mutter , die "Femme de trente ans", in allzu deutlicher Weise kundgab.
    9 Je heißer das Verhältnis zwischen Draga und "Sascha" wurde, desto kälter wurden die Beziehungen zwischen dem König und seiner Mutter .
    10 Die Begrüßung zwischen der hohen Mutter und dem, von der Herbstsonne gebräunten, recht gut aussehenden Kronprinzen war sehr herzlich, und die Liebenswürdigkeit und das gewinnende Wesen der hohen Frau rissen die zahlreichen Zuschauer zu begeisterten Huldigungen hin. 

"""


class PageParser(Container):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__page = None
        if self.subcorpus is None:
            self.subcorpus = 'kern'

    def __get_page(self):
        params = {'corpus': self.subcorpus,
                  'date-end': '1999',
                  'date-start': '1900',
                  'format': 'kwic',
                  'genre': 'Belletristik',
                  'genre': 'Wissenschaft',
                  'genre': 'Gebrauchsliteratur',
                  'genre': 'Zeitung',
                  'limit': self.n_results,
                  'q': self.query,
                  'sort': 'date_asc'}
        s = post('https://www.dwds.de/r', params=params)
        return s

    def __new_target(self, left, word, right):
        text = '%s %s %s' % (left, word, right)
        idxs = (len(left) + 1, len(left) + len(word) + 1)
        meta = ''
        tags = {}
        return Target(text, idxs, meta, tags)

    def __get_results(self):
        left_list = []
        right_list = []
        center_list = []
        soup = BeautifulSoup(self.__page.text, 'lxml')
        for left in soup.select('.ddc-kwic-ls'):
            left_list.append(left.text.strip())
        for center in soup.select('.ddc-kwic-kw.ddc-hl'):
            center_list.append(center.text.strip())
        for right in soup.select('.ddc-kwic-rs'):
            right_list.append(right.text.strip())

        s = [self.__new_target(l, w, r) for l, w, r in zip(
            left_list, center_list, right_list)]
        return s

    def __extract_results(self):
        self.__page = self.__get_page()
        parsed_results = self.__get_results()
        return parsed_results

    def extract(self):
        parsed_results = self.__extract_results()
        for res in parsed_results:
            yield res
