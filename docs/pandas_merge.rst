Pandas Merge
===================

The test compares two ways of marging *DataFrames*.

Code
-------------------

- **pandas.merge**

>>> pd.merge(df1, df2, left_index=True, right_index=True, how='inner')

- **exporting DataFrames to *dict* and merging them**

>>> d={}
>>> d.update(df1.to_dict())
>>> d.update(df2.to_dict())
>>> pd.DataFrame.from_dict(d)
  

Data
-------------------
Input data **df1** and **df2** is in following format:

- df1

  +------------+------------+-----------+
  | Index      |     A      |    B      |
  +============+============+===========+
  | K0000000   |  A0000000  | B0000000  |
  +------------+------------+-----------+
  | K0000001   |  A0000001  | B0000001  |
  +------------+------------+-----------+
  | K0000002   |  A0000002  | B0000002  |
  +------------+------------+-----------+
  |    ...     |     ...    |    ...    |
  +------------+------------+-----------+
  | K0999999   |  A0999999  | B0999999  |
  +------------+------------+-----------+
  
- df2

  +------------+------------+-----------+
  | Index      |     C      |    D      |
  +============+============+===========+
  | K0000000   |  C0000000  | D0000000  |
  +------------+------------+-----------+
  | K0000001   |  C0000001  | D0000001  |
  +------------+------------+-----------+
  | K0000002   |  C0000002  | D0000002  |
  +------------+------------+-----------+
  |    ...     |     ...    |    ...    |
  +------------+------------+-----------+
  | K0999999   |  C0999999  | D0999999  |
  +------------+------------+-----------+
  
Results
-------------------
- Windows - process explorer

In comparison to dict merge, pandas merge has lower memory usage peak and shorter time, however it leaves around 170MB more memory footprint after the end of the merge.

  - pandas merge 
  
    .. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/pandas_merge_pd.png
    
  - pandas dict merge
  
    .. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/pandas_merge_dict.png
    
- Linux - Raspberry Pi 3

CPU and memory usage history for pandas dataframe merge is presented between blue lines. The period between green lines prestents pandas dataframe dict merge.
A yellow line shows difference in memory footprint left between these two merges.

  .. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/pandas_merge_pd_vs_dict.png
