from json import dumps


class Object:
    subsets = {}

    def convert_subsets(self):
        for attribute_name, type in self.subsets.items():
            attribute = getattr(self, attribute_name)
            if not isinstance(attribute, dict):
                continue
            converted_attribute = type(attribute)
            setattr(self, attribute_name, converted_attribute)

    def __init__(self, client=None):
        self.client = client
        self.convert_subsets()

    def to_dict(self):
        return self.__dict__.copy()

    def to_json(self):
        obj = self.to_dict()
        del obj["client"]
        return dumps(obj, ensure_ascii=False, indent=4)

    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return self.to_json()

    def __getitem__(self, item):
        return getattr(self, item)
