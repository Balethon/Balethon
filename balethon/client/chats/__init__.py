from .ban_chat_member import BanChatMember
from .delete_chat_photo import DeleteChatPhoto
from .get_chat import GetChat
from .get_chat_administrators import GetChatAdministrators
from .get_chat_members_count import GetChatMembersCount
from .get_chat_member import GetChatMember
from .invite_user import InviteUser
from .leave_chat import LeaveChat
from .pin_chat_message import PinChatMessage
from .promote_chat_member import PromoteChatMember
from .send_chat_action import SendChatAction
from .set_chat_description import SetChatDescription
from .set_chat_photo import SetChatPhoto
from .set_chat_title import SetChatTitle
from .unban_chat_member import UnbanChatMember
from .unpin_chat_message import UnpinChatMessage


class Chats(
    BanChatMember,
    DeleteChatPhoto,
    GetChat,
    GetChatAdministrators,
    GetChatMembersCount,
    GetChatMember,
    InviteUser,
    LeaveChat,
    PinChatMessage,
    PromoteChatMember,
    SendChatAction,
    SetChatDescription,
    SetChatTitle,
    SetChatPhoto,
    UnbanChatMember,
    UnpinChatMessage
):
    pass
