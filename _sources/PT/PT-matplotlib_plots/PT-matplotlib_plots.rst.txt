
Plots with matplotlib
=====================

Basic plotting
--------------

We can create plots with Python using ``matplotlib.pyplot`` module.
First we import the module:

.. code:: python

    import matplotlib.pyplot as plt

Each function in ``matplotlib.pyplot`` can be now accessed by typing
``plt.function_name``.


Here are the main functions we will use. Click on the function
description to see its full documentation:

+--------------+------------------------------------------------+
| function     | usage                                          |
+==============+================================================+
| ``plot``     | `creates a plot`_                              |
+--------------+------------------------------------------------+
| ``title``    | `sets a title of the plot`_                    |
+--------------+------------------------------------------------+
| ``xlabel``   | `sets label of the x-axis`_                    |
+--------------+------------------------------------------------+
| ``ylabel``   | `sets label of the y-axis`_                    |
+--------------+------------------------------------------------+
| ``xlim``     | `set the range of x values displayed`_         |
+--------------+------------------------------------------------+
| ``ylim``     | `set the range of y values displayed`_         |
+--------------+------------------------------------------------+
| ``show``     | `displays the plot`_                           |
+--------------+------------------------------------------------+


.. _creates a plot: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
.. _sets a title of the plot: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.title
.. _sets label of the x-axis: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.xlabel
.. _sets label of the y-axis: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.ylabel
.. _set the range of x values displayed: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.xlim
.. _set the range of y values displayed: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.ylim
.. _displays the plot: http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.show



The syntax of the ``plot`` function is ``plot(xl, yl, options)`` where:

-  ``xl`` is the list of x-coordinates of points we want to plot
-  ``yl`` is the list of y-coordinates
-  other options may specify how we want the plot to look like.

The ``show`` function must be executed to display a plot.

.. code:: python

    xl = range(-10, 11)                  #x-coordinates
    yl = [x**2 for x in xl]              #y-coordinates
    plt.plot(xl, yl)                     #create plot
    plt.ylim(-10, 110)                   #set the range of y-values displayed
    plt.title('My first plot')           #set the plot title
    plt.xlabel('This is the x-axis')     #set the label of the x-axis
    plt.ylabel('This is the y-axis')     #set the label of the y-axis
    plt.show()                           #show plot - not necessary in the inline mode


.. image:: PT-matplotlib-1.svg
   :width: 450 px
   :align: center

Notice that on the plot above the x-axis and the y-axis have different
scales: the distance between 0 and 5 on the x-axis is bigger than the
distance between 0 and 20 on the y-axis. In order to set the same scale
for both axes we can use the ``axis`` function:

.. code:: python

    plt.plot(xl, yl)           #create plot
    plt.axis('equal')          #equalize axes
    plt.ylim(-10, 100)         #set the range of y-values displayed
    plt.show()


.. image:: PT-matplotlib-2.svg
   :width: 450 px
   :align: center


The ``axis`` function has other options that can be used to control
properties of coordinate axes of a plot. See `matplotlib
documentation <http://matplotlib.org/api/pyplot_api.html?highlight=axis#matplotlib.pyplot.axis>`__
for details.

More plotting options
---------------------

By default the ``plot`` function joins the specified points by straight
lines. If, instead, we want to plot individual points as red circles we
can add the ``'ro'`` option (``'r'`` specifies the color, and ``'o'``
the shape of markers):

.. code:: python

    plt.plot(xl, yl, 'ro')
    plt.xlim()
    plt.ylim(-10, 110)
    plt.show()


.. image:: PT-matplotlib-3.svg
   :width: 450 px
   :align: center

Here are same other options for shapes and colors of markers:

