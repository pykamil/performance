import sys
import pandas as pd
import pickle
import cPickle
from functools import partial
from time import time
import gc
import numpy as np
import os
from itertools import product
import string
import gzip
import lzma
import datetime

KB = 2.**10

def stringProducts(size, wordSize=4):
    '''
    ['AAAA', 'AAAB', 'AAAC', 'AAAD', 'AAAE', ...]
    '''
    return [ ''.join(prod) for prod in list(product(string.ascii_uppercase+string.digits, repeat=wordSize))][:size]

def stringCategory(size, wordSize=4):
    '''
    array([b'VVVV', b'BBBB', b'DDDD', b'PPPP', b'VVVV', ...], dtype='|S4')
    '''
    return np.array(np.random.choice([c*4 for c in string.ascii_uppercase], size), dtype="|S4")

def randomInt(size):
    return np.random.random_integers(-1000000, 1000000, size)

def randomFloat(size):
    return np.random.randn(size)

def timeRange(size):
    '''
    DatetimeIndex(['2017-01-14 17:36:27.867848960',
               '2017-01-15 05:36:27.867848960',
               '2017-01-15 17:36:27.867848960',
               ...],
              dtype='datetime64[ns]', freq=None, tz=None)
    '''
    return pd.to_datetime(np.linspace(pd.Timestamp(datetime.datetime.now()).value, pd.Timestamp(datetime.datetime.now() + datetime.timedelta(days=1)).value, size))

def floatRound(size, decimal=2, multiply=1000):
    '''
    array([  331.68,  -496.86, ..., 59.76,  -920.17, -1883.49], dtype('float64'))
    '''
    return np.round( np.random.randn(size)*multiply, decimal)

def floatRoundToInt(size, decimal=2, multiply=1000):
    '''
    array([  33168,  -49686, ..., 5976,  -92017, -188349], dtype('int32'))
    '''
    a = floatRound(size, decimal, multiply)*(10**decimal)
    a_max = np.max(a)
    a_min = np.min(a)

    intTypes = [np.int8, np.int16, np.int32]
    for intType in intTypes:
        iiinfo = np.iinfo(intType)
        if a_max <= iiinfo.max and a_min >= iiinfo.min:
            return a.astype(intType)

    return a.astype(np.int64)


def timeit(func, n=5):
    gc.disable()
    start = time()
    for i in range(n):
        func()
    end = time()
    gc.enable()
    gc.collect()
    return (end - start) / n

def pd_csv_save(s, f):
    s.to_csv(f)
def pd_csv_load(f):
    pd.read_csv(f)

def cPickle_save(s, f):
    with open(f, "wb") as fout:
        cPickle.dump(s, fout, protocol=0)
def cPickle_load(f):
    with open(f, "rb") as fin:
        cPickle.load(fin)

def PickleV0_save(s, f):
    with open(f, "wb") as fout:
        pickle.dump(s, fout, protocol=0)
def PickleV0_load(f):
    with open(f, "rb") as fin:
        pickle.load(fin)

def PickleV1_save(s, f):
    with open(f, "wb") as fout:
        pickle.dump(s, fout, protocol=1)
def PickleV1_load(f):
    with open(f, "rb") as fin:
        pickle.load(fin)

def PickleV2_save(s, f):
    with open(f, "wb") as fout:
        pickle.dump(s, fout, protocol=2)
def PickleV2_load(f):
    with open(f, "rb") as fin:
        pickle.load(fin)

def gzPickleV2_save(s, f):
    with gzip.open(f, "wb") as fout:
        pickle.dump(s, fout, protocol=2)
def gzPickleV2_load(f):
    with gzip.open(f, "rb") as fin:
        pickle.load(fin)

def lzmaPickleV2_save(s, f):
    pickledata=pickle.dumps(s)
    with open(f, "wb") as fo:
        fo.write(lzma.compress(pickledata))
def lzmaPickleV2_load(f):
	with open(f, "rb") as fo:
		pickle.loads(lzma.decompress(fo.read()))

def pd_Pickle_save(s, f):
    s.to_pickle(f)
def pd_Pickle_load(f):
    pd.read_pickle(f)

