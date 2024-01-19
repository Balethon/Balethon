from .delete_webhook import DeleteWebhook
from .get_updates import GetUpdates
from .get_webhook_info import GetWebhookInfo
from .set_webhook import SetWebhook


class Updates(DeleteWebhook, GetUpdates, GetWebhookInfo, SetWebhook):
    pass
