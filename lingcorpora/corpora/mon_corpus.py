from .arkhangelskiy_corpora import PageParser

language = 'mongolian'
results = 'http://web-corpora.net/MongolianCorpus/search/results.php'

TEST_DATA = {'test_single_query': {'query': 'муур'},
             'test_multi_query': {'query': ['муур', 'хайр']}
             }

__author__ = 'ustya-k'
__doc__ = \
"""
mon_corpus
==========

API for Mongolian corpus (http://web-corpora.net/MongolianCorpus/search/).
    
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
