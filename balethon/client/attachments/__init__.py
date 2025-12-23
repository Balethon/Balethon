from .send_photo import SendPhoto
from .send_animation import SendAnimation
from .send_audio import SendAudio
from .send_document import SendDocument
from .send_sticker import SendSticker
from .send_video import SendVideo
from .send_voice import SendVoice
from .send_location import SendLocation
from .send_contact import SendContact
from .send_media_group import SendMediaGroup
from .get_file import GetFile
from .upload_file import UploadFile


class Attachments(
    SendPhoto,
    SendAnimation,
    SendAudio,
    SendDocument,
    SendVideo,
    SendVoice,
    SendSticker,
    SendLocation,
    SendContact,
    SendMediaGroup,
    GetFile,
    UploadFile
):
    pass
