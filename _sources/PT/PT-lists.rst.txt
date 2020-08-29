
Lists, ranges and "for" loops
=============================

Lists
-----

Lists are a type of a container - they contain a number of other
objects: numbers, strings, even other lists. A list is an ordered
sequence of such objects, identified by surrounding square brackets
``[]``. List elements can be of any type, and can be of different types
within the same list. Lists are *mutable*, i.e. once they are created,
elements can be added to them, replaced or deleted.

Here are some examples of operations on lists:

Use square brackets to create a list:

.. code:: python

    mylist = [1, 'hello', 3.14]
    print(mylist)


.. container:: output

    [1, 'hello', 3.14]


``len()`` returns the number of elements in a list:

.. code:: python

    print(len(mylist))


.. container:: output

    3


Adding two lists makes a new list by concatenation:

.. code:: python

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = list1 + list2
    print(list3)


.. container:: output

    [1, 2, 3, 4, 5, 6]


Multiplying a list by an integer repeats the list:

.. code:: python

    list1 = ['a', 'b', 'c']
    list2 = 3*list1
    print(list2)


.. container:: output

    ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']


Use empty square brackets to create an empty list:

.. code:: python

    mylist = []
    print(mylist)


.. container:: output

    []


``append()`` adds an element to the end of a list:

.. code:: python

    mylist = ['a','b']
    mylist.append('c')
    print(mylist)


.. container:: output

    ['a', 'b', 'c']



Testing if an element is in a list:

.. code:: python

    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    12 in primes




.. container:: output

    False



.. code:: python

    13 in primes




.. container:: output

    True



Indexing
~~~~~~~~

Individual elements of a list can be accessed using their indexes
enclosed in square brackets. Indexing of list elements starts with 0:

.. code:: python

    elements = ['H','He','Li','Be','B','C']
    print(elements[0])
    print(elements[1])


.. container:: output

    H
    He


Negative indexes can be used to access elements counting from the end of
the list:

.. code:: python

    print(elements[-1])
    print(elements[-2])


.. container:: output

    C
    B


List elements can be changed by assigning a new element at a given
index:

.. code:: python

    elements[0] = 'new'
    print(elements)


.. container:: output

    ['new', 'He', 'Li', 'Be', 'B', 'C']


``del()`` deletes an element from a list:

.. code:: python

    del(elements[1])
    print(elements)


.. container:: output

    ['new', 'Li', 'Be', 'B', 'C']


Lists can be nested, that is a list can have other lists as its
elements:

.. code:: python

    list1 = [1, 2, 3]
    list2 = [4, 5]
    list_of_lists = [list1, list2]
    print(list_of_lists)


.. container:: output

    [[1, 2, 3], [4, 5]]


Using iterated indexes we can access elements of nested lists:

.. code:: python

    print(list_of_lists[1][0])


.. container:: output

    4


List slicing
~~~~~~~~~~~~

List slicing produces a new list, consisting of some elements of the
original list. Here are some examples.

Start at position 2, end at position 4:

.. code:: python

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print(letters[2:5])


.. container:: output

    ['c', 'd', 'e']


Start at the beginning, end at position 3:

.. code:: python

    print(letters[:4])


.. container:: output

    ['a', 'b', 'c', 'd']


Start at position 3, end at the end of the list:

.. code:: python

    print(letters[3:])


.. container:: output

    ['d', 'e', 'f', 'g', 'h']


Optionally slicing can be used with three arguments. The third argument
specifies by what value the index should be increased.

List slicing: start from position 1, end at position 5, increasing index
by 2:

.. code:: python

    print(letters[1:6:2])


.. container:: output

    ['b', 'd', 'f']


Select every third element of the list:

.. code:: python

    print(letters[::3])


.. container:: output

    ['a', 'd', 'g']


One way to revert a list:

.. code:: python

    print(letters[::-1])


.. container:: output

    ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']


Strings vs Lists
----------------

Slicing and indexing operations can be also applied to strings:

.. code:: python

    s = 'New York City'
    print(s[0])


.. container:: output

    N


.. code:: python

    print(s[4:8])


.. container:: output

    York


.. code:: python

    print(s[::2])


.. container:: output

    NwYr iy


A difference between strings and lists is that it is not possible to append
a character to a string or change a character using its index:

.. code:: python

    s[0] = 'A'


.. container:: output

    TypeError                                 Traceback (most recent call last)
    <ipython-input-19-418888caed05> in <module>()
    ----> 1 s[0] = 'A'
    TypeError: 'str' object does not support item assignment


"for" loops
-----------

Python ``for`` loops provide a way to iterate (loop) over the items in a
list, string, or any other iterable object, executing a block of code on
each pass through the loop. The syntax is:


.. parsed-literal::

	for <iteration variable(s)> in <iterable>:
            <code to execute inside loop>

**Note:**

-  The ``for`` statement must be followed by a colon ``:``.
-  The block of code to execute each time through the loop starts on the
   next line, and must be indented.
-  The block of code of the loop is finished by de-indenting back to the
   previous level.

Below are some examples of ``for`` loops.

Iteration over elements of a list. The iteration variable ``i`` gets
bound to each item of the lists in turn:

.. code:: python

    for i in [2, 4, 6]:
        print(10*i)


.. container:: output

    20
    40
    60


Iteration over characters in a string. The iteration variable ``letter``
gets bound to each string character in turn:

.. code:: python

    for letter in 'hello':
        if letter != 'l':
            print(letter)


.. container:: output

    h
    e
    o


Printing vowels in word:

.. code:: python

    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in 'Buffalo':
        if letter in vowels:
            print(letter)


.. container:: output

    u
    a
    o


Computing the sum of squares of numbers from 0 to 4:

.. code:: python

    total = 0
    mylist = [0,1,2,3,4]
    for x in mylist:
        total += x**2
    print(total)


.. container:: output

    30


``break`` can be used to terminate a loop early:

.. code:: python

    for letter in 'Buffalo':
        if letter == 'a':
            break
        else:
            print(letter)


.. container:: output

    B
    u
    f
    f


Range
-----

As the examples above illustrate in many situations we may need
to iterate a ``for`` loop over a sequence of consecutive integers. It
would be inconvenient having to manually type a list of integers to code
such iteration. Instead we can use the ``range`` function that generates
integers in a given range.

``range(n)`` generates consecutive integers, starting at 0 and ending at
n-1:

.. code:: python

    for x in range(5):
        print(x)


.. container:: output

    0
    1
    2
    3
    4


``range(m,n)`` creates a list of consecutive integers, from m to n-1:

.. code:: python

    for x in range(5,10):
        print(x)


.. container:: output

    5
    6
    7
    8
    9


The third argument to ``range()`` specifies the increment from one
integer to the next:

.. code:: python

    odds = range(1,10,2)
    for x in odds:
        print(x)


.. container:: output

    1
    3
    5
    7
    9


``range()`` can also count backwards using a negative increment:

.. code:: python

    countdown = range(5,0,-1)
    for x in countdown:
        print(x)


.. container:: output

    5
    4
    3
    2
    1


**Note.** In Python 3 the ``range`` function does not produce a list of
integers, but instead generates integers one by one as needed. This
saves computer memory and can speed up programs. In cases when we want
to get an actual list of integers we can do it by using the ``list``
function:

.. code:: python

    odds = range(1,10,2)
    odds_list = list(odds)
    print(odds_list)


.. container:: output

    [1, 3, 5, 7, 9]
