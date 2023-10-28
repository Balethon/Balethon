from typing import Union
from typing import BinaryIO

from . import InputMedia


class InputMediaVideo(InputMedia):

    def __init__(
            self,
            media: Union[str, bytes, BinaryIO] = None,
            caption: str = None,
            **kwargs
    ):
        super().__init__("video", media, caption, **kwargs)
