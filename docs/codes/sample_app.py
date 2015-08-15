import htmlPy
import os

app = htmlPy.AppWindow(title="htmlPy Quickstart", maximized=True)
app.set_template_path(os.path.abspath("."))
app.set_asset_path(os.path.abspath("."))

app.set_template("index.html")
app.start()
