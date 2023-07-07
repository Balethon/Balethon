from json import dumps


class Object:

    def __init__(self):
        pass

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return dumps(self.to_dict(), ensure_ascii=False, indent=4)

    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return self.to_json()

    def __getitem__(self, item):
        return getattr(self, item)
