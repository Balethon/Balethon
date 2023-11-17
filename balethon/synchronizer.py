from functools import wraps
from asyncio import new_event_loop
from inspect import iscoroutinefunction

from .client.attachments import Attachments
from .client.chats import Chats
from .client.messages import Messages
from .client.payments import Payments
from .client.stickers import Stickers
from .client.updates import Updates
from .client.users import Users
import objects


def synchronize_function(coroutine_function):

    @wraps(coroutine_function)
    def synchronous(*args, **kwargs):
        loop = new_event_loop()
        return loop.run_until_complete(coroutine_function(*args, **kwargs))

    return synchronous


def synchronize_object(obj):
    for name in dir(obj):
        method = getattr(obj, name)
        if not name.startswith("__"):
            if iscoroutinefunction(method):
                synchronous_method = synchronize_function(method)
                setattr(obj, name, synchronous_method)


def synchronize_program():
    synchronize_object(Attachments)
    synchronize_object(Chats)
    synchronize_object(Messages)
    synchronize_object(Payments)
    synchronize_object(Stickers)
    synchronize_object(Updates)
    synchronize_object(Users)
