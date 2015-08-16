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
Always set ``asset_path`` and ``template_path`` right after instantiating GUI. ``asset_path`` is where all the static files including images, stylesheets and javascripts are stored. The static files will have to be present on the user computer and using htmlPy asset tags, their links can be generated dynamically.

Set ``BASE_DIR`` variable as the absolute path to the directory of the driver file and set ``asset_path`` and ``template_path`` with respect to ``BASE_DIR``. Refer to the previous code section on this page for example.

The static files can be included in HTML templates as follows.

.. code-block:: html

    <script src="$asset$ js/jquery.min.js $endasset$"></script>
    <link rel="stylesheet" href="$asset$ css/bootstrap.min.css $endasset$">


htmlPy uses `Jinja2 <http://jinja.pocoo.org/>`_ for templating which is inspired by Django's templating system but extends with powerful tools. Jinja2 requires a base directory to be set. This can be done by setting the ``template_path`` as displayed above.

You can use your own templating system as ``htmlPy.AppWindow`` as a method ``set_html``.
