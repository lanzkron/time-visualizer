import time
from functools import wraps


def track_time(output):
    """ Decorates a function to output how long it took for visualization with visualize.html
    :param output: callable object that will output the time taken (usually logger function or `print`)
    Usage:
        @track_time(lambda x: logger.debug(x))
        def some_func(some, parameters):
            ...
    """
    def decorator(func):
        @wraps(func)
        def impl(*args, **kwargs):
            start = time.perf_counter()
            try:
                return func(*args, **kwargs)
            finally:
                end = time.perf_counter()
                output(f"exiting function {func.__name__} - "
                       f"execution time: {end-start:.4f} seconds ({start}:{end})")

        return impl
    return decorator
