from typing import get_type_hints, get_args, Optional
from copy import copy

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
            expected_type = expected_types[key]
            if not isinstance(expected_type, type):
                expected_type = get_args(expected_type)[0]
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

    def unwrap(self):  # TODO: fixing unwrap for all Objects
        result = copy(self)
        del result.client
        for key, value in result.__dict__.copy().items():
            if isinstance(value, Object):
                result[key] = value.unwrap()
            if value is None:
                delattr(result, key)
        for attribute_name, key_name in result.attribute_names:
            if result.__dict__.get(key_name):
                result[attribute_name] = result.__dict__.pop(key_name)
        return result.__dict__

    def __repr__(self):
        name = type(self).__name__
        attributes = ", ".join(f"{key}={repr(value)}" for key, value in self.unwrap().items())
        return f"{name}({attributes})"
