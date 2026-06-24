from .abacus_pb2 import *
from .auth_pb2 import *
from .configs_pb2 import *
from .files_pb2 import *
from .groups_pb2 import *
from .messaging_pb2 import *
from .presence_pb2 import *
from .request_pb2 import *
from .users_pb2 import *

GetMessageViews.service_name = "bale.abacus.v1.Abacus"
GetMessageViews.method = "GetMessagesViews"
GetMessageViews.http2 = False

MessageSetReaction.service_name = "bale.abacus.v1.Abacus"
MessageSetReaction.method = "MessageSetReaction"
MessageSetReaction.http2 = False

StartPhoneAuth.service_name = "bale.auth.v1.Auth"
StartPhoneAuth.method = "StartPhoneAuth"
StartPhoneAuth.http2 = True

ValidateCode.service_name = "bale.auth.v1.Auth"
ValidateCode.method = "ValidateCode"
ValidateCode.http2 = True

ValidatePassword.service_name = "bale.auth.v1.Auth"
ValidatePassword.method = "ValidatePassword"
ValidatePassword.http2 = True

SignUp.service_name = "bale.auth.v1.Auth"
SignUp.method = "SignUp"
SignUp.http2 = True

TerminateAllSessions.service_name = "bale.auth.v1.Auth"
TerminateAllSessions.method = "TerminateAllSessions"
TerminateAllSessions.http2 = True

GetJWTToken.service_name = "bale.auth.v1.Auth"
GetJWTToken.method = "GetJWTToken"
GetJWTToken.http2 = True

EditParameter.service_name = "bale.v1.Configs"
EditParameter.method = "EditParameter"
EditParameter.http2 = False

GetNasimFileUploadUrl.service_name = "ai.bale.server.Files"
GetNasimFileUploadUrl.method = "GetNasimFileUploadUrl"
GetNasimFileUploadUrl.http2 = False

GetNasimFileUrl.service_name = "ai.bale.server.Files"
GetNasimFileUrl.method = "GetNasimFileUrl"
GetNasimFileUrl.http2 = False

JoinGroup.service_name = "bale.groups.v1.Groups"
JoinGroup.method = "JoinGroup"
JoinGroup.http2 = False

JoinPublicGroup.service_name = "bale.groups.v1.Groups"
JoinPublicGroup.method = "JoinPublicGroup"
JoinPublicGroup.http2 = False

LeaveGroup.service_name = "bale.groups.v1.Groups"
LeaveGroup.method = "LeaveGroup"
LeaveGroup.http2 = False

GetFullGroup.service_name = "bale.groups.v1.Groups"
GetFullGroup.method = "GetFullGroup"
GetFullGroup.http2 = False

PinMessage.service_name = "bale.groups.v1.Groups"
PinMessage.method = "PinMessage"
PinMessage.http2 = False

EditGroupAvatar.service_name = "bale.groups.v1.Groups"
EditGroupAvatar.method = "EditGroupAvatar"
EditGroupAvatar.http2 = False

LoadGroupAvatars.service_name = "bale.groups.v1.Groups"
LoadGroupAvatars.method = "LoadGroupAvatars"
LoadGroupAvatars.http2 = False

RemoveGroupAvatar.service_name = "bale.groups.v1.Groups"
RemoveGroupAvatar.method = "RemoveGroupAvatar"
RemoveGroupAvatar.http2 = False

EditGroupTitle.service_name = "bale.groups.v1.Groups"
EditGroupTitle.method = "EditGroupTitle"
EditGroupTitle.http2 = False

EditGroupAbout.service_name = "bale.groups.v1.Groups"
EditGroupAbout.method = "EditGroupAbout"
EditGroupAbout.http2 = False

RevokeInviteUrl.service_name = "bale.groups.v1.Groups"
RevokeInviteUrl.method = "RevokeInviteUrl"
RevokeInviteUrl.http2 = False

UnBanUser.service_name = "bale.groups.v1.Groups"
UnBanUser.method = "UnBanUser"
UnBanUser.http2 = False

