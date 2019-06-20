from .arkhangelskiy_corpora import PageParser

language = 'greek'
results = 'http://web-corpora.net/GreekCorpus/search/results.php'

TEST_DATA = {'test_single_query': {'query': 'γάτα'},
             'test_multi_query': {'query': ['γάτα', 'αγάπη']}
             }

__author__ = 'ustya-k'
__doc__ = \
"""
grk_corpus
==========

API for Modern Greek corpus (http://web-corpora.net/GreekCorpus/search/).

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
