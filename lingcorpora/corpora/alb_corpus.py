from .arkhangelskiy_corpora import PageParser

language = 'albanian'
results = 'http://web-corpora.net/AlbanianCorpus/search/results.php'

TEST_DATA = {'test_single_query': {'query': 'mace'},
             'test_multi_query': {'query': ['mace', 'dua']}
             }

__author__ = 'ustya-k'
__doc__ = \
"""
Albanian Сorpus
===============
    
API for Albanian corpus (http://web-corpora.net/AlbanianCorpus/search/).

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

    corp = lingcorpora.Corpus('alb')
    results = corp.search('shqipe', n_results=10)
    for result in results:
        for i, target in enumerate(result):
            print(i+1, target.text)
    
.. parsed-literal::

    "shqipe": 100%|██████████| 10/10 [00:04<00:00,  2.02docs/s]

    1  «Shqiptarët po blejnë banesa në Nish », apo «Shqiptarët‘pushtojnë’Nishin » – ishin tituj bombastikë të cilët para disa ditësh gdhinë në shtypin tonë, ndërsa po të bëni një kërkim në Google me cilindo variant të tij, do të shihni se këtë lajm e kanë botuar pothuajse të gjitha portalet në internet në gjuhën shqipe nga të gjitha territoret e banuara nga shqiptarët. 
    2 
    Dyke u hapur shkolla shqipe e Korçës – siç pamë përmes aq mundimesh dhe intrigash dhe mjerimesh-shoqërisë Shqiptare të Kollonisë së Bukureshtit i-u hap dhe asaj një përkujdesje e re, një vepërim tjetër.  
    3 
    Këtë mendim ndan edhe Isen Bajrami, njëri prej iniciatorëve për themelimin e Këshillit të prindërve për formimin e paralele shqipe të ciklit të lartë, që u formua në vitin 2007. «Më distancuan prej Këshillit duke më quajtur të paaftë në gjeten e zgjidhjes së problemit afatgjatë, pasi i orientuan negociatat me MASH-in për ndërtimin e një shkolle të re », tregon Bajrami.  
    4 
    Mendoni se mund të ketë dëshmi të shkruara që e çojnë historinë e gjuhës shqipe para Buzukut? 
    5 
    Ai kërkoi besimin që në mandatin e ardhshëm katërvjeçar të zgjidh përfundimisht çështjen e përdorimit të gjuhës shqipe, zbutjen e papunësisë, hapjen e vendeve të reja të punës.  
    6 
    Përmes protestës, Beqiri ka njoftuar se shqiptarët e Luginës së Preshevës do të kërkojnë që të ketë tekste shkollore në gjuhën shqipe ngase nxënësit, sipas tij, vazhdojnë të zhvillojnë mësim me shënime, por jo me tekste shkollore. 
    7 
    Çdo ditë përballemi me gabime akute dhe deformime të gjuhës shqipe nëpër mediume (media të shkruar dhe vizive, forume online etj), çdo ditë shohim se si gjuha shqipe po venitet nga debate të vakta televizive dhe diskurset e forta mbi dialektet që e formojnë atë.  
    8 
    Duke jetuar në një botë ku bursa e vlerave të mirëfillta dhe të patjetërsueshme artistike përzihet keqazi me bursën e interesave dhe vlerave të ndryshueshme të tregut, lëvruesit e letrave shqipe, me synimin për të qenë të botuar jashtë vendit, kanë nisur të lëshojnë jo pak pe në drejtim të «invariableve » për t’u kapur pas «variableve » letrare, duke u përpjekur shpesh të lëvrojnë një mori vlerash të luhatshme, në mos të dyshimta, të cilat duket se grishin fort një lloj kërshërie të veçantë ndaj asaj që ndodh brenda izolimit në përgjithësi, por dhe ndaj vuajtjes njerëzore në veçanti.  
    9 
    Abetaret e Naum Veqilharxhit luajtën një rol të rëndësishëm në Rilindjen Shqiptare, hodhën hapat e parë të arsimit në gjuhën shqipe. 
    10 
    Nuk ishte e rastit as edhe prirja e disa klerikëve për të futur në shërbesat kishtare edhe gjuhën shqipe.  
    
"""


class PageParser(PageParser):

    def __init__(self, *args, **kwargs):
        super().__init__(language, results, *args, **kwargs)
