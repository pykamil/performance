import pandas as pd
import numpy as np
import numexpr as ne
from time import time
import gc
import os
import argparse

def test_comparison(results):
    SIZE = 100
    print ("Expr 1")
    a = np.arange(1e6)
    b = np.arange(1e6)
    df = pd.DataFrame({
                        'a' : a,
                        'b' : b
                     })

    _range = range(SIZE)

    gc.disable()
    s = time()
    for _ in _range:
        _ = eval('a*b-4.1*a > 2.5*b', locals())
    e = time()
    bi_time = (e-s)/SIZE
    gc.enable()
    gc.collect()

    gc.disable()
    s = time()
    for _ in _range:
        _ = a*b-4.1*a > 2.5*b
    e = time()
    np_time = (e-s)/SIZE
    gc.enable()
    gc.collect()

    gc.disable()
    s = time()
    for _ in _range:
        _ = ne.evaluate('a*b-4.1*a > 2.5*b')
    e = time()
    ne_time = (e-s)/SIZE
    gc.enable()
    gc.collect()

    gc.disable()
    s = time()
    for _ in _range:
        _ = df['a']*df['b']-4.1*df['a'] > 2.5*df['b']
    e = time()
    pd_time = (e-s)/SIZE
    gc.enable()
    gc.collect()

    gc.disable()
    s = time()
    for _ in _range:
        _ = df['a'].values*df['b'].values-4.1*df['a'].values > 2.5*df['b'].values
    e = time()
    pdnp_time = (e-s)/SIZE
    gc.enable()
    gc.collect()

    A = df['a'].values
    B = df['b'].values
    gc.disable()
    s = time()
    for _ in _range:
        _ = ne.evaluate('A*B-4.1*A > 2.5*B')
    e = time()
    pdne_time = (e-s)/SIZE
    gc.enable()
    gc.collect()

    gc.disable()
    s = time()
    for _ in _range:
        _ = df.eval('a*b-4.1*a > 2.5*b')
    e = time()
    pde_time = (e-s)/SIZE
    gc.enable()
    gc.collect()

    #print ('Iter:', it_time)
    print ('BuildIn:', bi_time)
    print ('Numpy:', np_time)
    print ('Numexpr:', ne_time)
    print ('Pandas:', pd_time)
    print ('PandasNumpy:', pdnp_time)
    print ('NumexprPandasNumpy:', pdne_time)
    print ('PandasEval:', pde_time)

    results.append(['Comparison', 'BuildinEval', bi_time])
    results.append(['Comparison', 'Numpy', np_time])
    results.append(['Comparison', 'Numexpr', ne_time])
    results.append(['Comparison', 'Pandas', pd_time])
    results.append(['Comparison', 'PandasNumpy', pdnp_time])
    results.append(['Comparison', 'NumexprPandasNumpy', pdne_time])
    results.append(['Comparison', 'PandasEval', pde_time])

def test_calc(results):
    SIZE = 100
    print ("Expr 2")
    a = np.arange(1e6)
    b = np.arange(1e6)
    df = pd.DataFrame({
                        'a' : a,
                        'b' : b
                     })

    _range = range(SIZE)

    gc.disable()
    s = time()
    for _ in _range:
        X = np.sin(a) + np.arcsinh(a/b)
    e = time()
    np_time = (e-s)/SIZE
    gc.enable()
    gc.collect()

    gc.disable()
    s = time()
    for _ in _range:
        _ = ne.evaluate('sin(a) + arcsinh(a/b)')
    e = time()
    ne_time = (e-s)/SIZE
    gc.enable()
    gc.collect()

    gc.disable()
    s = time()
    for _ in _range:
        _ = np.sin(df['a']) + np.arcsinh(df['a']/df['b'])
    e = time()
    pd_time = (e-s)/SIZE
    gc.enable()
    gc.collect()


    A = df['a'].values
    B = df['b'].values
    gc.disable()
    s = time()
    for _ in _range:
        _ = ne.evaluate('sin(A) + arcsinh(A/B)')
    e = time()
    pdne_time = (e-s)/SIZE
    gc.enable()
    gc.collect()

    gc.disable()
    s = time()
    for _ in _range:
        _ = np.sin(df['a'].values) + np.arcsinh(df['a'].values/df['b'].values)
    e = time()
    pdnp_time = (e-s)/SIZE
    gc.enable()
    gc.collect()

    gc.disable()
    s = time()
    for _ in _range:
        X = df.eval('sin(a) + arcsinh(a/b)')
    e = time()
    pde_time = (e-s)/SIZE
    gc.enable()
    gc.collect()

    print ('Numpy:', np_time)
    print ('Numexpr:', ne_time)
    print ('Pandas:', pd_time)
    print ('PandasNumpy:', pdnp_time)
    print ('NumexprPandasNumpy:', pdne_time)
    print ('PandasEval:', pde_time)

    results.append(['Calculation', 'Numpy', np_time])
    results.append(['Calculation', 'Numexpr', ne_time])
    results.append(['Calculation', 'Pandas', pd_time])
    results.append(['Calculation', 'PandasNumpy', pdnp_time])
    results.append(['Calculation', 'NumexprPandasNumpy', pdne_time])
    results.append(['Calculation', 'PandasEval', pde_time])

def performance_test(directory=''):
  '''
    Exmple resutlts
          Operation          DataSource      Time
    0    Comparison         BuildinEval  0.090734
    1    Comparison               Numpy  0.090342
    2    Comparison             Numexpr  0.014666
    3    Comparison              Pandas  0.071340
    4    Comparison         PandasNumpy  0.089584
    5    Comparison  NumexprPandasNumpy  0.014498
    6    Comparison          PandasEval  0.057700
    7   Calculation               Numpy  0.737929
    8   Calculation             Numexpr  0.187166
    9   Calculation              Pandas  0.723186
    10  Calculation         PandasNumpy  0.740764
    11  Calculation  NumexprPandasNumpy  0.189698
    12  Calculation          PandasEval  0.237735
  '''
    results = []
    test_comparison(results)
    test_calc(results)
    df = pd.DataFrame(results, columns=['Operation', 'DataSource', 'Time'])
    path_csv = os.path.join(directory, 'pandas_numexpr.csv')
    df.to_csv(path_csv)
    print ("Saved csv to {}".format(path_csv))
    print (df)
    return df

def main():

  parser = argparse.ArgumentParser()
  parser.add_argument('-d', '--dir', default='')
  parsed = parser.parse_args()
  directory = parsed.dir
  directory = os.path.abspath(directory)

  if not os.path.exists(directory):
      os.makedirs(directory)
      print ("Created {}".format(directory))
  else:
      print ("Already exist {}".format(directory))

  np.seterr(divide='ignore', invalid='ignore')
  df = performance_test(directory=directory)

if __name__ == '__main__':
    print ("Pandas numexpr test")
    main()