KickUser.service_name = "bale.groups.v1.Groups"
KickUser.method = "KickUser"
KickUser.http2 = False

GetGroupInviteUrl.service_name = "bale.groups.v1.Groups"
GetGroupInviteUrl.method = "GetGroupInviteUrl"
GetGroupInviteUrl.http2 = False

InviteUsers.service_name = "bale.groups.v1.Groups"
InviteUsers.method = "InviteUsers"
InviteUsers.http2 = False

SetMemberPermissions.service_name = "bale.groups.v1.Groups"
SetMemberPermissions.method = "SetMemberPermissions"
SetMemberPermissions.http2 = False

LoadMembers.service_name = "bale.groups.v1.Groups"
LoadMembers.method = "LoadMembers"
LoadMembers.http2 = False

GetGroupMembersCount.service_name = "bale.groups.v1.Groups"
GetGroupMembersCount.method = "GetGroupMembersCount"
GetGroupMembersCount.http2 = False

RemoveSinglePin.service_name = "bale.groups.v1.Groups"
RemoveSinglePin.method = "RemoveSinglePin"
RemoveSinglePin.http2 = False

RemovePin.service_name = "bale.groups.v1.Groups"
RemovePin.method = "RemovePin"
RemovePin.http2 = False

RemoveUserAdmin.service_name = "bale.groups.v1.Groups"
RemoveUserAdmin.method = "RemoveUserAdmin"
RemoveUserAdmin.http2 = False

GetGroupPreview.service_name = "bale.groups.v1.Groups"
GetGroupPreview.method = "GetGroupPreview"
GetGroupPreview.http2 = False

SendMessage.service_name = "bale.messaging.v2.Messaging"
SendMessage.method = "SendMessage"
SendMessage.http2 = False

UpdateMessage.service_name = "bale.messaging.v2.Messaging"
UpdateMessage.method = "UpdateMessage"
UpdateMessage.http2 = False

DeleteMessage.service_name = "bale.messaging.v2.Messaging"
DeleteMessage.method = "DeleteMessage"
DeleteMessage.http2 = False

ForwardMessages.service_name = "bale.messaging.v2.Messaging"
ForwardMessages.method = "ForwardMessages"
ForwardMessages.http2 = False

LoadHistory.service_name = "bale.messaging.v2.Messaging"
LoadHistory.method = "LoadHistory"
LoadHistory.http2 = False

PinMessages.service_name = "bale.messaging.v2.Messaging"
PinMessages.method = "PinMessage"
PinMessages.http2 = False

UnPinMessages.service_name = "bale.messaging.v2.Messaging"
UnPinMessages.method = "UnPinMessages"
UnPinMessages.http2 = False

LoadPinnedMessages.service_name = "bale.messaging.v2.Messaging"
LoadPinnedMessages.method = "LoadPinnedMessages"
LoadPinnedMessages.http2 = False

SendMultiMediaMessage.service_name = "bale.messaging.v2.Messaging"
SendMultiMediaMessage.method = "SendMultiMediaMessage"
SendMultiMediaMessage.http2 = False

LoadDialogs.service_name = "bale.messaging.v2.Messaging"
LoadDialogs.method = "LoadDialogs"
LoadDialogs.http2 = False

SetOnline.service_name = "bale.presence.v1.Presence"
SetOnline.method = "SetOnline"
SetOnline.http2 = False

Typing.service_name = "bale.presence.v1.Presence"
Typing.method = "Typing"
Typing.http2 = False

EditName.service_name = "bale.users.v1.Users"
EditName.method = "EditName"
EditName.http2 = False

LoadUsers.service_name = "bale.users.v1.Users"
LoadUsers.method = "LoadUsers"
LoadUsers.http2 = False

LoadFullUsers.service_name = "bale.users.v1.Users"
LoadFullUsers.method = "LoadFullUsers"
LoadFullUsers.http2 = False

SearchContacts.service_name = "bale.users.v1.Users"
SearchContacts.method = "SearchContacts"
SearchContacts.http2 = False
