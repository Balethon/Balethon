from .send_photo import SendPhoto
from .send_audio import SendAudio
from .send_document import SendDocument
from .send_video import SendVideo
from .send_voice import SendVoice
from .send_location import SendLocation
from .send_contact import SendContact
from .get_file import GetFile


class Attachments(SendPhoto, SendAudio, SendDocument, SendVideo, SendVoice, SendLocation, SendContact, GetFile):
    pass
