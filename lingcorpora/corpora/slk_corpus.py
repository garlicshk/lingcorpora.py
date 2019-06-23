from ..params_container import Container
from ..target import Target
from requests import get
from bs4 import BeautifulSoup

TEST_DATA = {'test_single_query': {'query': 'elektronická'},
             'test_multi_query': {'query': ['elektronická', 'je']}
            }

__author__ = 'zu-ann, ustya-k'
__doc__ = \
"""
Slovak Corpus
=============

API for Slovak corpus (http://korpus.juls.savba.sk:8080/manatee.ks/do_query).
    
**Search Parameters**

query: str or list([str])
    query or queries
n_results: int, default 100
    number of results wanted
kwic: bool, default True
    kwic format (True) or a sentence (False)
subcorpus: str, default 'prim-6.0-public-all'
    subcorpus. Available options: 'prim-6.0-public-all', 'r-mak-3.0'
start: int, default 0
    index of the first query appearance to be shown
"""


class PageParser(Container):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.subcorpus is None:
            self.subcorpus = 'prim-6.0-public-all'
        self.__page = None
        self.__pagenum = 0

    def __get_page(self):
        """
        create a query url and return a page with results
        """
        params = {'query': self.query,
                  'corpname': self.subcorpus,
                  'start': self.__pagenum}
        s = get('http://korpus.juls.savba.sk:8080/manatee.ks/do_query', params=params)
        return s.text

    def __new_target(self, left, word, right):
        text = '%s %s %s' % (left, word, right)
        idxs = (len(left) + 2, len(left) + len(word) + 1)
        meta = ''
        tags = {}
        return Target(text, idxs, meta, tags)

    def __parse_page(self):
        """
        parse the page
        """
        left_list = []
        center_list = []
        right_list = []
        soup = BeautifulSoup(self.__page, 'lxml')
        for left in soup.select('td[class="lc"]'):
            left_list.append(left.text)
        for center in soup.select('td[class="kwic"]'):
            center_list.append(center.text)
        for right in soup.select('td[class="rc"]'):
            right_list.append(right.text)
        res = [self.__new_target(l, c, r) for l, c, r in zip(
            left_list, center_list, right_list)]
        return res

    def __extract_results(self):
        self.__page = self.__get_page()
        parsed_results = self.__parse_page()
        return parsed_results

    def extract(self):
        output_counter = 0
        for i in range(0, self.n_results, 10):
            try:
                self.__pagenum = i
                results = self.__extract_results()
                j = 0
                while output_counter < self.n_results and j < len(results):
                    yield results[j]
                    output_counter += 1
                    j += 1
            except:
                pass
