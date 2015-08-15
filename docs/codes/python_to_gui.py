from sample_app import app
# app imported from sample_app file is an instance of htmlPy.AppWindow class.


## Change HTML of the app
app.set_html("<html></html>")

## Change HTML of the app using Jinja2 templates
app.set_template("./index.html", {"template_variable_name": "value"})

## Execute javascript on currently displayed HTML in the app
app.execute_javascript("alert('Hello from back-end')")
