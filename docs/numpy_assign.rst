Compares numpy and list arithmetical operations
===============================================

The test checks following performance:

1. **Multiplication VS Division**

  .. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/x1y.png
  
  VS
  
  .. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/xy.png  
  
2. **Arithmetic operators VS Assignment operators**

  +----------------+--------------------------------------+----------------------------------+
  | Operators      |     Arithmetic                       |   Assignment                     |
  +================+======================================+==================================+
  | Multiplication | T T::operator*(const T2 &b) const;   | T& T::operator *=(const T2& b);  |
  +----------------+--------------------------------------+----------------------------------+
  | Division       | T T::operator/(const T2 &b) const;   | T& T::operator /=(const T2& b);  |
  +----------------+--------------------------------------+----------------------------------+  
  
3. **list** VS **numpy** VS **list-->numpy-->list** 
4. **list comprehension** VS **list iteration**

Code
-------------------
Implementation examples

* numpy divison

  >>> def test_div__numpy(a, divisor):
  >>>   return a/divisor

* numpy multiplication assign

  >>> def test_mul_assign_numpy(a, divisor):
  >>>   val=1./divisor
  >>>   a *= val
  >>>   return a 
  
* list multiplication

  >>> def test_mul__list(a, divisor):
  >>>   val=1./divisor
  >>>   return [item*val for item in a]
    
* list2numpy2list multiplication

  >>> def test_mul_assign_list2numpy2list(a, divisor):
  >>>   val=1./divisor
  >>>   a = np.array(a)
  >>>   a *= val
  >>>   return a.tolist()

Results
-------------------

 .. image:: https://raw.githubusercontent.com/pykamil/performance/master/docs/img/numpy_assign__all.png
 
 More charts is available on GitHub_ in zip
 
 .. _GitHub: https://github.com/pykamil/performance/blob/master/docs/html/numpy_assign.zip?raw=true
   
