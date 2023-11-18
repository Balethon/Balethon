from functools import wraps
from asyncio import get_running_loop, new_event_loop, set_event_loop
from inspect import iscoroutinefunction


def synchronize_function(coroutine_function):

    @wraps(coroutine_function)
    def synchronous(*args, **kwargs):
        try:
            loop = get_running_loop()
        except RuntimeError:
            loop = new_event_loop()
            set_event_loop(loop)
        try:
            return loop.run_until_complete(coroutine_function(*args, **kwargs))
        except RuntimeError:
            coroutine = coroutine_function(*args, **kwargs)
            return coroutine.__await__()

    return synchronous


def synchronize_object(obj, *exceptions):
    for name in dir(obj):
        method = getattr(obj, name)

        if name.startswith("_"):
            continue
        if name in exceptions:
            continue
        if not iscoroutinefunction(method):
            continue

        synchronous_method = synchronize_function(method)
        setattr(obj, name, synchronous_method)
