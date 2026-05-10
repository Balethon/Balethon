import balethon
try:
    from balethon.proto import requests, structs, responses
except ImportError:
    pass


class GetChatMembers:

    async def get_chat_members(
            self: "balethon.Client",
            chat_id: str,
            limit: int = 200,
            next: bytes = None,
            excepted_permissions: bool = False,
            contacts: bool = False,
            query: str = None
    ) -> "responses.LoadMembers":
        peer_id, peer_type = map(int, chat_id.split("|"))
        return await self.invoke(
            service_name="bale.groups.v1.Groups",
            method="LoadMembers",
            payload=requests.LoadMembers(
                group=structs.GroupOutPeer(group_id=peer_id, access_hash=1),
                limit=limit,
                next=next,
                condition=structs.LoadMembersCondition(
                    excepted_permissions=excepted_permissions,
                    contacts=contacts,
                    query=query
                )
            )
        )
