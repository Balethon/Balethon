from .start_phone_auth import StartPhoneAuth
from .validate_code import ValidateCode


class Auth(StartPhoneAuth, ValidateCode):
    pass
