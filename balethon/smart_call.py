import asyncio
from inspect import getfullargspec, signature, iscoroutine, iscoroutinefunction
from concurrent.futures import ThreadPoolExecutor


def remove_unwanted_positional_parameters(function, *args):
    _, varargs, *__ = getfullargspec(function)

    if varargs is not None:
        return args

    positional_arguments = []

    for i, parameter in enumerate(signature(function).parameters.values()):
        if parameter.kind in (parameter.POSITIONAL_OR_KEYWORD, parameter.POSITIONAL_ONLY):
            try:
                positional_arguments.append(args[i])
            except IndexError:
                continue

    return positional_arguments


def remove_unwanted_keyword_parameters(function, **kwargs):
    _, __, varkw, *___ = getfullargspec(function)

    if varkw is not None:
        return kwargs

    keyword_arguments = {}

    for name, parameter in signature(function).parameters.items():
        if parameter.kind in (parameter.POSITIONAL_OR_KEYWORD, parameter.KEYWORD_ONLY):
            try:
                keyword_arguments[name] = kwargs[name]
            except KeyError:
                continue

    return keyword_arguments


def remove_unwanted_parameters(function, *args, **kwargs):
    args = remove_unwanted_positional_parameters(function, *args)
    kwargs = remove_unwanted_keyword_parameters(function, **kwargs)

    return args, kwargs


async def run_asynchronously(function, *args, **kwargs):
    if iscoroutine(function):
        return await function

    elif iscoroutinefunction(function):
        return await function(*args, **kwargs)

    return await asyncio.to_thread(function, *args, **kwargs)


def run_synchronously(function, *args, **kwargs):
    if iscoroutine(function):
        coro = function
    elif iscoroutinefunction(function):
        coro = function(*args, **kwargs)
    else:
        return function(*args, **kwargs)

    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(coro)
    else:
        with ThreadPoolExecutor(1) as pool:
            return pool.submit(asyncio.run, coro).result()
