from .arkhangelskiy_corpora import PageParser

language = 'yiddish'
results = 'http://web-corpora.net/YNC/search/results.php'

TEST_DATA = {'test_single_query': {'query': 'קאַץ'},
             'test_multi_query': {'query': ['קאַץ', 'ליבע']}
             }

__author__ = 'ustya-k'
__doc__ = \
"""
yid_corpus
==========

API for Modern Yiddish corpus (http://web-corpora.net/YMC/search/).
    
Search Parameters
-----------------
query: str or list([str])
    query or queries
n_results: int, default 100
    number of results wanted
kwic: bool, default True
    kwic format (True) or a sentence (False)
get_analysis: bool, default False
    tags shown (True) or not (False)
"""


class PageParser(PageParser):

    def __init__(self, *args, **kwargs):
        super().__init__(language, results, *args, **kwargs)
