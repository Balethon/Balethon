from copy import deepcopy

from balethon.objects import Object


class CopyTextButton(Object):
    def __init__(
            self,
            text: str = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.text: str = text

    def format(self, *args, **kwargs):
        copy_text_button = deepcopy(self)
        copy_text_button.text = copy_text_button.text.format(*args, **kwargs)
        return copy_text_button
