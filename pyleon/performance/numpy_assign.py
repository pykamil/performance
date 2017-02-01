import timeit
import gc
import numpy as np
import pandas as pd
import os

TIMEIT_RUNS = 10
CONTAINER_SIZE = 1000000

def test_div__numpy(a, divisor):
    return a/divisor

def test_mul__numpy(a, divisor):
    val=1./divisor
    b = a*val
    return b

def test_div_assign_numpy(a, divisor):
    a /= divisor
    return a

def test_mul_assign_numpy(a, divisor):
    val=1./divisor
    a *= val
    return a

def test_div__list(a, divisor):
    return [item/divisor for item in a]

def test_mul__list(a, divisor):
    val=1./divisor
    return [item*val for item in a]

def test_div_assign_list(a, divisor):
    for i in range(len(a)):
        a[i] /= divisor
    return a

def test_mul_assign_list(a, divisor):
    val=1./divisor
    for i in range(len(a)):
        a[i] *= val
    return a

def test_div__list2numpy2list(a, divisor):
    a = np.array(a)
    return (a/divisor).tolist()

def test_mul__list2numpy2list(a, divisor):
    val=1./divisor
    a = np.array(a)
    return (a*val).tolist()

def test_div_assign_list2numpy2list(a, divisor):
    a = np.array(a)
    a /= divisor
    return a.tolist()

def test_mul_assign_list2numpy2list(a, divisor):
    val=1./divisor
    a = np.array(a)
    a *= val
    return a.tolist()

setupNumpy = """
import __main__
import numpy as np
from pyleon.performance.utils import CopyCached
cache = CopyCached(np.random.randn(__main__.CONTAINER_SIZE), __main__.TIMEIT_RUNS)
divisor = 2.1234
"""

setupList = """
import __main__
import numpy as np
from pyleon.performance.utils import CopyCached
cache = CopyCached(list(np.random.randn(__main__.CONTAINER_SIZE)), __main__.TIMEIT_RUNS)
divisor = 2.1234
"""

def _test_combinations(f_name, setup, results):
    t = timeit.Timer('__main__.{}(cache(), divisor)'.format(f_name), setup=setup)
    t_run = t.timeit(TIMEIT_RUNS)
    print (f_name, t_run)
    namesplit = f_name.split('_')

    results.append([namesplit[3], namesplit[1], 'assignment' if namesplit[2] else 'arithmetic', t_run])

def performance_test(directory):
    results = []
    functions = ['test_{}_{}_{}'.format(operation, operationType, container) for operation in ['div', 'mul'] for operationType in ['', 'assign'] for container in ['numpy', 'list', 'list2numpy2list']]
    for f in functions:
        _test_combinations(f, setupNumpy if 'numpy' in f else setupList, results)
        gc.collect()
    df = pd.DataFrame(results, columns=['Container', 'Operation', 'Operator', 'Time'])
    df.to_csv(os.path.join(directory, 'numpy_assign.csv'))
    print (df)



