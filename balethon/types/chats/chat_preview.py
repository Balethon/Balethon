from ..object import Object

class ChatPreview(Object):
    
    @classmethod
    def from_dict(cls, chat_dict: dict):
        if chat_dict["type"] == 'group' and "username" in chat_dict.keys():
            chat_dict["type"] = "channel"
            
        return cls(**chat_dict)
    
    def __init__(
            self,
            id : int,
            type: str,
            client,
            title: str = None
    ):
        super().__init__()
        self.id = id
        self.type  = type
        self.title = title
        self.client = client
        self.members_count = self.client.get_chat_members_count(self.id)