+----------+--------------------+---------+-------------+
| shape    | meaning            | color   | meaning     |
+==========+====================+=========+=============+
| ``'-'``  | solid line         | ``'b'`` | blue        |
+----------+--------------------+---------+-------------+
| ``'--'`` | dashed line        | ``'g'`` | green       |
+----------+--------------------+---------+-------------+
| ``'.'``  | point marker       | ``'r'`` | red         |
+----------+--------------------+---------+-------------+
| ``'o'``  | circle marker      | ``'c'`` | cyan        |
+----------+--------------------+---------+-------------+
| ``'s'``  | square marker      | ``'w'`` | white       |
+----------+--------------------+---------+-------------+
| ``'+'``  | plus marker        | ``'m'`` | magenta     |
+----------+--------------------+---------+-------------+
| ``'x'``  | x marker           | ``'y'`` | yellow      |
+----------+--------------------+---------+-------------+
| ``'D'``  | diamond marker     | ``'k'`` | black       |
+----------+--------------------+---------+-------------+

Here are some examples:

.. code:: python

    x_list = range(20)
    y1_list = 20*[1]
    y2_list = 20*[2]
    y3_list = 20*[3]
    y4_list = 20*[4]

    plt.xlim(-1,20)
    plt.ylim(0,5)
    plt.plot(x_list, y1_list, 'b.',)
    plt.plot(x_list, y2_list, 'gx')
    plt.plot(x_list, y3_list, 'm.')
    plt.plot(x_list, y4_list, 'rs')
    plt.title('Shapes and colors')

    plt.show()


.. image:: PT-matplotlib-4.svg
   :width: 450 px
   :align: center

The parameter ``ms`` of the ``plot`` function can be used to set the
size of markers:

.. code:: python

    plt.xlim(-1,20)
    plt.ylim(0,5)

    plt.plot(x_list, y1_list, 'rD', ms=2)
    plt.plot(x_list, y2_list, 'rD', ms=4)
    plt.plot(x_list, y3_list, 'rD', ms=8)
    plt.plot(x_list, y4_list, 'rD', ms=12)
    plt.title('Sizes of markers')

    plt.show()


.. image:: PT-matplotlib-5.svg
   :width: 450 px
   :align: center


The parameter ``alpha`` controls transparency of plots. The value of
``alpha`` can vary between 0 (completely transparent) to 1 (opaque):

.. code:: python

    plt.xlim(-1,20)
    plt.ylim(0,5)

    plt.plot(x_list, y1_list, 'rD', ms=20, alpha= 0.25)
    plt.plot(x_list, y2_list, 'rD', ms=20, alpha= 0.5)
    plt.plot(x_list, y3_list, 'rD', ms=20, alpha= 0.75)
    plt.plot(x_list, y4_list, 'rD', ms=20, alpha= 1.0)
    plt.title('Transparency')

    plt.show()


.. image:: PT-matplotlib-6.svg
   :width: 450 px
   :align: center

Plot legend
-----------

If more than one graph is plotted on a single figure a legend can be
used to label graphs:

.. code:: python

    x_list =  [0.01*x for x in range(-200, 201)]
    y2_list = [x**2 for x in x_list]
    y4_list = [-x**2 for x in x_list]
    y6_list = [-x**3 + x for x in x_list]

    plt.plot(x_list, y2_list, 'b-', label='$y=x^2$')    # label specifies the plot description in the legend
    plt.plot(x_list, y4_list, 'r-', label='$y=-x^2$')   # LaTeX can be used to typeset formulas in matplotlib labels and titles
    plt.plot(x_list, y6_list, 'g-', label='$y=x^3+x$')

    plt.ylim(-1, 1)
    plt.xlim(-3, 3)

    plt.legend(fontsize=13) # creates the legend; fontsize specifies the size of fonts in the legend

    plt.show()



.. image:: PT-matplotlib-7.svg
   :width: 450 px
   :align: center


**Exercise 1.** Plot the function :math:`y = \sin(6x)` for :math:`0\leq x \leq 6`. The Python function
``sin`` which computes values of sine is a part of the ``math`` module:

.. code:: python

    from math import sin, pi
    sin(pi/2)




.. container:: output

    1.0



Further reading
---------------

Matplotlib is a very large module with a lot of uses. Here are a
couple links that can be helpful for exploring it further:

-  `Full online matplotlib
   refrence <http://matplotlib.org/api/pyplot_summary.html>`__
-  `A tutorial from
   scipy-lectures.org <http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html>`__
