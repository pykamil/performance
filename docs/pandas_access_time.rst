DataFrame access time
=======================

1. Operator assigment - timeit

>>> In [1]: import numpy as np
>>>    ...: import pandas as pd
>>>    ...: a = np.arange(1e6)
>>>    ...: df = pd.DataFrame({ 'a' : a,
>>>    ...:                     'b' : np.array(a, copy=True),
>>>    ...:                     'c' : np.array(a, copy=True),
>>>    ...:                     })
>>>    ...:
>>> 
>>> In [2]: v = df['a'].values
>>> 
>>> In [3]: %timeit  -n10 v[:] *= -1
>>> 10 loops, best of 3: 8.25 ms per loop
>>> 
>>> In [4]: %timeit  -n10 df['b'].values[:] *= -1
>>> 10 loops, best of 3: 8.41 ms per loop
>>> 
>>> In [5]: %timeit  -n10 df['c'] *= -1
>>> 10 loops, best of 3: 44.8 ms per loop
>>> 
>>> In [6]: %timeit  -n10 v[:] /= 2.123
>>> 10 loops, best of 3: 22.5 ms per loop
>>> 
>>> In [7]: %timeit  -n10 df['b'].values[:] /= 2.123
>>> 10 loops, best of 3: 22.7 ms per loop
>>> 
>>> In [8]: %timeit  -n10 df['c'] /= 2.123
>>> 10 loops, best of 3: 38.5 ms per loop
>>> 
>>> In [9]: %timeit  -n10 v[:] *= 2.123
>>> 10 loops, best of 3: 8.29 ms per loop
>>> 
>>> In [10]: %timeit  -n10 df['b'].values[:] *= 2.123
>>> 10 loops, best of 3: 8.45 ms per loop
>>> 
>>> In [11]: %timeit  -n10 df['c'] *= 2.123
>>> 10 loops, best of 3: 42.6 ms per loop
>>> 
>>> In [12]: df['a'].equals(df['b'])
>>> Out[12]: True
>>> 
>>> In [13]: df['b'].equals(df['c'])
>>> Out[13]: True

2. Operator assigment - memit

>>> In [1]: import numpy as np
>>>    ...: import pandas as pd
>>>    ...: a = np.arange(1e6)
>>>    ...: df = pd.DataFrame({ 'a' : a,
>>>    ...:                     'b' : np.array(a, copy=True),
>>>    ...:                     'c' : np.array(a, copy=True)
>>>    ...:                     })
>>>    ...:
>>> 
>>> In [2]: %load_ext memory_profiler
>>> 
>>> In [3]: %memit v = df['a'].values
>>> peak memory: 117.39 MiB, increment: 0.23 MiB
>>> 
>>> In [4]: %memit v[:] *= -1
>>> peak memory: 117.49 MiB, increment: 0.10 MiB
>>> 
>>> In [5]: %memit df['b'].values[:] *= -1
>>> peak memory: 117.49 MiB, increment: 0.00 MiB
>>> 
>>> In [6]: %memit df['c'] *= -1
>>> peak memory: 132.30 MiB, increment: 14.80 MiB
>>> 
>>> In [7]: %memit v[:] /= 2.123
>>> peak memory: 117.10 MiB, increment: 0.00 MiB
>>> 
>>> In [8]: %memit df['b'].values[:] /= 2.123
>>> peak memory: 117.10 MiB, increment: 0.00 MiB
>>> 
>>> In [9]: %memit df['c'] /= 2.123
>>> peak memory: 132.51 MiB, increment: 15.41 MiB
>>> 
>>> In [10]: %memit v[:] *= 2.123
>>> peak memory: 117.25 MiB, increment: 0.00 MiB
>>> 
>>> In [11]: %memit df['b'].values[:] *= 2.123
>>> peak memory: 117.25 MiB, increment: 0.00 MiB
>>> 
>>> In [12]: %memit df['c'] *= 2.123
>>> peak memory: 132.30 MiB, increment: 15.05 MiB
