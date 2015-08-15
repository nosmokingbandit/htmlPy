import htmlPy


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
