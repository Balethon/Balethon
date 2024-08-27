from .send_message import SendMessage
from .edit_message_caption import EditMessageCaption
from .edit_message_text import EditMessageText
from .forward_message import ForwardMessage
from .delete_message import DeleteMessage
from .copy_message import CopyMessage


class Messages(SendMessage, EditMessageCaption, EditMessageText, ForwardMessage, DeleteMessage, CopyMessage):
    pass
