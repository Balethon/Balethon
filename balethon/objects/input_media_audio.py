from typing import Union
from io import BufferedReader

from . import InputMedia


class InputMediaAudio(InputMedia):

    def __init__(
            self,
            media: Union[str, bytes, BufferedReader] = None,
            caption: str = None,
            **kwargs
    ):
        super().__init__("audio", media, caption, **kwargs)
