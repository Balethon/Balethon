class Object:

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, item):
        return getattr(self, item)

    def fix_types(self):
        types = type(self).__annotations__
        for key, value in self.__dict__.items():
            if not types.get(key):
                continue
            if isinstance(value, types[key]):
                continue
            if issubclass(types[key], Object) and isinstance(value, dict):
                self[key] = types[key](**value)
            else:
                self[key] = types[key](value)

    def add_defaults(self):
        for key, value in type(self).__annotations__.items():
            if self.__dict__.get(key):
                continue
            self[key] = None

    def __init__(self, *args, **kwargs):
        self.client = None
        for key, value in kwargs.items():
            self[key] = value
        self.fix_types()
        self.add_defaults()

    def bind(self, client):
        self.client = client
        for value in self.__dict__.values():
            if isinstance(value, Object):
                value.bind(client)

    def __repr__(self):
        return str(self.__dict__)
