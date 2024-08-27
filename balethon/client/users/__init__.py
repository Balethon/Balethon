from .get_me import GetMe
from .invite_user import InviteUser


class Users(GetMe, InviteUser):
    pass
