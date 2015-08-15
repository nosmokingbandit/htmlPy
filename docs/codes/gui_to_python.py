import htmlPy
import json
from sample_app import app


class ClassName(htmlPy.Bridge):
    # GUI callable functions have to be inside a class.
    # The class should be inherited from htmlPy.Bridge.

    def __init__(self):
        # Initialize the class here, if required.
        return

    @htmlPy.attach()
    def function_name(self):
        # This is the function exposed to GUI events.
        # You can change app HTML from here.
        # Or, you can do pretty much any python from here.
        #
        # NOTE: @htmlPy.attach decorater needs argument and return data-types.
        # Refer to API documentation.
        return

    @htmlPy.attach(str, result=str)
    def form_function_name(self, json_data):
        # @htmlPy.attach(arg1_type, arg2_type, ..., result=return_type)
        # This function can be used for GUI forms.
        #
        form_data = json.loads(json_data)
        return json.dumps(form_data)

    @htmlPy.attach()
    def javascript_function(self):
        # Any function decorated with @htmlPy.attach decorater can be called
        # using javascript in GUI
        return


## You have to register the class instance to the AppWindow instance to be
## callable from GUI
app.register(ClassName())
