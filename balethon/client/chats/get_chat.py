from typing import Union

import balethon
from ...objects import Chat, ChatId


class GetChat:

    async def get_chat(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> Chat:
        if self.is_userbot():
            from ...proto import requests, structs

            query = None

            if isinstance(chat_id, str):
                # "@username" | "+9*********" | "+09*********" | "+989*********"
                if chat_id.startswith(("@", "+")):
                    query = chat_id[1:]

                # "https://ble.ir/username" | "ble.ir/username"
                elif chat_id.startswith(("https://ble.ir/", "ble.ir/")):
                    query = chat_id.removeprefix("https://").removeprefix("ble.ir/")

            if query:
                response = await self.execute(requests.SearchContacts(request=query))

                if response.user_peers:
                    peer_id = int(response.user_peers[0].uid)
                    peer_type = 1
                else:
                    peer_id = int(response.group_peers[0].group_id)
                    peer_type = 2

            # ChatId(peer_id=1234567890, peer_type=1)
            elif isinstance(chat_id, ChatId):
                peer_id = chat_id.peer_id
                peer_type = chat_id.peer_type

            # (1234567890, 1)
            elif isinstance(chat_id, tuple):
                peer_id, peer_type = chat_id

            # 1234567890
            elif isinstance(chat_id, int):
                peer_id = chat_id
                peer_type = None

            # "1234567890:1" | "1234567890"
            else:
                peer_id, _, peer_type = str(chat_id).partition(":")
                peer_id = int(peer_id)
                peer_type = int(peer_type) if peer_type else None

            try:
                user_request = requests.LoadUsers(user_peers=[structs.UserOutPeer(uid=peer_id, access_hash=1)])
            except ValueError:
                pass
            group_request = requests.GetFullGroup(peer=structs.GroupOutPeer(group_id=peer_id, access_hash=1))

            if peer_type in (1, 4):
                response = await self.execute(user_request)
                return Chat.from_protobuf(response.users[0])

            if peer_type in (2, 3):
                response = await self.execute(group_request)
                return Chat.from_protobuf(response.full_group)

            try:
                response = await self.execute(group_request)
                return Chat.from_protobuf(response.full_group)
            except:
                response = await self.execute(user_request)
                return Chat.from_protobuf(response.users[0])

        else:
            return await self.auto_execute("getChat", locals())
