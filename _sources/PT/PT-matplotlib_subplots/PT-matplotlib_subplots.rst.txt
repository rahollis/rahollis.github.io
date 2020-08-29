
Matplotlib subplots and axes objects
====================================


Subplots
--------



The ``subplot`` function of the ``matplotlib`` module is a tool for
plotting several graphs on a single figure. By calling
``subplot(n,m,k)`` we subdidive the figure into ``n`` rows and ``m``
columns and specify that plotting should be done on the subplot number
``k``. Subplots are numbered row by row, from left to right.

.. code:: python

    import matplotlib.pyplot as plt
    import numpy as np
    from math import pi

.. code:: python

    plt.figure(figsize=(8,4))       # set dimensions of the figure
    x = np.linspace(0,2*pi, 100)
    for i in range(1,7):
        plt.subplot(2,3, i)         # create subplots on a grid with 2 rows and 3 columns
        plt.xticks([])              # set no ticks on x-axis
        plt.yticks([])              # set no ticks on y-axis
        plt.plot(np.sin(x), np.cos(i*x))
        plt.title('subplot' + '(2,3,' + str(i) + ')')

    plt.show()


.. image:: PT-matplotlib_subplots-1.svg
   :width: 600 px
   :align: center


**Note.** If the numbers ``i``, ``j``, ``k`` are all smaller than 10 we
can specify a subplot by typing ``subplot(ijk)`` instead of
``subplot(i,j,k)``:

.. code:: python

    plt.figure(figsize=(8,4))
    x = np.linspace(0,2*pi, 100)

    plt.subplot(231)
    plt.xticks([])
    plt.yticks([])
    plt.plot(np.sin(x), np.cos(x))
    plt.title('subplot(231)')

    plt.subplot(233)
    plt.xticks([])
    plt.yticks([])
    plt.plot(np.sin(x), np.cos(3*x))
    plt.title('subplot(233)')

    plt.subplot(235)
    plt.xticks([])
    plt.yticks([])
    plt.plot(np.sin(x), np.cos(5*x))
    plt.title('subplot(235)')

    plt.show()



.. image:: PT-matplotlib_subplots-2.svg
   :width: 600 px
   :align: center



It is possible to combine subplots of different sizes as long as they do
not overlap:

.. code:: python

    plt.figure(figsize=(8,4))
    x = np.linspace(0,2*pi, 200)

    for i in [1, 2, 4, 5]:
        plt.subplot(2,3,i)    # create some subplots on a grid with 2 rows and 3 columns
        plt.xticks([])
        plt.yticks([])
        plt.plot(np.sin(3*x), np.cos(i*x))
        plt.title('subplot(2,3,' + str(i) + ')')


    plt.subplot(1,3,3)       # create a subplot on a grid with 1 row and 3 columns
    plt.xticks([])
    plt.yticks([])
    plt.plot(np.sin(10*x), x)
    plt.title('subplot(1,3,3)')

    plt.show()



.. image:: PT-matplotlib_subplots-3.svg
   :width: 600 px
   :align: center


Spacing between subplots can be controlled using the ``subplots_adjust``
function:

.. code:: python

    plt.figure(figsize=(8,4))
    x = np.linspace(0,2*pi, 200)

    plt.subplots_adjust(wspace=0.05, # wspace controls the width of space between subplots
                        hspace=0.5)  # hspace controls the hight of space between subplots

    for i in [1, 2, 4, 5]:
        plt.subplot(2,3,i)
        plt.xticks([])
        plt.yticks([])
        plt.plot(np.sin(3*x), np.cos(i*x))
        plt.title('subplot(2,3,' + str(i) + ')')

    plt.subplot(1,3,3)
    plt.xticks([])
    plt.yticks([])
    plt.plot(np.sin(10*x), x)
    plt.title('subplot(1,3,3)')

    plt.show()

.. image:: PT-matplotlib_subplots-4.svg
   :width: 600 px
   :align: center


Axes objects
------------

The ``subplot`` function returns an ``axes`` object. We can use it to
specify which subplot is active at any time:


.. code:: python

    plt.figure(figsize=(8,4))
    x = np.linspace(0,2*pi, 200)

    plt.subplots_adjust(hspace=0.4)

    ax1 = plt.subplot(2,1,1) # subplot(2,1,1) is active, plotting will be done there
    plt.xlim(0, 2*pi)
    plt.plot(x, np.sin(2*x))
    plt.title('subplot(2,1,1)')

    ax2 = plt.subplot(2,1,2) # subplot(2,1,2) is now active
    plt.xlim(0, 2*pi)
    plt.plot(x, np.sin(10*x), 'g')
    plt.title('subplot(2,1,2)')

    plt.axes(ax1) # we activate subplot(2,1,1) to do more plotting on this subplot
    plt.plot(x, np.cos(2*x), 'r--')


    plt.show()


.. image:: PT-matplotlib_subplots-5.svg
   :width: 600 px
   :align: center


The ``axes`` function that we used above to select an existing axes
object can be also used to create such objects. This is a useful
alternative to the ``subplot`` function since it gives more flexibility
in setting the layout of the figure: while the ``subplot`` function
creates an evenly spaced grid, using the ``axes`` function we can place
graphs within the figure any way we want:

.. code:: python

    plt.figure(figsize=(8,4))

    # we use the axes function to create an axes object
    # coordinates of the object within the picture are numbers between 0 and 1.
    # The point (0,0) is the lower left corner of the figure, the point (1,1)
    # is the upper right corner
    ax1 = plt.axes([
            0.1,      # x-coordinate of the lower left corner of the axes object
            0.1,      # y-coordinate of the lower left corner of the axes object
            0.5,      # width of the object
            0.4       # height of the object
        ])

    #here we create another axes object
    ax2 = plt.axes([0.5, 0.2, 0.4, 0.6])

    x = np.linspace(0,2*pi, 300)

    plt.axes(ax1) # select ax1 to do some plotting there
    plt.title('This is ax1')
    plt.xlim(0, 2*pi)
    plt.plot(x, np.cos(20*x), 'g')
    plt.xticks([])
    plt.yticks([])

    plt.axes(ax2) # switch to ax2
    plt.title('This is ax2')
    plt.xlim(0, 2*pi)
    plt.plot(x, np.sin(2*x))
    plt.plot(x, np.cos(2*x), 'r--')
    plt.xticks([])
    plt.yticks([])

    plt.show()

.. image:: PT-matplotlib_subplots-6.svg
   :width: 600 px
   :align: center
