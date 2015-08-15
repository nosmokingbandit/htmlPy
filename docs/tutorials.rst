Tutorials for common tasks
==========================
Following are some basic instructions for performing most common GUI and
Python tasks with htmlPy.

HTML to Python calls
~~~~~~~~~~~~~~~~~~~~~~~~
An essential aspect of GUI is to attach back-end calls to GUI events.
htmlPy needs the corresponding back-end functions to be selectively exposed
to GUI. The calls from GUI can be done in very HTML way.

The back-end functions that have to be attached to GUI events are
defined as follows

.. literalinclude:: codes/html_to_python.py

After exposing the class methods to GUI, they can be called from HTML as
follows

.. literalinclude:: codes/html_to_python.html

Python to HTML calls
~~~~~~~~~~~~~~~~~~~~

Integration with django
~~~~~~~~~~~~~~~~~~~~~~

Integration with web.py
~~~~~~~~~~~~~~~~~~~~~~~
