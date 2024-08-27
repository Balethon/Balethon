from .delete_sticker_from_set import DeleteStickerFromSet
from .get_sticker_set import GetStickerSet
from .create_new_sticker_set import CreateNewStickerSet
from .upload_sticker_file import UploadStickerFile
from .add_sticker_to_set import AddStickerToSet


class Stickers(GetStickerSet, CreateNewStickerSet, DeleteStickerFromSet, UploadStickerFile, AddStickerToSet):
    pass
