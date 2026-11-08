from .delete_my_commands import DeleteMyCommands
from .get_my_commands import GetMyCommands
from .set_my_commands import SetMyCommands


class BotCommands(DeleteMyCommands, GetMyCommands, SetMyCommands):
    pass
