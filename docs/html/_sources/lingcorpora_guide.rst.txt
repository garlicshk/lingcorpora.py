
Making New API
==============

Main concept
------------

-  Search is done via ``Corpus`` object (``search`` method)
-  Each API of a corpus, dictionary, etc. is a ``PageParser`` class (see
   below) which has method ``.extract()``.
-  ``PageParser.extract()`` is a generator (see ``yield`` in Python) of
   ``Target`` objects (individual hits).
-  ``PageParser`` inherits from ``Container``, which is a class in
   ``params_container.py`` and contains all possible parameters for
   corpora.
-  All ``Target`` objects are collected in ``search`` (in the ``Corpus``
   object) into the ``Result`` object.
-  Documentation for users can be found
   `here <https://lingcorpora.github.io/lingcorpora.py/docs.html>`__

To make a new API
-----------------

1.  Make a ``PageParser`` object
2.  It inherits from ``Container`` and ``Container`` constructor is
    called in ``__init__`` (see example below)
3.  It has method ``extract()`` which ``yield``\ s ``Target`` objects
4.  All other (auxiliary) parameters in ``PageParser`` should be
    encapsulated (add to underscores ``__`` to their names)
5.  You should pass to ``Target`` object the following information:
6.  whole sentence (``text``) - string
7.  indices (``idxs``) of the target in the sentence: ``l`` and ``r``
    such that target == ``text[l:r]`` - tuple
8.  metadata (``meta``) (document name, author, year, etc.) - string. If
    there is no meta, then pass empty string
9.  grammar tags (``tags``) - dict. If there are no tags, pass empty
    dict
10. for parallel corpora: translation (``transl``) - translation from
    ``queryLanguage`` to another language
11. for parallel corpora: language (``lang``) - the other language (not
    ``queryLanguage``) in the example pair
12. **Important**: if there are several target occurrences in one
    example, you should split them into **separate** Target objects.
13. Write the docstring ``__doc__`` and the author ``__author__`` before
    ``PageParser``
14. Name the file *langcode*\ \_corpus.py and place it into the
    ``corpora`` directory. *langcode* stands for `ISO 639-3
    code <https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`__
15. For testing purposes querying data must be provided via ``<dict>``
    named ``TEST_DATA`` (see template below for details)
16. If you would like to add new search parameters, open
    ``params_container.py`` and add this parameter to the arguments
    (**do not forget default value**) and attributes.
17. Make a pull request and if API is OK, we will:
18. Add it to the package
19. Include it in the docs

API template
------------

.. code:: ipython3

    from params_container import Container
    from target import Target
    
    
    __author__ = ''
    # The docs should be in reST format
    # The header is the name of the module
    # The subheader is 'Search Parameters'
    # e.g:
    # pol_corpus
    # ==========
    # 
    # API for National Corpus of Polish (http://nkjp.pl/)
    # 
    # Search Parameters
    # ------------------
    # query: str:
    #    Search by word.
    # n_results: int, default 100
    #     Number of results.
    # ...
    __doc__ = \
    """
    """
    
    # <dict> of querying data passed to `Corpus.search` as kwargs while testing
    # keys and types to be preserved
    
    TEST_DATA = {'test_single_query': {'query': <str>, ...},                            # {arg: value, ...}
                 'test_multi_query': {'query': [<str 1>, <str 2>, ... <str N>], ...}    # {arg: value, ...}
                }
    
    
    class PageParser(Container):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # inner auxiliary attributes:
            # self.__page = None
            # self.__pagenum = 0
            # ...
        
        def any_method_for_getting_the_results(self):
            pass
        
        # ...
        
        def any_method_for_getting_the_results_10(self):
            pass
        
        def extract(self):
            """
            --- Generator of found occurrences as `Target` types
                Query.search() uses this method---
            """
            # ...
            
            # for each occurrence found we pass `Target` object,
            # describing the occurrence, to Query.search()
            # for parallel corpora also transl and lang
            for text, idxs, meta, tags in found:
                yield Target(text, idxs, meta, tags)
