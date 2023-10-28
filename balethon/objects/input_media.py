from typing import Union
from typing import BinaryIO
from os.path import isfile

from . import Object


class InputMedia(Object):

    def __init__(
            self,
            type: str = None,
            media: Union[str, bytes, BinaryIO] = None,
            caption: str = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.type: str = type
        try:
            if isfile(media):
                with open(media, "rb") as media_file:
                    media = media_file.read()
        except TypeError:
            pass
        self.media: Union[str, bytes, BinaryIO] = media
        self.caption: str = caption

    @property
    def is_json_serializable(self):
        return isinstance(self.media, str)
