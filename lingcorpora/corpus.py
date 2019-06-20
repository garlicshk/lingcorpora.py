# python3
# coding=<UTF-8>

from collections import Iterable, deque
import warnings
from time import sleep
from tqdm import tqdm
from .result import Result
from .functions import functions



class Corpus:
    """The object of this class should be instantiated for each corpus. Search is conducted via search method.
    
    Parameters
    ----------
    language: str
        Language ISO 639-3 code for the corpus with combined codes for parallel corpora.
        List of available corpora with corresponding codes:
        
        +--------------+---------------------------------------------------------------+
        | Code         |   Corpus                                                      |
        +==============+===============================================================+
        | ady          |   Adyghe corpus                                               |
        +--------------+---------------------------------------------------------------+
        | alb          |   Albanian corpus                                             |
        +--------------+---------------------------------------------------------------+
        | arm          |   Eastern Armenian corpus                                     |
        +--------------+---------------------------------------------------------------+
        | bam          |   Corpus Bambara de Reference                                 |
        +--------------+---------------------------------------------------------------+
        | bua          |   Buryat corpus                                               |
        +--------------+---------------------------------------------------------------+
        | chr          |   Crimean Tatar corpus                                        |
        +--------------+---------------------------------------------------------------+
        | dan          |   Danish corpus                                               |
        +--------------+---------------------------------------------------------------+
        | deu          |   German corpus                                               |
        +--------------+---------------------------------------------------------------+
        | emk          |   Maninka Automatically Parsed corpus                         |
        +--------------+---------------------------------------------------------------+
        | est          |   Estonian corpus                                             |
        +--------------+---------------------------------------------------------------+
        | grk          |   Modern Greek corpus                                         |
        +--------------+---------------------------------------------------------------+
        | hin          |   Hindi corpus                                                |
        +--------------+---------------------------------------------------------------+
        | jpn_eng      |   Japanese-English subcorpus of JuKuu corpus                  |
        +--------------+---------------------------------------------------------------+
        | jpn_zho      |   Japanese-Chinese subcorpus of JuKuu corpus                  |
        +--------------+---------------------------------------------------------------+
        | kal          |   Kalmyk corpus                                               |
        +--------------+---------------------------------------------------------------+
        | kat          |   Georgian monolingual corpus                                 |
        +--------------+---------------------------------------------------------------+
        | kaz          |   Almaty corpus of the Kazakh language                        |
        +--------------+---------------------------------------------------------------+
        | mon          |   Mongolian corpus                                            |
        +--------------+---------------------------------------------------------------+
        | pol          |   National Corpus of Polish                                   |
        +--------------+---------------------------------------------------------------+
        | rus          |   National Corpus of Russian                                  |
        +--------------+---------------------------------------------------------------+
        | rus_parallel |   Parallel subcorpus of National Corpus of Russian Language   |
        +--------------+---------------------------------------------------------------+
        | rus_pol      |   Polish-Russian Parallel Corpus                              |
        +--------------+---------------------------------------------------------------+
        | sl_dict      |   Spreadthesign sign language dictionary                      |
        +--------------+---------------------------------------------------------------+
        | slk          |   Slovak corpus                                               |
        +--------------+---------------------------------------------------------------+
        | tat          |   Tatar corpus                                                |
        +--------------+---------------------------------------------------------------+
        | udm          |   Udmurt corpus                                               |
        +--------------+---------------------------------------------------------------+
        | yid          |   Modern Yiddish corpus                                       |
        +--------------+---------------------------------------------------------------+
        | zho          |   Center of Chinese Linguistics corpus                        |
        +--------------+---------------------------------------------------------------+
        | zho_eng      |   Chinese-English subcorpus of JuKuu corpus                   |
        +--------------+---------------------------------------------------------------+
        
    verbose: bool, default True
        whether to enable tqdm progressbar.
    sleep_time: int, default 1
        the length of pause between requests to the corpus (in seconds).
        It is required to avoid blocking and corpus breakdown.
    sleep_each: int, default 5
        the number of requests after which a pause is required.
    
    Attributes
    ----------
    doc: str
        Documentation for chosen corpus (after instance creation).
    results: list
        List of all Result objects, each returned by search method.
    failed: list
        List of Result objects where nothing was found.
    """
    def __init__(self, language, verbose=True, sleep_time=1, sleep_each=5):
        """
        Parameters
        ----------
        language: str
            language alias
        verbose: bool
            enable tqdm progressbar
        sleep_time: int
            sleeping time in seconds USELESS?
        sleep_each: int
            sleep after each `sleep_each` request USELESS?
        """
        
        self.language = language
        self.verbose = verbose
        self.__corpus = functions[self.language] 
        self.doc = self.__corpus.__doc__
        self.gr_tags_info = self.__corpus.__dict__.get('GR_TAGS_INFO')

        self.results = list()
        self.failed = deque(list())
        
        self.__warn = \
        """Nothing found for query "%s".\nCall `retry_failed` method to retry failed queries
        """

        self.__pbar_desc = '"%s"'

        if sleep_each < 1:
            raise ValueError('Argument `sleep_each` must  be >= 1')
            
        self.sleep_each = sleep_each
        self.sleep_time = sleep_time
        
    def __getattr__(self, name):
        if name.lower() == 'r':
            return self.results
        
        raise AttributeError("'Corpus' object has no attribute '%s'" % name)

    def __to_multisearch_format(self, arg, arg_name, len_multiplier=1):
        """
        pack <str> or List[str] `arg` to multisearch format
        """
        
        if isinstance(arg, str):
            arg = [arg] * len_multiplier
        
        if not isinstance(arg, Iterable):
            raise TypeError(
                'Argument `%s` must be of type <str> or iterable[str], got <%s>'
                % (arg_name, arg)
            )
            
        return arg

    def get_gr_tags_info(self):
        print(self.gr_tags_info)

    def search(self, query, *args, **kwargs):
        """This is a search function that queries the corpus and returns the results.
        
        Parameters
        ----------
        query: str
            query, for arguments see `params_container.Container`
        
        Example
        -------
        .. code-block:: python

            >>> rus_corp = lingcorpora.Corpus('rus')
            >>> rus_results = rus_corp.search('мешок', n_results = 10)
            >>> rus_results
            "мешок": 100%|███████████████████████████████| 10/10 [00:07<00:00,  1.40docs/s]
            [Result(query=мешок, N=10, params={'n_results': 10, 'kwic': True, 'n_left': None, 'n_right': None, 'query_language': None, 'subcorpus': 'main', 'get_analysis': False, 'gr_tags': None, 'start': 0, 'writing_system': None})]
        """

        query = self.__to_multisearch_format(query, 'query')
        gr_tags = self.__to_multisearch_format(kwargs['gr_tags'], 'gr_tags', len(query)) if kwargs.get('gr_tags') is not None else [None] * len(query)

        if len(query) != len(gr_tags):
            raise ValueError('`query`, `gr_tags` length mismatch')

        _results = list()
        
        for q, c_gr_tags in zip(query, gr_tags):
            kwargs['gr_tags'] = c_gr_tags            
            parser = self.__corpus.PageParser(q, *args, **kwargs)
            R = Result(self.language, parser.__dict__)
                
            for t in tqdm(parser.extract(),
                          total=parser.n_results,
                          unit='docs',
                          desc=self.__pbar_desc % q,
                          disable=not self.verbose
            ):
                
                R.add(t)
            
            if R:
                _results.append(R)
            
            else:
                warnings.warn(self.__warn % q)
                self.failed.append(R)
        
        self.results.extend(_results)
        
        return _results

    def retry_failed(self):
        """
        Apply `.search()` to failed queries stored in `.failed`
        """
        
        if self.failed:
            n_rounds = len(self.failed)
            retrieved = list()
            
            for _ in range(n_rounds):
                R_failed = self.failed.popleft()
                
                # List[<Result>]
                results_new = self.search(R_failed.query,
                                          **R_failed.params
                )
                
                if results_new:
                    retrieved.append(results_new[0])
            
            return retrieved
        
    def reset_failed(self):
        """
        Reset `.failed`
        """
        
        self.failed = deque(list())
