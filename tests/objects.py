from balethon.objects import Message, CallbackQuery


def main():
    message = Message(message_id=234, text=23)
    print(message.__dict__)

    callback_query = CallbackQuery(id=2345)
    print(callback_query)


if __name__ == "__main__":
    main()
