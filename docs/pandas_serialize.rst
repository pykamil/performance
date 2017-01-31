Pandas data frame serialization test
====================================

The test compares the number of algorithms to serialize different types of data.

1. **Algorithms**

* **pd_csv** - write/read DataFrame to a comma-separated values (csv) file (build in function)
* **pd_hdf5_fixed** - write/read the contained data to an HDF5 file using HDFStore, format=fixed (build in function)
* **pd_hdf5_table** - write/read the contained data to an HDF5 file using HDFStore, format=table (build in function)
* **pd_Pickle** - Pickle (serialize) object to input file path, version 2 (build in function)
* **cPickle** - cpickle.cPickle (serialize) object to input file path
* **PickleV0** - pickle.Pickle (serialize) object to input file path, version 0
* **PickleV1** - pickle.Pickle (serialize) object to input file path, version 1
* **PickleV2** - pickle.Pickle (serialize) object to input file path, version 2
* **gzPickleV2** - gzipped pickle.Pickle stream, version 2
* **lzmaPickleV2** - lzma pickle.Pickle stream, version 2 - The Lempel–Ziv–Markov chain algorithm
* **pd_msgpack** - msgpack (serialize) object to input file path
* **pd_msgpack_zlib** - msgpack (serialize) object to input file path, compressed with zlib
* **pd_msgpack_blosc** - msgpack (serialize) object to input file path, compressed with zlib
* **pd_json_index** - convert the object to a JSON string - index : dict like {index -> {column -> value}}
* **pd_json_split** - convert the object to a JSON string - split : dict like {index -> [index], columns -> [columns], data -> [values]}
* **pd_json_records** - convert the object to a JSON string - records : list like [{column -> value}, ... , {column -> value}]

2. **Data Types**

* **Text**

  * "|S4" product of *string.ascii_uppercase+string.digits*
  * array(['AAAA', 'AAAB', 'AAAC', 'AAAD', 'AAAE', ...], dtype='|S4')
  
* **Category**

  * A variable, which can take on only a limited, and usually fixed, number of possible values
  * array([b'VVVV', b'BBBB', b'DDDD', b'PPPP', b'VVVV', ...], dtype='|S4')
 
* **Datetime64**

  *  DatetimeIndex(['2000-01-14 17:36:27.867848960', '2000-01-15 05:36:27.867848960', ...], dtype='datetime64[ns]', freq=None, tz=None)
  *  pd.to_datetime(np.linspace(pd.Timestamp(datetime.datetime.now()).value, pd.Timestamp(datetime.datetime.now() + datetime.timedelta(days=1)).value, size))

* **Float64**

  * np.random.randn(size)
  
* **Int64**

  * np.random.random_integers(-1000000, 1000000, size)
  
* **Ones**
  
  * array([1, 1, 1, ......
  * np.ones(size, dtype=np.int)
  
* **RoundFloat**

  * float64 rounded to two decimal places
  * array([  331.68,  -496.86, ..., 59.76,  -920.17, -1883.49], dtype('float64'))
  * np.round( np.random.randn(size)*multiply, decimal)
  
* **Floattoint**

  * **RoundFloat** multiplied by 100 and converted to int
  * array([  33168,  -49686, ..., 5976,  -92017, -188349], dtype('int32'))
  
  
 Results
-------------------

1. A total **saving time** of pandas DataFrame split by algorithm and data type

.. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/pandas_serialize_by_save_all.png

2. A total **saving size** of pandas DataFrame split by algorithm and data type (stacked and histogram representation)

.. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/pandas_serialize_by_size_all.png

.. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/pandas_serialize_by_size_all_histogram.png

3. **Categorical data VS text data size** after serialization in KB.

.. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/pandas_serialize_text_vs_cat.png

3. **round(Float64,2) VS int(round(Float64,2)*100)** data size after serialization in KB.

.. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/pandas_serialize_round.png

4. **Load and Save** for float64 time grouped by algorithm

.. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/pandas_serialize_save_load_float.png

5. Check how **linear** seialization of Datarame is.

.. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/pandas_serialize_text_line.png

.. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/pandas_serialize_text_save_line.png


60+ more charts is available on GitHub_ in zip
 
.. _GitHub: https://github.com/pykamil/performance/blob/master/docs/html/pandas_serialize.zip?raw=true
