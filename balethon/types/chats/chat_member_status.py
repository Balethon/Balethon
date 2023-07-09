from ..object import Object
from ..chats.user import User
from ..chats.user_abilities import UserAbilities

class ChatMemeber(Object):
    
    @classmethod
    def from_dict(cls, info_dict: dict):
        info_dict_copy = info_dict.copy()
        info_dict_copy.pop("user")
        
        info_dict = {
            "user" : info_dict["user"],
            "abilities" : info_dict_copy
        }
        
        return cls(**info_dict)
    
    def __init__(
            self,
            user: User,
            abilities: UserAbilities
    ):
        super().__init__()
        self.user = user
        self.abilities = abilities
