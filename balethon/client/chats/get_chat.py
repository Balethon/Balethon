from typing import Union

import balethon
from ...objects import Chat
from ...proto import request_pb2, struct_pb2


class GetChat:

    async def get_chat(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> Chat:
        if self.is_userbot():
            peer_id, peer_type = chat_id.split("|")

            if not peer_id.isnumeric():
                # "@username"
                if peer_id.startswith("@"):
                    peer_id = peer_id[1:]

                # "+9*********" | "+09*********" | "+989*********"
                elif peer_id.startswith("+"):
                    peer_id =  peer_id[1:]

                # "https://ble.ir/join/ABCDEEFGHI" | "https://ble.ir/username"
                elif peer_id.startswith("https://ble.ir/"):
                    peer_id = peer_id[15:]

                # "ble.ir/join/ABCDEEFGHI" | "ble.ir/username"
                elif peer_id.startswith("ble.ir/"):
                    peer_id = peer_id[7:]

                response = await self.invoke(
                    service_name="bale.users.v1.Users",
                    method="SearchContacts",
                    payload=request_pb2.SearchContacts(
                        request=peer_id
                    )
                )

                if response.user_peers:
                    result = response.user_peers[0]
                    peer_id = result.uid

                elif response.group_peers:
                    result = response.group_peers[0]
                    peer_id = result.group_id

                else:
                    return

            peer_id, peer_type = map(int, (peer_id, peer_type))

            if peer_type in (1, 4):
                return await self.invoke(
                    service_name="bale.users.v1.Users",
                    method="LoadUsers",
                    payload=request_pb2.LoadUsers(
                        user_peers=[struct_pb2.UserOutPeer(
                                uid=peer_id,
                                access_hash=1
                            )
                        ]
                    )
                )

            if peer_type in (2, 3, 5):
                return await self.invoke(
                    service_name="bale.groups.v1.Groups",
                    method="GetFullGroup",
                    payload=request_pb2.GetFullGroup(
                        peer=struct_pb2.GroupOutPeer(
                            group_id=peer_id,
                            access_hash=1
                        )
                    )
                )

        else:
            return await self.auto_execute("getChat", locals())
