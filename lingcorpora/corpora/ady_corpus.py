from .arkhangelskiy_corpora import PageParser

language = 'adyghe'
results = 'http://web-corpora.net/AdygheCorpus/search/results.php'

TEST_DATA = {'test_single_query': {'query': 'чэтыу'},
             'test_multi_query': {'query': ['чэтыу', 'хэон']}
             }

__author__ = 'ustya-k'
__doc__ = \
"""
Adyghe Сorpus
=============

API for Adyghe corpus (http://web-corpora.net/AdygheCorpus/search/).

**Search Parameters**

query: str or list([str])
    query or queries
n_results: int, default 100
    number of results wanted
kwic: bool, default True
    kwic format (True) or a sentence (False)
get_analysis: bool, default False
    tags shown (True) or not (False)
    
Example
-------

.. code-block:: python

    corp = lingcorpora.Corpus('ady')
    results = corp.search('лӏыгъэ', n_results=10)
    for result in results:
        for i, target in enumerate(result):
            print(i+1, target.text)

.. parsed-literal::

    "лӏыгъэ": 100%|██████████| 10/10 [00:01<00:00,  5.35docs/s]

    1  «Лӏыгъэ »,«адыгагъ »,«адыгэ хабз » зыфэпӏощтхэм тарихъ, социальнэ ыкӏи психологическэ лъэпсэ къэкӏуапӏэу яӏэхэм тхакӏор алъыплъагъ, ыгъэунэфыгъэх.  
    2 
    Ащ фэдэ зекӏуакӏэр пфэукӏочӏыныри лӏыгъэ ыкӏи цӏыфыгъ. 
    3 
    Лӏыгъэ шъыпкъэ спортым идунай, щыӏэныгъэм ащызепхьан олъэкӏы.  
    4 
    Ащ къикӏырэр нафэ - уцӏыфыным цӏыфыгъэ ищыкӏагъ, цӏыфыгъэм шэн лъэныкъуабэ къызэлъеубыты: лӏыгъэ, гукӏэгъу, шъыпкъэныгъ, хьалэлныгъ ыкӏи нэмыкӏхэр. 
    5 
    Непэ тшъхьэ ӏэтыгъэу «хэку тиӏ » зыкӏэтӏошъурэр чӏыгужъым исхэм лӏыгъэ ахэлъэу, аӏэбжъэнакӏэ хэгъэнагъэу хэкур аухъумагъэшъ ары.  
    6 
    Заом игъогу къинхэм лӏыгъэ къызхагъафэзэ арыкӏуагъэх офицерхэу Дзыбэ Тыркубый, Батышэ Къэрбатыр, Брыцо 
    7 
    Фэсакъ, уижьау чӏэгъэт, лӏыгъэ напэкӏэ султӏаным къегъэгъэзэжь есӏуагъэмэ, дзэр умыгъэзао, къегъаж есӏуагъэп сэ...  
    8 
    Ипсауныгъэ зыпкъ зеуцожьым, зэуапӏэм ӏухьажьыгъ, лӏыгъэ хэлъэу пыим езэуагъ.  
    9 
    Лӏыгъэ хабзэм фэкъаигъагъ, иӏорэ-ишӏэрэ зэтетэу псэугъэ. 
    10 
    — Нэфэ теор уихабзэпышъ, ари лӏыгъэ, тыхьазырыщт.

"""


class PageParser(PageParser):

    def __init__(self, *args, **kwargs):
        super().__init__(language, results, *args, **kwargs)
