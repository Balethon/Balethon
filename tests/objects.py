from balethon.objects import User, unwrap


def main():
    user = User(id=1234, username="@username", first_name="first_name", last_name="last_name")
    print(user)

    print(unwrap(user))

    print(unwrap([user, [user, user]]))


if __name__ == "__main__":
    main()
