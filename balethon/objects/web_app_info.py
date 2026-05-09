from copy import deepcopy

from . import Object


class WebAppInfo(Object):
    def __init__(
            self,
            url: str = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.url: str = url

    def format(self, *args, **kwargs):
        web_app_info = deepcopy(self)
        web_app_info.url = web_app_info.url.format(*args, **kwargs)
        return web_app_info
