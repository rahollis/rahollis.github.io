
List comprehensions
===================

Basic comprehensions
--------------------

List comprehensions are a tool that in many cases makes it easier to
create a list of elements. For example, if we want to create a list of
squares of the first few positive integers, we can do it using the
``for`` loop as follows:

.. code:: python

    squares = []              # start with an empty list
    for n in range(10):
        squares.append(n**2)  # append n**2

    print(squares)


.. container:: output

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


The same task can be accomplished with less code using list
comprehensions:

.. code:: python

    squares = [n**2 for n in range(10)]   # list comprehension generating a list of squares

    print(squares)


.. container:: output

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


The syntax of list comprehensions is as follows:

.. code:: python

    mylist = [<expression> for <item> in <iterable_object>]

Such code will take one by one items from the iterable object, compute
the value of the expression for each item, and create a list consisting
of all these values. The iterable object can be a list, tuple, string etc.
In the next example we use list comprehensions to create a list from
characters of a string:

.. code:: python

    mylist  = [letter + '!' for letter in 'Buffalo']

    print(mylist)


.. container:: output

    ['B!', 'u!', 'f!', 'f!', 'a!', 'l!', 'o!']


Generalized comprehensions
--------------------------

In a more general form list comprehensions can include an ``if``
statement. For example, in order to create a list of squares of odd
integers we can use the following code:

.. code:: python

    odd_squares = []                  # start with an empty list
    for n in range(10):
        if n%2 == 1:                  # check if n is odd
            odd_squares.append(n**2)  # if n is odd append n**2 to the list

    print(odd_squares)


.. container:: output

    [1, 9, 25, 49, 81]


Using generalized list comprehensions we can get the same list as
follows:

.. code:: python

    odd_squares = [n**2 for n in range(10) if n%2 == 1]

    print(odd_squares)


.. container:: output

    [1, 9, 25, 49, 81]


The syntax of generalized comprehensions is as follows:

.. code:: python

    mylist = [<expression> for <variable> in <iterable_object> if <condition>]

This code will take items from the iterable object, and check for each
item if the condition holds. If it does it will compute the value of the
expression, and produce a list consisting of all these values.

As one more application of this generalized syntax we create a list
consisting of all vowels in a string:

.. code:: python

    vowels = [letter for letter in 'euforia' if letter in 'aeiou']

    print(vowels)


.. container:: output

    ['e', 'u', 'o', 'i', 'a']


Nested comprehensions
---------------------

List comprehensions can be nested to involve more than one variable. For
example, the following code takes values from two different lists of
strings and produces a list of combined strings:

.. code:: python

    greeting_list = ['Hello', 'Hi']
    name_list = ['Alice', 'Bob', 'Caroline']

    mylist = [greeting + ' ' + name + '!' for greeting in greeting_list for name in name_list]

    print(mylist)


.. container:: output

    ['Hello Alice!', 'Hello Bob!', 'Hello Caroline!', 'Hi Alice!', 'Hi Bob!', 'Hi Caroline!']


The above code produces the same output as a nested ``for`` loop:

.. code:: python

    greeting_list = ['Hello', 'Hi']
    name_list = ['Alice', 'Bob', 'Caroline']

    mylist = []
    for greeting in greeting_list:
        for name in name_list:
            mylist.append(greeting + ' ' + name + '!')

    print(mylist)


.. container:: output

    ['Hello Alice!', 'Hello Bob!', 'Hello Caroline!', 'Hi Alice!', 'Hi Bob!', 'Hi Caroline!']


Nested comprehensions can be used with the ``if`` statement. In the next
example we create a list of tuples :math:`(a, b)` such that :math:`b`
divides :math:`a`:

.. code:: python

    divisors = [(a, b) for a in range(1,6) for b in range(1,6) if a%b == 0]

    print(divisors)


.. container:: output

    [(1, 1), (2, 1), (2, 2), (3, 1), (3, 3), (4, 1), (4, 2), (4, 4), (5, 1), (5, 5)]


Equivalent code using nested ``for`` loops looks as follows:

.. code:: python

    divisors = []

    for a in range(1,6):
        for b in range(1,6):
            if a%b == 0:
                divisors.append((a,b))

    print(divisors)


.. container:: output

    [(1, 1), (2, 1), (2, 2), (3, 1), (3, 3), (4, 1), (4, 2), (4, 4), (5, 1), (5, 5)]
