from typing import Union
from io import BufferedReader
from os.path import isfile

from . import Object


class InputMedia(Object):

    def __init__(
            self,
            type: str = None,
            media: Union[str, bytes, BufferedReader] = None,
            caption: str = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.type: str = type
        if isfile(media):
            with open(media, "rb") as media_file:
                media = media_file.read()
        self.media: Union[str, bytes, BufferedReader] = media
        self.caption: str = caption
