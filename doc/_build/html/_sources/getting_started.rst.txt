Getting started with idf-plotter
================================

The ``idf-plotter`` project creates an overview of an EnergyPlus IDF file. If
you have EnergyPlus installed on your system, you will have a bunch of these
files kicking around. Check the `ExampleFiles` folder of your EnergyPlus
installation.


Prerequisites
-------------

You will need to install ``ply``:

.. sourcecode:: bat

   $ pip install ply


You will also nead to have GraphViz_ installed and accessible from your 
``%PATH%``.


.. _GraphViz: http://www.graphviz.org/

Running idf-plotter the easy way
--------------------------------


The easiest way to use the ``idf-plotter`` is with the ``findreferences.bat``
file.

Example:

.. sourcecode:: bat
   
   C:\idf-plotter\findreferences.bat C:\EnergyPlusV8-4-0\ExampleFiles\gasAbsorptionChillerHeater.idf

This will create a files called :download:`output.dot.pdf <output.dot.pdf>`
in the current directory.


Running idf-plotter the hard way
--------------------------------

Check the contents of the ``findreferences.bat`` file:

.. literalinclude:: ../findreferences.bat

As you can see, ``findreferences.bat`` calls ``findreferences.py``. Twice. Once without the ``--names`` argument and
once with. These two calls work slightly different:

- if ``--names`` is present, this references a text file containing the list of names to output. Each line of this
  text file represents an object in the IDF file on a line. The objects are expected to be of the form ``CLASS;ID``
  and the output contains only the ``ID`` portion. You can pass an edited version of the names text file, e.g. to filter
  out unwanted objects. The output of calling ``findreferences.py`` with a ``--names`` argument is the DOT graph.

- if ``-names`` is not present, the output is a names text file that can be used in a subsequent call, see above.
