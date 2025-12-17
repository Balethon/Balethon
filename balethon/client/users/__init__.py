from .ask_review import AskReview
from .get_me import GetMe
from .invite_user import InviteUser


class Users(AskReview, GetMe, InviteUser):
    pass
