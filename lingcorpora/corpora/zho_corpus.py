from ..params_container import Container
from requests import get
from bs4 import BeautifulSoup
from html import unescape
from ..target import Target


TEST_DATA = {'test_single_query': {'query': '代汉语'},
             'test_multi_query': {'query': ['古', '问题']}
            }

__author__ = 'kategerasimenko'
__doc__ = \
"""
zho_corpus
==========

API for Chinese corpus (http://ccl.pku.edu.cn:8080/ccl_corpus/).
    
Search Parameters
-----------------
query: str or list([str])
    query or queries (currently only exact search by word or phrase is available)
n_results: int, default 100
    number of results wanted
subcorpus: str, default 'xiandai'
    subcorpus.
    Available options:
        * 'xiandai' (modern Chinese)
        * 'dugai' (ancient Chinese)
n_left: int, default 30
    context lenght (in symbols)
n_right: int, default 30
    context lenght (in symbols)
"""


class PageParser(Container):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.__per_page = 50
        self.__pagenum = 0
        if self.subcorpus is None:
            self.subcorpus = 'xiandai'
        if self.n_left is None:
            self.n_left = 30
        if self.n_right is None:
            self.n_right = 30

            
    def get_results(self):
        """
        create a query url and get results for one page
        """
        params = {'q': self.query,
                  'start': self.__pagenum,
                  'num': self.n_results,
                  'index':'FullIndex',
                  'outputFormat':'HTML',
                  'encoding':'UTF-8',
                  'maxLeftLength':self.n_left,
                  'maxRightLength':self.n_right,
                  'orderStyle':'score',
                  'dir':self.subcorpus,
                  'scopestr':'' # text selection: TO DO?
                  }
        r = get('http://ccl.pku.edu.cn:8080/ccl_corpus/search',params)
        return unescape(r.text)


    def parse_page(self):
        """
        find results (and total number of results) in the page code
        """
        soup = BeautifulSoup(self.__page, 'lxml')
        res = soup.find('table',align='center')
        if res:
            res = res.find_all('tr')
        else:
            return []
        if self.__pagenum == 0:
            self.n_results = min(self.n_results,int(soup.find('td',class_='totalright').find('b').text))
        return res

        
    def parse_result(self,result):
        """
        find hit and its left and right contexts
        in the extracted row of table
        """
        result = result.select('td[align]')
        result = [x.text.strip() for x in result]
        text = ''.join(result)
        idxs = (len(result[0]),len(result[0])+len(result[1]))
        return Target(text,idxs,'',[])

        
    def extract(self):
        n = 0
        while n < self.n_results:
            self.__page = self.get_results()
            rows = self.parse_page()
            if not rows:
                break
            r = 0
            while n < self.n_results and r < len(rows):
                yield self.parse_result(rows[r])
                n += 1
                r += 1
            self.__pagenum += self.__per_page

