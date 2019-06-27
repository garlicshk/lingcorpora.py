from .arkhangelskiy_corpora import PageParser

language = 'udmurt'
results = 'http://web-corpora.net/UdmurtCorpus/search/results.php'

TEST_DATA = {'test_single_query': {'query': 'кыл'},
             'test_multi_query': {'query': ['кыл', 'яра']}
             }

__author__ = 'ustya-k'
__doc__ = \
"""
Udmurt Сorpus
=============
    
API for Udmurt corpus (http://web-corpora.net/UdmurtCorpus/search/).
    
**Search Parameters**

query: str or list([str]):
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

    corp = lingcorpora.Corpus('udm')
    results = corp.search('кыл', n_results=10)
    for result in results:
        for i, target in enumerate(result):
            print(i+1, target.text)

.. parsed-literal::

    "кыл": 100%|██████████| 10/10 [00:01<00:00,  5.64docs/s]

    1 
    Абхазилэн обороная министрез кылсёoӥc: Грузия ожмаськонзэ ӧc дугдытыке, со кыкетӥ фронт усьтоз.  
    2 
    Ми палан 80 процентэз улӥсьёс - удмуртъёс, нош школаын удмурт кыл быдтэмын.  
    3 
    Озьы шуи ке, янгыш уг луы, дыр, уго ужало соос «Ӟеч-а, бур-а, удмурт кыл » книгая, кудӥз чакламын воксё удмуртсэ тодӥсьтэм ӟуч нылпиослы. 
    4 
    Соос пӧлын нимаз ӧвӧл ӟуч литература, вань ӟуч кыл но литература.  
    5 
    Одӥг кыл гинэ верай вал. 
    6 
    История уг яраты трос кыл быдтэмез, со эскере документъёсты, учыръёсты.  
    7 
    Азьвыл аръёсы сямен ик, Гурт шудонъёсын ыбылӥськонэ пыриськозы полиатлонистъёс но ёрос йыръёс гинэ.- Мугорез кыдатонэ трос калыкез кыскон понна специалистъёс но тырмыт луыны кулэ, дыр?- Ёросысь мугорез кыдатон культураез но спортэз азинтон удысын 70 мурт ужа: нылпи садъёсын, школаосын физкультураез нуисьёс, профессиональной колледжысь преподавательёс, предприятиосын но организациосын 6 мурт спортэз азинтон понна кыл кутэ.  
    8 
    Мон валасько семьяе азьын кыл кутонме,«пӧйшурась » луэмме.- Мон малпай вал, али Д. Донцовалэн кадь книгаос гинэ коньдон ваё...- Кудласянь учкод ведь гожъямъёсыд шоры.  
    9 
    Нылкышно пал кыл но ӧз тоды ӟуч сямен.  
    10 
    Базарын китай сямен вераськимы ни, отын, конешно, дасо кыл но тырмыт. 

"""


class PageParser(PageParser):

    def __init__(self, *args, **kwargs):
        super().__init__(language, results, *args, **kwargs)
