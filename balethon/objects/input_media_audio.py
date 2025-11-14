from typing import Union, BinaryIO

from . import InputMedia


class InputMediaAudio(InputMedia):

    def __init__(
        self,
        media: Union[str, bytes, BinaryIO] = None,
        thumbnail:  Union[str, bytes, BinaryIO] = None,
        caption: str = None,
        duration: int = None,
        title: str = None,
        **kwargs
    ):
        super().__init__(
            type="audio",
            media=media,
            thumbnai=thumbnail,
            caption=caption,
            duration=duration,
            title=title,
            **kwargs
        )