def pd_hdf5_fixed_save(s, f):
    s.to_hdf(f, 'bar', format='fixed', mode='w')
def pd_hdf5_fixed_load(f):
    pd.read_hdf(f, 'bar')

def pd_hdf5_table_save(s, f):
    s.to_hdf(f, 'bar', format='table', mode='w')
def pd_hdf5_table_load(f):
    pd.read_hdf(f, 'bar')

def pd_msgpack_save(s, f):
    s.to_msgpack(f)
def pd_msgpack_load(f):
    pd.read_msgpack(f)

def pd_msgpack_zlib_save(s, f):
    s.to_msgpack(f, compress='zlib')
def pd_msgpack_zlib_load(f):
    pd.read_msgpack(f)

def pd_msgpack_blosc_save(s, f):
    s.to_msgpack(f, compress='blosc')
def pd_msgpack_blosc_load(f):
    pd.read_msgpack(f)

def pd_json_index_save(s, f):
    s.to_json(f, orient='index')
def pd_json_index_load(f):
    pd.read_json(f, orient='index')

def pd_json_split_save(s, f):
    s.to_json(f, orient='index')
def pd_json_split_load(f):
    pd.read_json(f, orient='index')

def pd_json_records_save(s, f):
    s.to_json(f, orient='index')
def pd_json_records_load(f):
    pd.read_json(f, orient='index')

def sizeF(f):
    return os.path.getsize(f)

def serialize_test(directory='', filename='df.csv'):

    serialization_types = ['pd_csv', 'pd_hdf5_fixed', 'pd_hdf5_table', 'pd_Pickle', 'cPickle', 'PickleV0', 'PickleV1', 'PickleV2', 'gzPickleV2', 'lzmaPickleV2', 'pd_msgpack', 'pd_msgpack_zlib', 'pd_msgpack_blosc', 'pd_json_index', 'pd_json_split', 'pd_json_records']
    fname = "pandas_performance"
    runs_dict = { name: (globals()["{}_load".format(name)], globals()["{}_save".format(name)]) for name in serialization_types}

    headers = ['Format', 'DataType', 'Size', 'Save', 'Load', 'FileSize (KB)']
    result = []
    for size in [1000, 5000, 10000, 50000, 100000, 500000]:
        dataset = pd.DataFrame({'text'       : stringProducts(size),
                                'float64'    : randomFloat(size),
                                'category'   : stringCategory(size),
                                'int64'      : randomInt(size),
                                'datetime64' : timeRange(size),
                                'ones'       : np.ones(size, dtype=np.int),
                                'roundFloat' : floatRound(size),
                                'floatToInt' : floatRoundToInt(size),
                                })

        dataset['float64'] = dataset['float64'].astype(np.float64)
        dataset['int64'] = dataset['int64'].astype(np.int64)
        dataset['category'] = dataset['category'].astype('category')

        print ("#"*28)
        print (dataset.dtypes)
        print ("#"*28)

        dfs_dict = {col:dataset[[col]] for col in dataset.columns}

        for name, (loadF, saveF) in runs_dict.items():
            for col, data in dfs_dict.iteritems():
                print (size, name, col)

                try:
                    #result.append([name, col,         size, timeit(saveF(data, fname)),       timeit(loadF(fname)), round(sizeF()/KB, 2)])
                    saveTime = timeit(partial(saveF, data, fname))
                    loadTime = timeit(partial(loadF, fname))
                    fileSize = round(sizeF(fname)/KB, 2)
                    result.append([name, col, size, saveTime, loadTime, fileSize])
                    if os.path.exists(fname):
                        os.remove(fname)
                except NotImplementedError:
                    #case for NotImplementedError: Cannot store a category dtype in a HDF5 dataset that uses format="fixed". Use format="table".
                    result.append([name, col, size, 0., 0., 0.])
                except Exception:
                    raise

    df_result = pd.DataFrame(result, columns=headers)
    df_result_size = len(df_result)
    pd.set_option("display.max_rows",df_result_size)

    df_result.to_csv(os.path.join(directory, filename))
    print (df_result)


serialize_test(directory, filename)

