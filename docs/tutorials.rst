Tutorials for common tasks
==========================
Following are some basic instructions for performing most common GUI and
Python tasks with htmlPy.

GUI to Python calls
~~~~~~~~~~~~~~~~~~~~~~~~
These calls work only for `htmlPy.AppWindow <reference.html#class-htmlpy-appwindow>`_ applications.

An essential aspect of GUI is to attach back-end calls to GUI events.
htmlPy needs the corresponding back-end functions to be selectively exposed
to GUI. The calls from GUI can be done in very HTML way.

The back-end functions that have to be attached to GUI events are
defined as follows

.. literalinclude:: codes/gui_to_python.py

After exposing the class methods to GUI, they can be called from HTML as
follows

.. literalinclude:: codes/gui_to_python.html
   :language: html

Python to GUI calls
~~~~~~~~~~~~~~~~~~~~
These calls work only for `htmlPy.AppWindow <reference.html#class-htmlpy-appwindow>`_ applications.

.. literalinclude:: codes/python_to_gui.py



Integration with django
~~~~~~~~~~~~~~~~~~~~~~~~~
Django can be used for standalone application development using htmlPy. The integration can be done seamlessly. Read `important tips section <important.html>`_ first
