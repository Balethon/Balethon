from typing import Union

import balethon
from balethon.proto import request_pb2, struct_pb2

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
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            return await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="SetMemberPermissions",
                payload=request_pb2.SetMemberPermissions(
                    group=struct_pb2.GroupOutPeer(group_id=peer_id, access_hash=1),
                    user=struct_pb2.UserOutPeer(uid=user_id, access_hash=1),
                    permissions=struct_pb2.Permissions(
                        edit_message=can_edit_messages,
                        delete_message=can_delete_messages,
                        manage_call=can_manage_video_chats,
                        change_info=can_change_info,
                        invite_user=can_invite_users,
                        pin_message=can_pin_messages,
                        send_media=can_send_media,
                        send_gif_stickers=can_send_gif_stickers,
                        reply_to_story=can_reply_to_story,
                        forward_message_from=can_forward_message_from,
                        send_gift_packet=can_send_gift_packet,
                        start_call=can_start_call,
                        send_link_message=can_send_link_message,
                        send_forwarded_message=can_send_forwarded_message,
                        kick_user=can_kick_user,
                        send_message=can_send_message,
                        see_members=can_see_members,
                        add_story=can_add_story
                    )
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        user_id = await self.resolve_peer_id(user_id)
        return await self.auto_execute("promoteChatMember", locals())
