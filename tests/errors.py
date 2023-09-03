from balethon.errors import RPCError


def main():
    raise RPCError.create(400, "something went wrong", "SendMessage")


if __name__ == "__main__":
    main()
