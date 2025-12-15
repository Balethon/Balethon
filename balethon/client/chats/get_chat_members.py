import balethon
from ...proto.response_pb2 import LoadMembers
from balethon.proto import request_pb2, struct_pb2


class GetChatMembers:

    async def get_chat_members(
            self: "balethon.Client",
            chat_id: str,
            limit: int = 200,
            next: bytes = None,
            excepted_permissions: bool = False,
            contacts: bool = False,
            query: str = None
    ) -> LoadMembers:
        peer_id, peer_type = map(int, chat_id.split("|"))
        return await self.invoke(
            service_name="bale.groups.v1.Groups",
            method="LoadMembers",
            payload=request_pb2.LoadMembers(
                group=struct_pb2.GroupOutPeer(group_id=peer_id, access_hash=1),
                limit=limit,
                next=next,
                condition=struct_pb2.LoadMembersCondition(
                    excepted_permissions=excepted_permissions,
                    contacts=contacts,
                    query=query
                )
            )
        )
