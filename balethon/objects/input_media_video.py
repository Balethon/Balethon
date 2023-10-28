from typing import Union
from io import BufferedReader

from . import InputMedia


class InputMediaVideo(InputMedia):

    def __init__(
            self,
            media: Union[str, bytes, BufferedReader] = None,
            caption: str = None,
            **kwargs
    ):
        super().__init__("video", media, caption, **kwargs)
