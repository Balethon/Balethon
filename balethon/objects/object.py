from typing import get_type_hints, get_args, Union, List
from copy import copy
from json import dumps

import balethon


class Object:
    attribute_names = []

    @classmethod
    def expected_types(cls):
        return get_type_hints(cls.__init__)

    @staticmethod
    def wrap_list(expected_type, lst):
        lst = copy(lst)
        for i, element in enumerate(lst):
            if isinstance(expected_type, (type(List), type(List[str]))):
                if isinstance(element, list):
                    lst[i] = Object.wrap_list(get_args(expected_type)[0], element)
                continue
            if not issubclass(expected_type, Object):
                continue
            if isinstance(element, expected_type):
                continue
            lst[i] = expected_type.wrap(element)
        return lst

    @classmethod
    def validate_types(cls, raw_object):
        expected_types = cls.expected_types()
        for key, value in raw_object.items():
            if not expected_types.get(key):
                continue
            expected_type = expected_types[key]
            if isinstance(expected_type, type(Union)):
                expected_type = get_args(expected_type)[0]
            if isinstance(expected_type, (type(List), type(List[str]))):
                if isinstance(value, list):
                    raw_object[key] = cls.wrap_list(get_args(expected_type)[0], value)
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

    @staticmethod
    def unwrap_list(lst):
        lst = copy(lst)
        for i, element in enumerate(lst):
            if isinstance(element, list):
                lst[i] = Object.unwrap_list(element)
            elif isinstance(element, Object):
                lst[i] = element.unwrap()
        return lst

    def unwrap(self):
        result = copy(self)
        del result.client
        for key, value in result.__dict__.copy().items():
            if isinstance(value, list):
                result[key] = self.unwrap_list(value)
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
        return self.to_json()
