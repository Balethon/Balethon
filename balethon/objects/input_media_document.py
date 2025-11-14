from typing import Union, BinaryIO

from . import InputMedia


class InputMediaDocument(InputMedia):

    def __init__(
        self,
        media: Union[str, bytes, BinaryIO] = None,
        thumbnail: Union[str, bytes, BinaryIO]=None,
        caption: str = None,
        **kwargs
    ):
        super().__init__(
            type="docuemnt",
            media=media,
            thumbnail=thumbnail,
            caption=caption,
            **kwargs
        )
