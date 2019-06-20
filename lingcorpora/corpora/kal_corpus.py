from .arkhangelskiy_corpora import PageParser

language = 'kalmyk'
results = 'http://web-corpora.net/KalmykCorpus/search/results.php'

TEST_DATA = {'test_single_query': {'query': 'мис'},
             'test_multi_query': {'query': ['мис', 'бәәх']}
             }

__author__ = 'ustya-k'
__doc__ = \
"""
kal_corpus
==========

API for Kalmyk corpus (http://web-corpora.net/KalmykCorpus/search/).
    
Search Parameters
-----------------

query: str or list([str])
    query or queries
n_results: int, default 100
    number of results wanted
kwic: bool, default True
    kwic format (True) or a sentence (False) (True by default)
get_analysis: bool, default False
    tags shown (True) or not (False)
"""


class PageParser(PageParser):

    def __init__(self, *args, **kwargs):
        super().__init__(language, results, *args, **kwargs)
