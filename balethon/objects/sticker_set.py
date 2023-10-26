from typing import List

from . import Object
from balethon import objects


class StickerSet(Object):

    def __init__(
            self,
            name: str = None,
            title: str = None,
            sticker_type: str = None,
            is_animated: bool = None,
            is_video: bool = None,
            contains_masks: bool = None,
            stickers: List["objects.Sticker"] = None,
            thumb: "objects.Photo" = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.name: str = name
        self.title: str = title
        self.sticker_type: str = sticker_type
        self.is_animated: bool = is_animated
        self.is_video: bool = is_video
        self.contains_masks: bool = contains_masks
        self.stickers: List = stickers
        self.thumb: "objects.Photo" = thumb
