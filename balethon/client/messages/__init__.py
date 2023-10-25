from .send_message import SendMessage
from .edit_message_text import EditMessageText
from .forward_message import ForwardMessage
from .delete_message import DeleteMessage
from .send_media_group import SendMediaGroup


class Messages(SendMessage, EditMessageText, ForwardMessage, DeleteMessage, SendMediaGroup):
    pass
