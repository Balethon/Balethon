from .send_message import SendMessage
from .edit_message_text import EditMessageText
from .delete_message import DeleteMessage


class Messages(SendMessage, EditMessageText, DeleteMessage):
    pass
