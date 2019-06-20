from .arkhangelskiy_corpora import PageParser

language = 'armenian1'
results = 'http://eanc.net/EANC/search/results.php'

TEST_DATA = {'test_single_query': {'query': 'կատու'},
             'test_multi_query': {'query': ['կատու', 'սիրով']}
             }

__author__ = 'ustya-k'
__doc__ = \
"""
arm_corpus
==========
    
API for Eastern Armenian corpus (http://eanc.net).
    
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
