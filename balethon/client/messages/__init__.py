from .answer_callback_query import AnswerCallbackQuery
from .send_message import SendMessage
from .edit_message_caption import EditMessageCaption
from .edit_message_reply_markup import EditMessageReplyMarkup
from .edit_message_text import EditMessageText
from .forward_message import ForwardMessage
from .delete_message import DeleteMessage
from .copy_message import CopyMessage


class Messages(
    AnswerCallbackQuery,
    SendMessage,
    EditMessageCaption,
    EditMessageReplyMarkup,
    EditMessageText,
    ForwardMessage,
    DeleteMessage,
    CopyMessage
):
    pass
