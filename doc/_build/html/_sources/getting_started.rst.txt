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