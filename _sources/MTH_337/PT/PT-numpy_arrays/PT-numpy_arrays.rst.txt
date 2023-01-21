
Numpy arrays
============

Numpy array basics
------------------

Numpy is the standard module for doing numerical computations
in Python. It provides tools for writing code which is both easier to
develop and usually a lot faster than it would be without numpy.

We begin by importing numpy:

.. code:: python

    import numpy as np

The main objects provided by numpy are numpy arrays, than in their
simplest form are similar to lists. A list can be converted into a numpy
array using the numpy ``array()`` function:

.. code:: python

    mylist = [1, 2, 3]
    print(numbers)


.. container:: output

    [1, 2, 3]


.. code:: python

    a = np.array(numbers)
    print(numbers_arr)


.. container:: output

    [1 2 3]


A visible difference between lists and numpy arrays is that arrays
are printed without commas separating their elements. We can also use the
``type()`` function to verify that ``a`` is a numpy array:

.. code:: python

    type(mylist)




.. container:: output

    list



.. code:: python

    type(a)




.. container:: output

    numpy.ndarray



One advantage of using numpy arrays that many computations can be
performed on all array elements at once:

.. code:: python

    print(2*a)  # multiplication by a number


.. container:: output

    [2 4 6]


.. code:: python

    print(a**3) # exponentiation


.. container:: output

    [ 1  8 27]


.. code:: python

    a += 10  # incrementing elements of an array
    print(a)


.. container:: output

    [11 12 13]


.. code:: python

    b = np.array([100, 200, 300])

    print(a+b) # addition of arrays


.. container:: output

    [111 212 313]


.. code:: python

    print(b/a) # division of one array by another


.. container:: output

    [  9.09090909  16.66666667  23.07692308]


The numpy module contains implementations of many mathematical functions
(trigonometric, logarithmic etc.) that can be applied to whole numpy
arrays:

.. code:: python

    print(np.sin(a))  # compute sine of every element of an array


.. container:: output

    [-0.99999021 -0.53657292  0.42016704]


In other respects numpy array behave the same way as lists. For example, ``for``
loops work with numpy arrays as usual:

.. code:: python

    x = np.array([1,2,3,4,5,6,8])

    for t in x:
        print(t**2)



.. container:: output

    1
    4
    9
    16
    25
    36
    64


Indexing and slicing operations are also unchanged:

.. code:: python

    x[0] = 100
    print(x)


.. container:: output

    [100   2   3   4   5   6   8]


.. code:: python

    y = x[:4]
    print(y)


.. container:: output

    [100   2   3   4]


Some differences between lists and numpy arrays
-----------------------------------------------

**1.** Lists can contain objects of different types, but in numpy arrays all
objects must be of the same type (integers, floats, strings, booleans
etc).

.. code:: python

    a = np.array([100, 200, 300])  # a is an array of integers
    a[0] = 'hello'                 # assigning a string as an array element results in an error


.. container:: output


    ValueError                                Traceback (most recent call last)

    <ipython-input-67-3c04f588b76c> in <module>()
    1 a = np.array([100, 200, 300])  # a is an array of integers
    ----> 2 a[0] = 'hello'                 # assigning a string as an array element results in an error


    ValueError: invalid literal for int() with base 10: 'hello'


**2.** Lists can be shortened and extended (e.g. using ``append``). The
size of a numpy array is fixed when the array is created and can't be
changed.

**3.** Lists slicing produces a new list, independent of the
original list. For numpy arrays slicing produces a *view* of the
original array; changing a slice changes the original array:

.. code:: python

    a = np.array([1, 2, 3, 4])
    b = a[:3]
    b[0] = 999
    print('b = {}'.format(b))
    print('a = {}'.format(a))


.. container:: output

    b = [999   2   3]
    a = [999   2   3   4]


We can use the ``copy()`` function to get an independent copy of an
array or its slice:

.. code:: python

    a = np.array([1, 2, 3, 4])
    b = np.copy(a[:3])
    b[0] = 999
    print('b = {}'.format(b))
    print('a = {}'.format(a))


.. container:: output

    b = [999   2   3]
    a = [1 2 3 4]


How to create a numpy array
---------------------------

Numpy arrays can be created in several ways:

**1.** The ``np.array()`` function converts a list into a numpy array:

.. code:: python

    a = np.array([1,2,3])
    print(a)


.. container:: output

    [1 2 3]


**2.** ``np.zeros()`` creates an array of zeros of a given length:

.. code:: python

    a0 = np.zeros(5)
    print(a0)


.. container:: output

    [ 0.  0.  0.  0.  0.]


**3.** ``np.ones()`` creates an array of ones:

.. code:: python

    a1 = np.ones(7)
    print(a1)


.. container:: output

    [ 1.  1.  1.  1.  1.  1.  1.]


From here we can easily get an array with any fixed value for its
entries:

.. code:: python

    b = 3.14*a1
    print(b)


.. container:: output

    [ 3.14  3.14  3.14  3.14  3.14  3.14  3.14]


**4.** ``np.empty()`` creates an array of a given length with
unitialized entries (more precisely, values of the array will be equal
to whatever is in the computer memory in the region allocated to the
array) . This is useful if we want to set values of the array at some
later point. For large arrays ``np.empty()`` works faster than
``np.zeros()`` and ``np.ones()``:

.. code:: python

    c = np.empty(4)
    print(c)


.. container:: output

    [  4.94065646e-324   9.88131292e-324   1.48219694e-323   1.97626258e-323]


**Note.** By default ``np.zeros()``, ``np.ones()``, and ``np.empty()``
create arrays of floats, but we can use the ``dtype`` argument to
specify a different data type:

.. code:: python

    a = np.zeros(5, dtype=int)   # creates an array of integers
    print(a)


.. container:: output

    [0 0 0 0 0]


**5.** ``np.arange()`` is similar to the ``range()`` function but
it produces a numpy array:

.. code:: python

    numbers = np.arange(10)
    print(numbers)


.. container:: output

    [0 1 2 3 4 5 6 7 8 9]


.. code:: python

    evens = np.arange(10, 20, 2) # start at 10, stop at 20, increment by 2
    print(evens)


.. container:: output

    [10 12 14 16 18]


**Note.** Arguments of ``np.arange()`` need not be integers:

.. code:: python

    w = np.arange(0.3, 1.0, 0.2) # start at 0.3, stop at 1.0, increment by 0.2
    print(w)


.. container:: output

    [ 0.3  0.5  0.7  0.9]


**6.** ``np.linspace(a, b, n)`` creates an array of ``n`` evenly spaced
points between the numbers ``a`` and ``b``:

.. code:: python

    x = np.linspace(0,1,5)
    print(x)


.. container:: output

    [ 0.    0.25  0.5   0.75  1.  ]




Numpy and matplotlib
--------------------

matplotlib works directly with numpy arrays:

.. code:: python

    import matplotlib.pyplot as plt

    x = np.linspace(-10, 10, 100)
    y = x**2
    plt.plot(x, y)
    plt.show()


.. image::  PT-numpy_arrays-1.svg
   :width: 400 px
   :align: center




Further reading
---------------

`Numpy documentation <https://docs.scipy.org/doc/numpy/>`__ provides a
comprehensive numpy reference and a `quickstart
tutorial <https://docs.scipy.org/doc/numpy/user/quickstart.html>`__.
