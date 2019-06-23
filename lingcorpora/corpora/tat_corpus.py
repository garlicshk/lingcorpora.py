from .arkhangelskiy_corpora import PageParser

language = 'tatar'
results = 'http://web-corpora.net/TatarCorpus/search/results.php'

TEST_DATA = {'test_single_query': {'query': 'туган'},
             'test_multi_query': {'query': ['туган', 'мәхәббәт']}
             }

__author__ = 'ustya-k'
__doc__ = \
"""
Tatar Corpus
============

API for Tatar corpus (http://web-corpora.net/TatarCorpus/).
    
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

    corp = lingcorpora.Corpus('tat')
    results = corp.search('теле', n_results=10)
    for result in results:
        for i, target in enumerate(result):
            print(i+1, target.text)

.. parsed-literal::

    "теле": 100%|██████████| 10/10 [00:02<00:00,  4.85docs/s]

    1 
    Ир-егетләреңдәй дәртле, Гайрәтле син, татар теле. 
    2 
    гел Гадел Кутуй 348 украин теле. 
    3 
    Аның тагы башы әйләнә башлады, авызы кипте, теле әйләнмәс хәлгә килде. 
    4 
    Хәзер РИУда татар теле күп булмаса да фән буларак укытыла. 
    5 
    — Татар теле һәм әдәбияты. 
    6 
    Хәбибуллин укый торган класска җитәкче итеп беркетелгән ана теле укытучысы белән сөйләште. 
    7 
    Тик шунысы кызганыч һәм сәер, шул кеше мәктәпләрдә милли компонетларны бетерүче мәгънәсез указга ашыгыч рәвештә кул куйды.) Татар теле төрле чорлар кичерде. 
    8 
    Гомумән, җыеп әйткәндә, татар теле синтаксисы галим тарафыннан бербөтен система итеп тирәнтен өйрәнелә һәм нәтиҗәләр 1958 елда «Хәзерге татар әдәби теле: Синтаксис» исемендә басылып чыга. 
    9 
    Шагыйрь әсәрләрендә рус теле аркылы шактый күп санда Көнбатыш Европа телләреннән дә алынмалар кулланылган. 
    10 
    Сүз җаеннан аңлашылганча, мәкаләдә вакытлы матбугат теле турында гына фикер әйтелә, ягъни Г. 

"""


class PageParser(PageParser):

    def __init__(self, *args, **kwargs):
        super().__init__(language, results, *args, **kwargs)
