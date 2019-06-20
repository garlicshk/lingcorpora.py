from .arkhangelskiy_corpora import PageParser

language = 'adyghe'
results = 'http://web-corpora.net/AdygheCorpus/search/results.php'

TEST_DATA = {'test_single_query': {'query': 'чэтыу'},
             'test_multi_query': {'query': ['чэтыу', 'хэон']}
             }

__author__ = 'ustya-k'
__doc__ = \
"""
ady_corpus
==========

API for Adyghe corpus (http://web-corpora.net/AdygheCorpus/search/).

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
