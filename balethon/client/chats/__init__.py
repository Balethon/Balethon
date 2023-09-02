from .get_chat import GetChat
from .get_chat_administrators import GetChatAdministrators
from .get_chat_members_count import GetChatMembersCount
from .get_chat_member import GetChatMember


class Chats(GetChat, GetChatAdministrators, GetChatMembersCount, GetChatMember):
    pass
