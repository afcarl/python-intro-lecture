About
=====
This is material I prepared for a class. I was too ambitious.

I didn't have time to show numpy/scipy.
I didn't show json-files.
I didn't show virtualenvs.
You should look into these things, they are pure awesomeness.

Files
=====
- *1.py*: Shows scoping by indentation. Python's most discussion-about-this-is-futile-but-fun feature.
- *2.py*: Basic lists, loops, tests, and scope again.
- *3.py*: Duck-typing: OO sans interfaces and inheritance! IMO C++ templates done right :) (Of course I understand it's a dynamic language. No. Stop it.)
- *ipython_log.py*: The log of my live-session, analyzing some CSV data. I added comments to it.
- *test.py*: This will lead to an obvious-in-hindsight, eye-opening realization at some point in your coder's life. Maybe in the future, maybe in the past, maybe now.

Preparations
============
Create (and activate) a "virtual environment", this installs all python-stuff into one directory so you don't mess with your system.

    $ virtual_env env
    $ . env/bin/activate

Install the ipython console and its necessary dependencies. IPython is more user-friendly than the regular python shell

    $ pip install ipython
    $ easy_install readline

Numpy & scipy
-------------
`Numpy` brings performant matrices (called ndarrays) to python. It also includes a GEMM&friends-wrapper called "numpy.dot".
`Scipy` can be compared to a wrapper around LAPACK, FFTPACK and many more.

    $ pip install numpy
    $ pip install scipy

Note that it is possible, but tedious, to link numpy against a HP-BLAS implementation like OpenBLAS, MKL, ACML and friends.
I am still working on a full tutorial for installing numpy+scipy+OpenBLAS. In the meantime, instructions for a
[global install](http://software.intel.com/en-us/articles/numpyscipy-with-intel-mkl) using MKL are provided by Intel.

### Check to which BLAS numpy was linked
If you need to veriy which BLAS implementation your numpy is using, write the following in a python console:

    import numpy.distutils.system_info as sysinfo
    sysinfo.get_info('blas')

This gives you the name of the linked library. You could then `ldd /usr/lib/libblas.so` (if that is the indicated file) to
get a few more details.


### Plotting
`matplotlib` is a plotting library which is very similar to matlab's plotting. I will not introduce it, because I don't like/use matlab's plotting. I like d3.js.

General python introduction
===========================

* `%logstart` is like matlab's `diary` command. Commands starting with a `%`-sign are IPython "magic" commands.

General stuff
-------------

These are my "lecture notes", i.e. what I didn't want to forget to tell you guys.

### Two camps of sci
* Compute compute compute, using known algos
    * Paolo, physicists, chemists
* Discover, discover, discover
    * "Big data", Biologists, Data/Social/Financial Analysts
    * Data transformation *everywhere*
    * Use many tools

* Of course not B/W

### What's Python?
* Scripting language from the 90s (read: young)
* GvR is *the* BDFL (Benevolent Dictator For Life)
* Readable, practical, ... "import this"
* "Dump brain to editor" - Some guy on the internet

### When not to use Python
* High numerical performance is central
* Big GUI code
* Windows only
* You are an IDE hugger
* You are a static typing lover

### When to use Python
* All other cases :)
* Have fun programming
* Glue code
* Prototypes
* Fast development time

Uncleaned notes
---------------
Any other notes I had made quickly but didn't have the time to "cleanup".

TODO:
* ipython: %logon/logstart _ \_i
* Indentation-scoped
* Readable (professors = ['Bientinesi', 'Leibe', 'Lichter'] if 'lucas' not in professors: print('No permission') )
* dynamic typing
    * Still has types: int (c:long), long (c:mpl), float (c:double), complex
* OO+Duck-typing
* numpy?
    * a[x>5]
* Away from OO->dicts+lists(+tuples(+sets))
* (immutability: strings, tuples)
* To functional: map, filter, all/any
* To pythonic: list/dict comprehension
* [bla for i for j] # j is faster
* generators/lazyness
    qsort1 = lambda lst : lst if len(lst) <= 1 else qsort1([i for i in lst[1:] if i < lst[0]]) + [lst[0]] + qsort1([i for i in lst[1:] if i >= lst[0]])
