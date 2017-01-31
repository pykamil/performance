import pandas as pd
import numpy as np

def createDataFrame(size):
    df1 = pd.DataFrame(
                        {
                        'A': np.array([ "A{num:07d}".format(num=num) for num in range(size) ], dtype="|S8"),
                        'B': np.array([ "B{num:07d}".format(num=num) for num in range(size) ], dtype="|S8")
                        },
                        index=   np.array([ "K{num:07d}".format(num=num) for num in range(size) ], dtype="|S8")

                     )
    df2 = pd.DataFrame(
                        {
                        'C': np.array([ "C{num:07d}".format(num=num) for num in range(size) ], dtype="|S8"),
                        'D': np.array([ "D{num:07d}".format(num=num) for num in range(size) ], dtype="|S8")
                        },
                        index=   np.array([ "K{num:07d}".format(num=num) for num in range(size) ], dtype="|S8")

                     )
    return df1,df2

def _testPandasMerge(df1, df2):
    pd.merge(df1, df2, left_index=True, right_index=True, how='inner')

def _testDictMerge(df1, df2):
    d={}
    d.update(df1.to_dict())
    d.update(df2.to_dict())
    pd.DataFrame.from_dict(d)

def testPandasMerge(size=1000000):
    df1,df2 = createDataFrame(size)
    _testPandasMerge(df1, df2)
    del df1
    del df2

def testDictMerge(size=1000000):
    df1,df2 = createDataFrame(size)
    _testDictMerge(df1, df2)
    del df1
    del df2
    
