from balethon.errors import HTTPError


def main():
    raise HTTPError.create(400, "something went wrong", "SendMessage")


if __name__ == "__main__":
    main()
