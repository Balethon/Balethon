from . import Object
import balethon


class File(Object):

    @classmethod
    def wrap(cls, raw_object):
        if raw_object.get("file_id"):
            raw_object["id"] = raw_object.pop("file_id")
        if raw_object.get("file_size"):
            raw_object["size"] = raw_object.pop("file_size")
        if raw_object.get("file_path"):
            raw_object["path"] = raw_object.pop("file_path")
        return super().wrap(raw_object)

    def __init__(
            self,
            client: "balethon.Client" = None,
            id: str = None,
            size: int = None,
            path: str = None,
            **kwargs
    ):
        super().__init__(client, **kwargs)
        self.id: str = id
        self.size: int = size
        self.path: str = path
