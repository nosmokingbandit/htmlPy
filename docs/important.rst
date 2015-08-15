Important instructions for application development with htmlPy
==============================================================

Use a driver file
~~~~~~~~~~~~~~~~~

Keep your application modularized. Use a separate file for initialization,
configuration and execution of htmlPy GUI. Do not include any back-end
functionalities in this file. The driver file structure should be

1. Initial configurations
2. htmlPy GUI initialization
3. htmlPy GUI configuration
4. Binding of back-end functionalities with GUI
    a. Import back-end functionalities
    b. Bind imported functionalities
5. Instructions for running front-end in ``if __name__ == "__main__":`` conditional. **Always keep the GUI starter code in the ``if __name__ == "__main__":`` conditional**. The GUI has to be started only when the driver file is running, not when it is being imported

Here's a sample driver file

.. literalinclude:: codes/driver.py



Set ``asset_path`` and ``template_path``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
asasd
