from asyncio import run, sleep

from balethon import Client
from balethon.objects import InputMediaPhoto, InputMediaVideo

from config import TOKEN, CHAT_ID, USER_ID

PHOTO_URL = "https://bale.ai/_next/image?url=%2Fuploads%2FmainPic.webp&w=1200&q=75"
VIDEO_URL = "https://dev.bale.ai/sites/default/files/1398-03/final_5ce505a96467ba00144535c8_377089.mp4"
AUDIO = "https://vgmsite.com/soundtracks/minecraft/abtibsbmth/1-07.%20Haggstrom.mp3"


async def test_message_methods(client):
    message = await client.send_message(CHAT_ID, "send_message")
    print(f"send_message: {message}")

    await sleep(1)

    response = await client.edit_message_text(CHAT_ID, message.id, "edit_message_text")
    print(f"edit_message_text: {response}")

    await sleep(1)

    response = await client.forward_message(CHAT_ID, CHAT_ID, message.id)
    print(f"forward_message: {response}")

    await sleep(1)

    response = await client.copy_message(CHAT_ID, CHAT_ID, message.id)
    print(f"copy_message: {response}")

    await sleep(1)

    response = await client.delete_message(CHAT_ID, message.id)
    print(f"delete_message: {response}")


async def test_update_methods(client):
    response = await client.get_updates()
    print(f"get_updates: {response}")

    response = await client.set_webhook("url")
    print(f"set_webhook: {response}")

    response = await client.get_webhook_info()
    print(f"get_webhook_info: {response}")

    response = await client.delete_webhook()
    print(f"delete_webhook: {response}")


async def test_user_methods(client):
    response = await client.get_me()
    print(f"get_me: {response}")


async def test_attachment_methods(client):
    response = await client.send_photo(CHAT_ID, PHOTO_URL)
    print(f"send_photo: {response}")

    response = await client.send_audio(CHAT_ID, AUDIO)
    print(f"send_audio: {response}")

    response = await client.send_document(CHAT_ID, PHOTO_URL)
    print(f"send_document: {response}")

    response = await client.send_video(CHAT_ID, VIDEO_URL)
    print(f"send_video: {response}")

    response = await client.send_voice(CHAT_ID, AUDIO)
    print(f"send_voice: {response}")

    response = await client.send_location(CHAT_ID, latitude=10, longitude=10)
    print(f"send_location: {response}")

    response = await client.send_contact(chat_id=CHAT_ID, phone_number="09909090999", first_name="name")
    print(f"send_contact: {response}")

    response = client.send_animation(CHAT_ID, VIDEO_URL)
    print(f"send_animation: {response}")

    response = client.send_media_group(CHAT_ID, [InputMediaPhoto(PHOTO_URL), InputMediaVideo(VIDEO_URL)])
    print(f"send_media_group: {response}")

    response = await client.get_file(CHAT_ID)
    print(f"get_file: {response}")


async def test_chat_methods(client):
    # response = await client.ban_chat_member(CHAT_ID, USER_ID)
    # print(f"ban_chat_member: {response}")

    response = await client.get_chat(CHAT_ID)
    print(f"get_chat: {response}")

    response = await client.get_chat_administrators(CHAT_ID)
    print(f"get_chat_administrators: {response}")

    response = await client.get_chat_member(CHAT_ID, USER_ID)
    print(f"get_chat_member: {response}")

    response = await client.get_chat_members_count(CHAT_ID)
    print(f"get_chat_members_count: {response}")

    # response = await client.invite_user(CHAT_ID, USER_ID)
    # print(f"invite_user: {response}")

    # response = await client.leave_chat(CHAT_ID)
    # print(f"leave_chat: {response}")

    # response = await client.promote_chat_member(CHAT_ID, USER_ID)
    # print(f"promote_chat_member: {response}")

    response = await client.send_chat_action(CHAT_ID)
    print(f"send_chat_action: {response}")

    response = await client.set_chat_photo(CHAT_ID, PHOTO_URL)
    print(f"set_chat_photo: {response}")

    # response = await client.unban_chat_member(CHAT_ID, USER_ID)
    # print(f"unban_chat_member: {response}")


async def test_payment_methods(client):
    response = await client.send_invoice(
        chat_id=CHAT_ID,
        title="Test",
        description="Test",
        payload="Test",
        provider_token="Test",
        prices="0"
    )
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
