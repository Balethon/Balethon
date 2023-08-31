from balethon.objects import Message


def main():
    obj = Message(text=23)
    print(obj.__dict__)


if __name__ == "__main__":
    main()
