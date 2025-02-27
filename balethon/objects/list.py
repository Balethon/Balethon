from . import Object, unwrap


class List(list, Object):
    @classmethod
    def wrap(cls, raw_object):
        return cls(raw_object)

    def bind(self, client):
        self.client = client
        for element in self:
            if isinstance(element, Object):
                element.bind(client)

    def unwrap(self):
        return unwrap(self)

    def __repr__(self):
        elements = "\n".join(f"{repr(element)}," for element in self)
        if elements:
            elements = "\n".join(" "*4 + line for line in elements.splitlines())
            elements = f"\n{elements}\n"
        return f"[{elements}]"
