from functools import wraps

from .app import server, app


def get_url(path):
    """Expands an internal URL to include prefix the app is mounted at"""
    return f"{app.config.routes_pathname_prefix}{path}"


def component(func):
    """Decorator to help vanilla functions as pseudo Dash Components"""
    @wraps(func)
    def function_wrapper(children=None, **kwargs):
        # remove className and style args from input kwargs so the component
        # function does not have to worry about clobbering them.
        className = kwargs.pop('className', None)
        style = kwargs.pop('className', None)
        
        # call the component function and get the result
        result = func(children=children, **kwargs)

        # now restore the initial classes and styles by adding them
        # to any values the component introduced

        if className is not None:
            if hasattr(result, 'className'):
                result.className = f'{className} {result.className}'
            else:
                result.className = className

        if style is not None:
            if hasattr(result, 'style'):
                result.style = style.update(result.style)
            else:
                result.style = style                

        return result
    return function_wrapper
