from .add_sticker_to_set import AddStickerToSet
from .create_new_sticker_set import CreateNewStickerSet
from .delete_sticker_from_set import DeleteStickerFromSet
from .get_sticker_set import GetStickerSet


class Stickers(AddStickerToSet, CreateNewStickerSet, DeleteStickerFromSet, GetStickerSet):
    pass
