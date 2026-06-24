from .start_phone_auth import StartPhoneAuth
from .validate_code import ValidateCode
from .sign_up import SignUp
from .validate_password import ValidatePassword
from .refresh_token import RefreshToken


class Auth(StartPhoneAuth, ValidateCode, SignUp, ValidatePassword, RefreshToken):
    pass
