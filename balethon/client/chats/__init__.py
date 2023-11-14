from .ban_chat_member import BanChatMember
from .get_chat import GetChat
from .get_chat_administrators import GetChatAdministrators
from .get_chat_members_count import GetChatMembersCount
from .get_chat_member import GetChatMember
from .invite_user import InviteUser
from .leave_chat import LeaveChat
from .promote_chat_member import PromoteChatMember


class Chats(
    BanChatMember,
    GetChat,
    GetChatAdministrators,
    GetChatMembersCount,
    GetChatMember,
    InviteUser,
    LeaveChat,
    PromoteChatMember
):
    pass
