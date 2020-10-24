def memoize(f):
    """Memoize a function."""
    memo = {}
    def wrapper(*args, **kwargs):
        kwargs_tuple = tuple(kwargs.items())
        if (args, kwargs_tuple) in memo:
            return memo[(args, kwargs_tuple)]

        memo[(args, kwargs_tuple)] = f(*args, **kwargs)

        return memo[(args, kwargs_tuple)]

    return wrapper

