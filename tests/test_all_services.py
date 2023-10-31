from json import JSONDecodeError

from balethon import Client

import config

bot = Client(config.TOKEN)

services = """
addStickerToSet
answerCallbackQuery
answerInlineQuery
answerPreCheckoutQuery
answerShippingQuery
answerWebAppQuery
approveChatJoinRequest
banChatMember
banChatSenderChat
close
closeForumTopic
closeGeneralForumTopic
copyMessage
createChatInviteLink
createForumTopic
createInvoiceLink
createNewStickerSet
declineChatJoinRequest
deleteChatPhoto
deleteChatStickerSet
deleteForumTopic
deleteMessage
deleteMyCommands
deleteStickerFromSet
deleteStickerSet
deleteWebhook
editChatInviteLink
editForumTopic
editGeneralForumTopic
editMessageCaption
editMessageLiveLocation
editMessageMedia
editMessageReplyMarkup
editMessageText
exportChatInviteLink
forwardMessage
getChat
getChatAdministrators
getChatMember
getChatMemberCount
getChatMenuButton
getCustomEmojiStickers
getFile
getForumTopicIconStickers
getGameHighScores
getMe
getMyCommands
getMyDefaultAdministratorRights
getMyDescription
getMyName
getMyShortDescription
getStickerSet
getUpdates
getUserProfilePhotos
getWebhookInfo
hideGeneralForumTopic
leaveChat
logOut
pinChatMessage
promoteChatMember
reopenForumTopic
reopenGeneralForumTopic
restrictChatMember
revokeChatInviteLink
sendAnimation
sendAudio
sendChatAction
sendContact
sendDice
sendDocument
sendGame
sendInvoice
sendLocation
sendMediaGroup
sendMessage
sendPhoto
sendPoll
sendSticker
sendVenue
sendVideo
sendVideoNote
sendVoice
setChatAdministratorCustomTitle
setChatDescription
setChatMenuButton
setChatPermissions
setChatPhoto
setChatStickerSet
setChatTitle
setCustomEmojiStickerSetThumbnail
setGameScore
setMyCommands
setMyDefaultAdministratorRights
setMyDescription
setMyName
setMyShortDescription
setPassportDataErrors
setStickerEmojiList
setStickerKeywords
setStickerMaskPosition
setStickerPositionInSet
setStickerSetThumbnail
setStickerSetTitle
setWebhook
stopMessageLiveLocation
stopPoll
unbanChatMember
unbanChatSenderChat
unhideGeneralForumTopic
unpinAllChatMessages
unpinAllForumTopicMessages
unpinAllGeneralForumTopicMessages
unpinChatMessage
uploadStickerFile
""".split()


@bot.on_connect()
async def main(client):
    for i, s in enumerate(services, start=1):
        try:
            await client.execute("get", s)
        except JSONDecodeError:
            pass
        except:
            print(f"{i}-{s}: ✅")


if __name__ == "__main__":
    bot.run_polling()
