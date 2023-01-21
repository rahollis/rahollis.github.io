
Functions
=========

Functions basics
----------------

Functions are a basic tool for organizing programs in Python (and in
other programming languages). A function is essentially a block a code
with a name. It we want to use a function then we can simply call it by
its name. The syntax for defining functions is as follows:

.. parsed-literal::

    def <function name>(<function arguments>):
   	<code>

**Example.** The following function multiplies two numbers and prints
the result:

.. code:: python

    def multiply(a, b):
        c = a*b
        print('{0}*{1} = {2}'.format(a, b, c))

.. code:: python

    multiply(3,2)


.. container:: output

    3*2 = 6


.. code:: python

    multiply(12,13)


.. container:: output

    12*13 = 156


A function can return one or more values using the ``return`` statement.
This statement is optional since in general a function does not need to
return anything. However, a function will stop executing as soon as the
``return`` statement is encountered.

**Example.** The following function takes as its argument a string, and returns
the first vowel in the string:

.. code:: python

    def first_vowel(s):
        for letter in s:
            if letter in ['a', 'e', 'i', 'o', 'u']:
                return letter
        return 0

.. code:: python

    first_vowel('scratches')




.. container:: output

    'a'



.. code:: python

    first_vowel('hmm')




.. container:: output

    0



Positional and keyword arguments
--------------------------------

There are two ways to pass arguments to a function: by position and by
keyword. For example, here is a function which computes the volume of a
cylinder with a given height and radius:

.. code:: python

    def cyl_vol(height, radius):
        pi = 3.1415926
        vol = pi*height*radius**2
        return vol

If we call this function by ``cyl_vol(3,5)`` it will pass the arguments
by position: 3 becomes the value of the first argument ``height``, and 5
the value of the second argument ``radius``:

.. code:: python

    cyl_vol(3,5)




.. container:: output

    235.61944500000004



Alternatively, we can explicitly use the keywords to set values of the
arguments:

.. code:: python

    cyl_vol(height = 3, radius = 5)




.. container:: output

    235.61944500000004



While this takes more typing the advantage is that the code is more
readable. In addition, arguments specified by keywords can be given in
any order, so we don't need to remember their positions:

.. code:: python

    cyl_vol(radius = 5, height = 3)




.. container:: output

    235.61944500000004



It is also possible to specify some arguments of a function by position
and some by keyword.

**Example.** The following function coverts temperatures between
Celsius, Fahrenheit, and Kelvin scales. It takes three arguments: ``t``
is the temperature to be converted, ``in_temp`` specifies the scale from
which we are converting, and ``out_temp`` sets the scale we are
converting to:

.. code:: python

    def temp_convert(t, in_temp, out_temp):
        if in_temp == 'C' and out_temp == 'F':
            return (9.0/5.0)*t + 32
        if in_temp == 'C' and out_temp == 'K':
            return t + 273.15
        if in_temp == 'F' and out_temp == 'C':
            return (5.0/9.0)*(t-32)
        if in_temp == 'F' and out_temp == 'K':
            return (5.0/9.0)*(t+459.67)
        if in_temp == 'K' and out_temp == 'C':
            return t - 273.15
        if in_temp == 'K' and out_temp == 'F':
            return (9.0/5.0)*t - 459.67

It is convenient to specify the first argument of this function by
position, and the remaining ones by keywords. In this way we don't need
to remember which position is the input and which is the output scale:

.. code:: python

    temp_convert(47, in_temp = 'C', out_temp = 'K')




.. container:: output

    320.15



.. code:: python

    temp_convert(12, out_temp = 'F', in_temp = 'C')




.. container:: output

    53.6



Default values
--------------

In the definition of a function we can give default values of some
function arguments. These arguments can be then ommitted in function
calls since in such case the default values will be used.

**Example.** Here we modify the function ``first_vowel`` defined above
so that for a given integer n it returns the n-th vowel in a string :

.. code:: python

    def nth_vowel(s, n=1):
        count = 0
        for letter in s:
            if letter in ['a', 'e', 'i', 'o', 'u']:
                count += 1
                if count == n:
                    return letter
        return 0

In the definition of this function the argument ``n`` is given the
default value 1, so this will be the value used if we don't specify a
value for ``n``:

.. code:: python

    nth_vowel('profitable')




.. container:: output

    'o'



On the other hand, if we specify the value of ``n`` this value will be
used instead:

.. code:: python

    nth_vowel('profitable', 3)




.. container:: output

    'a'


**Note.** In the definition of a function arguments with default values
must be listed after arguments without defaults.



Why use functions
-----------------

Here are some reasons why functions are useful:

-  **Reusability.** If some code will be used more than once in a
   program it is better to write is as a function rather than copy and
   paste the code several times.

-  **Code readibility.** It is usually easier to understand what a
   program does if it is split into short functions.

-  **Debugging.** Since each function can be tested separately it is
   easier to fix problems in a program if it is organized into
   functions.
