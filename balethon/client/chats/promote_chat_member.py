from typing import Union

import balethon


class PromoteChatMember:

    async def promote_chat_member(
            self: "balethon.Client",
            chat_id: Union[int, str],
            user_id: Union[int, str],
            can_edit_messages: bool = None,
            can_delete_messages: bool = None,
            can_manage_video_chats: bool = None,
            can_restrict_members: bool = None,
            can_promote_members: bool = None,
            can_change_info: bool = None,
            can_invite_users: bool = None,
            can_pin_messages: bool = None,
            can_send_messages: bool = None,
            can_send_media_messages: bool = None,
            can_send_media: bool = None,
            can_send_gif_stickers: bool = None,
            can_reply_to_story: bool = None,
            can_forward_message_from: bool = None,
            can_send_gift_packet: bool = None,
            can_start_call: bool = None,
            can_send_link_message: bool = None,
            can_send_forwarded_message: bool = None,
            can_kick_user: bool = None,
            can_send_message: bool = None,
            can_see_members: bool = None,
            can_add_story: bool = None
    ) -> bool:
        chat_id = await self.resolve_peer_id(chat_id)
        user_id = await self.resolve_peer_id(user_id)
        return await self.auto_execute("post", "promoteChatMember", locals())
