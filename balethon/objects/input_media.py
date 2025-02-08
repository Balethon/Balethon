from typing import Union, BinaryIO
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
                media = open(media, "rb")
        except TypeError:
            pass
        self.media: Union[str, bytes, BinaryIO] = media
        self.caption: str = caption

    @property
    def is_json_serializable(self):
        return isinstance(self.media, str)


def resolve_media(media):
    if isinstance(media, InputMedia):
        return media

    return InputMedia(media=media).media
