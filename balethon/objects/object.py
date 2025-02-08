from typing import get_type_hints, get_args, get_origin, Union, List, Optional
from copy import copy
from json import dumps

import balethon


class Object:
    attribute_names = []

    @classmethod
    def expected_types(cls):
        return get_type_hints(cls.__init__)

    @classmethod
    def validate_types(cls, raw_object):
        expected_types = cls.expected_types()
        for key, value in raw_object.items():
            if not expected_types.get(key):
                continue
            if value is None:
                continue
            expected_type = expected_types[key]
            if isinstance(expected_type, (type(Union), type(Union[str, int]))) and get_origin(expected_type) in (Union, None):
                expected_type = get_args(expected_type)[0]
            if isinstance(expected_type, (type(List), type(List[str]))) and get_origin(expected_type) == list:
                if isinstance(value, list):
                    raw_object[key] = wrap(expected_type, value)
                continue
            if not issubclass(expected_type, Object):
                continue
            if isinstance(value, expected_type):
                continue
            raw_object[key] = expected_type.wrap(value)
        return raw_object

    @classmethod
    def wrap(cls, raw_object):
        for attribute_name, key_name in cls.attribute_names:
            if raw_object.get(key_name):
                raw_object[attribute_name] = raw_object.pop(key_name)
        raw_object = cls.validate_types(raw_object)
        return cls(**raw_object)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, item):
        return getattr(self, item)

    def bind(self, client):
        self.client = client
        for value in self.__dict__.values():
            if isinstance(value, Object):
                value.bind(client)

    def __init__(
            self,
            **kwargs
    ):
        self.client: Optional["balethon.Client"] = None
        for key, value in kwargs.items():
            self[key] = value

    def unwrap(self):
        result = copy(self)
        del result.client
        for key, value in result.__dict__.copy().items():
            if isinstance(value, list):
                result[key] = unwrap(value)
            if isinstance(value, Object):
                result[key] = value.unwrap()
            if value is None:
                delattr(result, key)
        for attribute_name, key_name in result.attribute_names:
            if result.__dict__.get(key_name):
                result[attribute_name] = result.__dict__.pop(key_name)
        return result.__dict__

    def to_json(self):
        return dumps(self.unwrap(), ensure_ascii=False, indent=4)

    def __repr__(self):
        attributes = {}
        for key, value in self.__dict__.items():
            if key == "client":
                continue
            if value is None:
                continue
            attributes[key] = value
        attributes = [f"{key}={repr(value)}," for key, value in attributes.items()]
        attributes = "\n".join(attributes)
        if attributes:
            attributes = "\n".join(" "*4 + line for line in attributes.splitlines())
            attributes = f"\n{attributes}\n"
        return f"{type(self).__name__}({attributes})"


def wrap(expected_type, raw_object):
    if isinstance(expected_type, (type(List), type(List[str]))) and get_origin(expected_type) == list:
        if isinstance(raw_object, list):
            expected_type = get_args(expected_type)[0]
            raw_object = copy(raw_object)
            for i, element in enumerate(raw_object):
                if element is None:
                    continue
                if isinstance(expected_type, (type(List), type(List[str]))) and get_origin(expected_type) == list:
                    if isinstance(element, list):
                        raw_object[i] = wrap(expected_type, element)
                    continue
                if not issubclass(expected_type, Object):
                    continue
                if isinstance(element, expected_type):
                    continue
                raw_object[i] = expected_type.wrap(element)
            from .list import List as BalethonList
            return BalethonList(raw_object)

    if isinstance(expected_type, Object):
        return expected_type.wrap(raw_object)

    return raw_object


def unwrap(wrapped_object):
    if isinstance(wrapped_object, list):
        wrapped_object = copy(wrapped_object)
        for i, element in enumerate(wrapped_object):
            wrapped_object[i] = unwrap(element)
        return list(wrapped_object)

    if isinstance(wrapped_object, Object):
        return wrapped_object.unwrap()

    return wrapped_object
