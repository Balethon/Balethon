from asyncio import run, sleep

from balethon import Client

from config import TOKEN, CHAT_ID, USER_ID

PHOTO_URL = "https://www.bale.ai/img/bale-main.png"
VIDEO_URL = "https://dev.bale.ai/sites/default/files/1398-03/final_5ce505a96467ba00144535c8_377089.mp4"


async def test_message_methods(client):
    message = await client.send_message(CHAT_ID, "send_message")
    print(f"send_message: {message}")

    await sleep(1)

    response = await client.edit_message_text(CHAT_ID, message["message_id"], "edit_message_text")
    print(f"edit_message_text: {response}")

    await sleep(1)

    response = await client.delete_message(CHAT_ID, message["message_id"])
    print(f"delete_message: {response}")


async def test_update_methods(client):
    response = await client.get_updates()
    print(f"get_updates: {response}")

    response = await client.set_webhook("url")
    print(f"set_webhook: {response}")

    response = await client.delete_webhook()
    print(f"delete_webhook: {response}")


async def test_user_methods(client):
    response = await client.get_me()
    print(f"get_me: {response}")


async def test_attachment_methods(client):
    response = await client.send_photo(CHAT_ID, PHOTO_URL)
    print(f"send_photo: {response}")

    # response = await client.send_audio()
    # print(f"send_audio: {response}")

    response = await client.send_document(CHAT_ID, PHOTO_URL)
    print(f"send_document: {response}")

    response = await client.send_video(CHAT_ID, VIDEO_URL)
    print(f"send_video: {response}")

    # response = await client.send_voice()
    # print(f"send_voice: {response}")

    response = await client.send_location(CHAT_ID, latitude=10, longitude=10)
    print(f"send_location: {response}")

    # response = await client.send_contact()
    # print(f"send_contact: {response}")

    response = await client.get_file(CHAT_ID)
    print(f"get_file: {response}")


async def test_chat_methods(client):
    response = await client.get_chat(CHAT_ID)
    print(f"get_chat: {response}")

    response = await client.get_chat_administrators(CHAT_ID)
    print(f"get_chat_administrators: {response}")

    response = await client.get_chat_members_count(CHAT_ID)
    print(f"get_chat_members_count: {response}")

    response = await client.get_chat_member(CHAT_ID, USER_ID)
    print(f"get_chat_member: {response}")


async def test_payment_methods(client):
    response = await client.send_invoice(CHAT_ID, "Test", "Test", "Test", "0")
    print(f"send_invoice: {response}")


async def main():
    bot = Client(TOKEN)
    async with bot:
        await test_message_methods(bot)
        await test_update_methods(bot)
        await test_user_methods(bot)
        await test_attachment_methods(bot)
        await test_chat_methods(bot)
        await test_payment_methods(bot)


if __name__ == "__main__":
    run(main())
