from typing import get_type_hints

import balethon


class Object:

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
            if not issubclass(expected_type, Object):
                continue
            if isinstance(value, expected_type):
                continue
            raw_object[key] = expected_type.wrap(value)
        return raw_object

    @classmethod
    def wrap(cls, raw_object):
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
            client: "balethon.Client" = None,
            **kwargs
    ):
        self.client: "balethon.Client" = client
        for key, value in kwargs.items():
            self[key] = value
        if client is not None:
            self.bind(client)

    def unwrap(self):
        for key, value in self.__dict__:
            if isinstance(value, Object):
                self[key] = value.unwrap()
        return self.__dict__

    def __repr__(self):
        name = type(self).__name__
        attributes = ", ".join(f"{key}={repr(value)}" for key, value in self.__dict__.items())
        return f"{name}({attributes})"
