
Multidimensional numpy arrays
=============================

Creating arrays with more than one dimension
--------------------------------------------

So far we have encountered numpy arrays that have one dimension - their
elements are arranged as a list and they can be accessed using a single index:

.. code:: python

    import numpy as np
    a = np.array([1, 2, 3, 4, 5, 6])

    a[0] # get the 0-th element of the array




.. container:: output

    1



In general numpy arrays can have more than one dimension. One way to
create such array is to start with a 1-dimensional array and use the
numpy ``reshape()`` function that rearranges elements of that array into
a new shape.

.. code:: python

    b = np.reshape(
                   a,     # the array to be reshaped
                   (2,3)  # dimensions of the new array
                  )

.. code:: python

    print(a)  # the original 1-dimensional array


.. container:: output

    [1 2 3 4 5 6]


.. code:: python

    print(b)  # the reshaped array


.. container:: output

    [[1 2 3]
    \  [4 5 6]]


``b`` is a 2-dimensional array, with 2 rows and 3 columns. We can access
its elements by specifying row and column indexes:

.. code:: python

    b[0,2] # get the element in  0-th row and 2-nd column




.. container:: output

    3



.. code:: python

    b[0,2] = 100
    print(b)


.. container:: output

    [[  1   2 100]
    \  [  4   5   6]]


The numpy functions ``zeros()``, ``ones()``, and ``empty()`` can be also
used to create arrays with more than one dimension:

.. code:: python

    c = np.ones((3,4))  # creates an array 3 rows and 4 columns
    print(c)


.. container:: output

    [[ 1.  1.  1.  1.]
    \  [ 1.  1.  1.  1.]
    \  [ 1.  1.  1.  1.]]


Mathematical operations on multidimensional arrays
--------------------------------------------------

Mathematical operations on multidimensional arrays work similarly as for
1-dimensional arrays.

.. code:: python

    a = np.arange(4)
    b = np.reshape(a, (2,2))
    print(b)


.. container:: output

    [[0 1]
    \  [2 3]]


.. code:: python

    c = 10*b  # multiplication by a number
    print(c)


.. container:: output

    [[ 0 10]
    \  [20 30]]


.. code:: python

    d = np.ones((2,2))

    e = b+d  # addition of two arrays of the same dimensions
    print(e)


.. container:: output

    [[ 1.  2.]
    \  [ 3.  4.]]


.. code:: python

    f = b*e  # multiplication of two arrays of the same dimensions
    print(f)


.. container:: output

    [[  0.   2.]
    \  [  6.  12.]]


Notice that array multiplication multiplies corresponding elements of
arrays. In order to perform matrix multiplication of 2-dimensional
arrays we can use the numpy ``dot()`` function:

.. code:: python

    g = np.dot(b, e) # matrix multiplication of b and e
    print(g)


.. container:: output

    [[  3.   4.]
    \  [ 11.  16.]]


Mathematical functions defined by numpy can be applied to
multidimensional arrays:

.. code:: python

    h = np.cos(g)  # compute cosine of all elements of the array g
    print(h)


.. container:: output

    [[-0.9899925  -0.65364362]
    \  [ 0.0044257  -0.95765948]]


Slicing multidimensional arrays
-------------------------------

In order to create a slice of a multidimensional array we need to
specify which part of each dimension we want to select.

.. code:: python

    a = np.reshape(np.arange(30), (5,6)) # create a 5x6 array
    print(a)


.. container:: output

    [[ 0  1  2  3  4  5]
    \  [ 6  7  8  9 10 11]
    \  [12 13 14 15 16 17]
    \  [18 19 20 21 22 23]
    \  [24 25 26 27 28 29]]


.. code:: python

    b = a[1:4, 0:2] #select elements in rows 1-3 and columns 0-1
    print(b)


.. container:: output

    [[ 6  7]
    \  [12 13]
    \  [18 19]]


.. code:: python

    c = a[:3, 2:4] #select elements in rows 0-2 and columns 2-3
    print(c)


.. container:: output

    [[ 2  3]
    \  [ 8  9]
    \  [14 15]]



.. code:: python

        d = a[:, 0] # select all elements in the 0-th column
        print(d)


.. container:: output

        [ 0  6 12 18 24]



**Note.** ``a[i]`` is the same as ``a[i,:]`` i.e. it selects the i-th
row of the array:

.. code:: python

    print(a[1])


.. container:: output

    [ 6  7  8  9 10 11]


Similarly as for 1-dimensional arrays slicing produces a view
of the original array, and changing a slice changes the original array:

.. code:: python

    b = a[:3, :3]
    print(b)


.. container:: output

    [[ 0  1  2]
    \  [ 6  7  8]
    \  [12 13 14]]


.. code:: python

    b[0,0] = 1000
    print(b)


.. container:: output

    [[1000    1    2]
    \  [   6    7    8]
    \  [  12   13   14]]


.. code:: python

    print(a)


.. container:: output

    [[1000    1    2    3    4    5]
    \  [   6    7    8    9   10   11]
    \  [  12   13   14   15   16   17]
    \  [  18   19   20   21   22   23]
    \  [  24   25   26   27   28   29]]


We can use this to change many entries of an array at once

.. code:: python

    a[:4, :4] = 0 # set all entries of the slize to 0
    print(a)


.. container:: output

    [[ 0  0  0  0  4  5]
    \  [ 0  0  0  0 10 11]
    \  [ 0  0  0  0 16 17]
    \  [ 0  0  0  0 22 23]
    \  [24 25 26 27 28 29]]
