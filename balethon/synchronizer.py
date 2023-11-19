from functools import wraps
from asyncio import get_event_loop, new_event_loop, set_event_loop
from inspect import iscoroutinefunction


def synchronize_method(obj, coroutine_method):

    @wraps(coroutine_method)
    def synchronous(*args, **kwargs):
        if obj.is_asynchronous:
            return coroutine_method(*args, **kwargs)
        try:
            loop = get_event_loop()
        except RuntimeError:
            loop = new_event_loop()
            set_event_loop(loop)
        try:
            return loop.run_until_complete(coroutine_method(*args, **kwargs))
        except RuntimeError:
            coroutine = coroutine_method(*args, **kwargs)
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

        synchronous_method = synchronize_method(obj, method)
        setattr(obj, name, synchronous_method)
