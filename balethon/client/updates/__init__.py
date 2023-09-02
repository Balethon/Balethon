from .get_updates import GetUpdates
from .set_webhook import SetWebhook
from .delete_webhook import DeleteWebhook


class Updates(GetUpdates, SetWebhook, DeleteWebhook):
    pass
