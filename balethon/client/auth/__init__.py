from .start_phone_auth import StartPhoneAuth
from .validate_code import ValidateCode
from .sign_up import SignUp
from .validate_password import ValidatePassword


class Auth(StartPhoneAuth, ValidateCode, SignUp, ValidatePassword):
    pass
