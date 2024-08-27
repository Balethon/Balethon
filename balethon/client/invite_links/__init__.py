from .create_chat_invite_link import CreateChatInviteLink
from .export_chat_invite_link import ExportChatInviteLink
from .revoke_chat_invite_link import RevokeChatInviteLink


class InviteLinks(CreateChatInviteLink, ExportChatInviteLink, RevokeChatInviteLink):
    pass
