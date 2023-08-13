class Condition:

    def __init__(self, function):
        self.function = function

    async def __call__(self, client, update):
        return await self.function(self, client, update)

    def __and__(self, other):
        return AllCondition(self, other)

    def __or__(self, other):
        return AnyCondition(self, other)

    def __invert__(self):
        return NotCondition(self)

    def __repr__(self):
        if hasattr(self, "function") and callable(self.function):
            return self.function.__name__
        return type(self).__name__


class AllCondition(Condition):

    def __init__(self, *conditions):
        super().__init__(None)
        self.conditions = conditions

    async def __call__(self, client, update):
        for condition in self.conditions:
            if not await condition(client, update):
                return False
        return True

    def __repr__(self):
        conditions_string = ", ".join(map(str, self.conditions))
        return f"All({conditions_string})"


class AnyCondition(Condition):

    def __init__(self, *conditions):
        super().__init__(None)
        self.conditions = conditions

    async def __call__(self, client, update):
        for condition in self.conditions:
            if await condition(client, update):
                return True
        return False

    def __repr__(self):
        conditions_string = ", ".join(map(str, self.conditions))
        return f"Any({conditions_string})"


class NotCondition(Condition):

    def __init__(self, condition):
        super().__init__(None)
        self.condition = condition

    async def __call__(self, client, update):
        return not await self.condition(client, update)

    def __repr__(self):
        return f"Not({self.condition})"


@Condition
async def all(condition, client, message):
    return True


@Condition
async def forward(condition, client, message):
    bool(message.get("forward_from") or message.get("forward_from_chat"))


@Condition
async def reply(condition, client, message):
    return bool(message.get("reply_to_message"))


@Condition
async def text(condition, client, message):
    return bool(message.get("text"))


@Condition
async def entities(condition, client, message):
    return bool(message.get("entities") or message.get("caption_entities"))


@Condition
async def document(condition, client, message):
    return bool(message.get("document"))


@Condition
async def photo(condition, client, message):
    return bool(message.get("photo"))


@Condition
async def video(condition, client, message):
    return bool(message.get("video"))


@Condition
async def voice(condition, client, message):
    return bool(message.get("voice"))


@Condition
async def caption(condition, client, message):
    return bool(message.get("caption"))


@Condition
async def contact(condition, client, message):
    return bool(message.get("contact"))


@Condition
async def location(condition, client, message):
    return bool(message.get("location"))


@Condition
async def new_chat_members(condition, client, message):
    return bool(message.get("new_chat_members"))


@Condition
async def left_chat_member(condition, client, message):
    return bool(message.get("left_chat_member"))


@Condition
async def new_chat_title(condition, client, message):
    return bool(message.get("new_chat_title"))


@Condition
async def new_chat_photo(condition, client, message):
    return bool(message.get("new_chat_photo"))


@Condition
async def delete_chat_photo(condition, client, message):
    return bool(message.get("delete_chat_photo"))


@Condition
async def group_chat_created(condition, client, message):
    return bool(message.get("group_chat_created"))


@Condition
async def supergroup_chat_created(condition, client, message):
    return bool(message.get("supergroup_chat_created"))


@Condition
async def channel_chat_created(condition, client, message):
    return bool(message.get("channel_chat_created"))


@Condition
async def pinned_message(condition, client, message):
    return bool(message.get("pinned_message"))


@Condition
async def invoice(condition, client, message):
    return bool(message.get("invoice"))


@Condition
async def media(condition, client, message):
    return bool(
        message.get("photo") or
        message.get("video") or
        message.get("voice") or
        message.get("document")
    )
