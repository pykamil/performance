Numpy array creation
====================

A new array filled in with the same value 
----------------------------------------------------------

>>> In [1]: import numpy as np
>>> In [2]: SIZE=1000
>>> In [3]: VALUE = np.int64(1e7)

>>> In [4]: %timeit -n100000 a = np.empty(SIZE, dtype=np.int64); a.fill(VALUE)

100000 loops, best of 3: **14.6 µs** per loop

>>> In [5]: %timeit -n100000 a = np.empty(SIZE, dtype=np.int64); a[:]=VALUE

100000 loops, best of 3: **15 µs** per loop

>>> In [6]: %timeit -n100000 a = np.full(SIZE, VALUE, dtype=np.int64)

100000 loops, best of 3: **19.6 µs** per loop

>>> In [13]: %timeit -n100000 a = np.zeros(SIZE, dtype=np.int64)+VALUE

100000 loops, best of 3: **27.2** µs per loop

>>> In [7]: %timeit -n100000 a = np.ones(SIZE, dtype=np.int64)*VALUE

100000 loops, best of 3: **39.4 µs** per loop

>>> In [8]: %timeit -n100000 a = np.repeat(VALUE,(SIZE))

100000 loops, best of 3: **77.3 µs** per loop

>>> In [9]: %timeit -n100000 a = np.tile(VALUE,[SIZE])

100000 loops, best of 3: **116 µs** per loop

>>> In [10]: %timeit -n100000 a = np.array([VALUE]*SIZE)

100000 loops, best of 3: **623 µs** per loop
