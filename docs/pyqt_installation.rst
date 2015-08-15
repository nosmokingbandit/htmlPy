Installing PyQt4
================

Windows (with and without virtualenv)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Download and install SIP_.
2. Download and install PyQt4_.
3. If you want to use htmlPy in virtualenv, copy following files to your virtualenv libraries.

+--------------------------------------------------+-----------------+
| Source                                           | Target          |
+==================================================+=================+
| ``<PYTHON_LIB_PATH>/site-packages/sip*``         | ``<venv>/lib/`` |
+--------------------------------------------------+-----------------+
| ``<PYTHON_LIB_PATH>/site-packages/PyQt4/``       | ``<venv>/lib/`` |
+--------------------------------------------------+-----------------+
| **NOTE**:                                                          |
|                                                                    |
| 1. ``PYTHON_LIB_PATH`` is usually ``C:/Python2x/Lib/``             |
| 2. ``sip*`` means every file and directory with name starting with |
|    ``sip``.                                                        |
+--------------------------------------------------------------------+



Linux (with and without virtualenv)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Download and install SIP_. Ubuntu users can install it with :command:`apt-get install python-sip`
2. Download and install PyQt4_. Ubuntu users can install it with :command:`apt-get install python-qt4`
3. If you want to use htmlPy in virtualenv, copy following files to your virtualenv libraries.

+--------------------------------------------------+-----------------+
| Source                                           | Target          |
+==================================================+=================+
| ``<PYTHON_LIB_PATH>/dist-packages/sip*``         | ``<venv>/lib/`` |
+--------------------------------------------------+-----------------+
| ``<PYTHON_LIB_PATH>/dist-packages/PyQt4/``       | ``<venv>/lib/`` |
+--------------------------------------------------+-----------------+
| **NOTE**:                                                          |
|                                                                    |
| 1. ``PYTHON_LIB_PATH`` is usually ``/usr/lib/python2.x/``          |
| 2. ``sip*`` means every file and directory with name starting with |
|    ``sip``.                                                        |
+--------------------------------------------------------------------+



.. _SIP: http://www.riverbankcomputing.com/software/sip/download
.. _PyQt4: http://www.riverbankcomputing.com/software/pyqt/download
