from .arkhangelskiy_corpora import PageParser

language = 'mongolian'
results = 'http://web-corpora.net/MongolianCorpus/search/results.php'

TEST_DATA = {'test_single_query': {'query': 'муур'},
             'test_multi_query': {'query': ['муур', 'хайр']}
             }

__author__ = 'ustya-k'
__doc__ = \
"""
Mongolian Corpus
================

API for Mongolian corpus (http://web-corpora.net/MongolianCorpus/search/).
    
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

    corp = lingcorpora.Corpus('mon')
    results = corp.search('ОХУ', n_results = 10)
    for result in results:
        for i,target in enumerate(result):
            print(i+1,target.text)

.. parsed-literal::

    "ОХУ": 100%|██████████| 10/10 [00:00<00:00, 89.05docs/s]

    1 )1996 Канад Швед ОХУ Бостон АНУ) 
    2 )1997 Канад АНУ ОХУ Женев,Морже Швейцарь) 
    3 )2000 Чех ОХУ Канад Шеллефтео,Умео Швед) 
    4 )2007 Канад ОХУ АНУ Мора,Лександ Швед) 
    5 )2009 Канад Швед ОХУ Оттава Канад) 
    6 )2011 ОХУ Канад АНУ Баффало АНУ) 
    7 )2005 Канад ОХУ Чех Грэнд Форкс,АНУ) 
    8 
    Хагас шигшээгийн хоёр дахь тоглолтод өүхлийн хэсэгтө Канад,Чех,ОХУ гээд хоккейн луухгаруудтай багтсан ч нэг хожигдолгүй хэсэгтээ тэргүүлж,хагас шигшээд шууд шалгарсан өГурван титэмтө Швед  энэ тэмцээнд эхлээд Канад,Шведийн багт хожигдож,ирээдүй нь нилээд бүрхэг болоод байсан ч Норвеги,Чехийн багийг дараалан хожиж плей-оффын эрхээ аваад хагас шигшээд үлдэх эрхийн төлөө Финландын багт тоглолтын цаг дуусахад 4 минут орчим дутуу байхад 1:3-аар хожигдож яваад 3:3 болгож дөнгөсөн,улмаар нэмэлт цагт хожлын шайб оруулан гайхамшигтай ялалт байгуулсан Оросын залуучууд хоорондоо таарсан. 
    9 )2006 Канад ОХУ Финланд Ванкувер Канад) 
    10 .Канада ОХУ 3:5 2:0,1:0,0:5) 

"""


class PageParser(PageParser):

    def __init__(self, *args, **kwargs):
        super().__init__(language, results, *args, **kwargs)
