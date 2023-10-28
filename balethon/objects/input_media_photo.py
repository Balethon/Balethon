from typing import Union
from typing import BinaryIO

from . import InputMedia


class InputMediaPhoto(InputMedia):

    def __init__(
            self,
            media: Union[str, bytes, BinaryIO] = None,
            caption: str = None,
            **kwargs
    ):
        super().__init__("photo", media, caption, **kwargs)
