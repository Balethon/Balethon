from inspect import getfullargspec, signature


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
