from .start_phone_auth import StartPhoneAuth
from .validate_code import ValidateCode
from .sign_up import SignUp

class Auth(StartPhoneAuth, ValidateCode, SignUp):
    pass
