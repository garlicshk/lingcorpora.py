from .arkhangelskiy_corpora import PageParser

language = 'kazakh'
results = 'http://web-corpora.net/KazakhCorpus/search/results.php'

TEST_DATA = {'test_single_query': {'query': 'мысық'},
             'test_multi_query': {'query': ['мысық', 'сүю']}
             }

__author__ = 'ustya-k'
__doc__ = \
"""
kaz_corpus
==========
    
API for Almaty corpus of the Kazakh language
(http://web-corpora.net/KazakhCorpus/search/).
    
Search Parameters
-----------------
query: str or list([str]):
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
