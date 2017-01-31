Mathematical operations on different conatiners
===================

The test compares how long it takes to do mathematical operations as:

.. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/ab-4.1a_gr_2.5b.png

.. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/sinA_add_arcsinhAdivB.png

using functions:

- BuildinEval - __buildin__.eval
- Numpy
- Numexpr
- Pandas
- PandasNumpy - numpy accessed from pandas dataframe - df['X'].values
- NumexprPandasNumpy - numexpr with PandasNumpy
- PandasEval - pandas eval

Data
-------------------

  >>> a = np.arange(1e6)
  >>> b = np.arange(1e6)
  >>> df = pd.DataFrame({
  >>>    'a' : a,
  >>>    'b' : b
  >>>    })

Code
-------------------
Implementation examples

* Numpy

  >>> a*b-4.1*a > 2.5*b
  
* Numexpr

  >>> ne.evaluate('a*b-4.1*a > 2.5*b')
  
* Pandas

  >>> df['a']*df['b']-4.1*df['a'] > 2.5*df['b']
  
* PandasNumpy

  >>> df['a'].values*df['b'].values-4.1*df['a'].values > 2.5*df['b'].values
  
* NumexprPandasNumpy

  >>> A = df['a'].values
  >>> B = df['b'].values
  >>> ne.evaluate('A*B-4.1*A > 2.5*B')
  
* PandasEval

  >>> df.eval('a*b-4.1*a > 2.5*b')
  
 
Results
-------------------

 .. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/pandas_numexpr_calculation.png
 .. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/pandas_numexpr_comparison.png
 
 Charts are available on GitHub_ in zip
 
 .. _GitHub: https://github.com/pykamil/performance/blob/master/docs/html/pandas_numexpr.zip?raw=true
 
  
