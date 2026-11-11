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
        chat_id = await self.resolve_chat_id(chat_id)
        return await self.execute(requests.LoadMembers(
            group=structs.GroupOutPeer(group_id=chat_id.peer_id, access_hash=1),
            limit=limit,
            next=next,
            condition=structs.LoadMembersCondition(
                excepted_permissions=excepted_permissions,
                contacts=contacts,
                query=query
            )
        ))
