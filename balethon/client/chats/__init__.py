from .ban_chat_member import BanChatMember
from .delete_chat_photo import DeleteChatPhoto
from .get_chat import GetChat
from .get_chat_administrators import GetChatAdministrators
from .get_chat_history import GetChatHistory
from .get_chat_members_count import GetChatMembersCount
from .get_chat_member import GetChatMember
from .leave_chat import LeaveChat
from .pin_chat_message import PinChatMessage
from .promote_chat_member import PromoteChatMember
from .restrict_chat_member import RestrictChatMember
from .send_chat_action import SendChatAction
from .set_chat_description import SetChatDescription
from .set_chat_photo import SetChatPhoto
from .set_chat_title import SetChatTitle
from .unban_chat_member import UnbanChatMember
from .unpin_all_chat_messages import UnpinAllChatMessages
from .unpin_chat_message import UnpinChatMessage


class Chats(
    BanChatMember,
    DeleteChatPhoto,
    GetChat,
    GetChatAdministrators,
    GetChatHistory,
    GetChatMembersCount,
    GetChatMember,
    LeaveChat,
    PinChatMessage,
    PromoteChatMember,
    RestrictChatMember,
    SendChatAction,
    SetChatDescription,
    SetChatTitle,
    SetChatPhoto,
    UnbanChatMember,
    UnpinAllChatMessages,
    UnpinChatMessage
):
    pass
