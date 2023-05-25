from app import db
import datetime
import json
from json import JSONEncoder

class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()
        
class GroupInfo():
    GroupId = ""
    Name = ""
    CreatedAt = ""
    BackgroundImg = ""
    IsPrivate = ""
    
    def __init__(self,GroupId,Name,CreatedAt,BackgroundImg,IsPrivate):
        self.GroupId = GroupId
        self.Name = Name
        self.CreatedAt = CreatedAt
        self.BackgroundImg = BackgroundImg
        self.IsPrivate = IsPrivate
        
    def serialize(self):
        return {
            'groupId': self.GroupId,
            'name': self.Name,
            'createdAt':self.CreatedAt ,
            'backgroundImg': self.BackgroundImg,
            'isPrivate': self.IsPrivate
        }
        
class ClientInfo():
    ClientId = ""
    Name = ""
    PhoneNumber = ""
    Email = ""
    Account = ""
    Password = ""
    Sex = ""
    DayOfBirth = ""
    Avatar = ""
    BackgroundImg = ""
    
    def __init__(self,ClientId,Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImg):
        self.ClientId = ClientId
        self.Name = Name
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Account = Account
        self.Password = Password
        self.Sex = Sex
        self.DayOfBirth = DayOfBirth
        self.Avatar = Avatar
        self.BackgroundImg = BackgroundImg
        
    def serialize(self):
        return {
            'clientId': self.ClientId,
            'name': self.Name,
            'phoneNumber': self.PhoneNumber,
            'email': self.Email,
            'account': self.Account,
            'password': self.Password,
            'sex': self.Sex,
            'dayOfBirth': self.DayOfBirth,
            'avatar': self.Avatar,
            'backgroundImg': self.BackgroundImg
        }
        
class FriendRequestInfo():
    ClientId = ""
    Name = ""
    PhoneNumber = ""
    Email = ""
    Account = ""
    Password = ""
    Sex = ""
    DayOfBirth = ""
    Avatar = ""
    BackgroundImg = ""
    FriendRequestId = ''
    CreatedAt = ''

    
    def __init__(self,ClientId,Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImg,FriendRequestId,CreatedAt):
        self.ClientId = ClientId
        self.Name = Name
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Account = Account
        self.Password = Password
        self.Sex = Sex
        self.DayOfBirth = DayOfBirth
        self.Avatar = Avatar
        self.BackgroundImg = BackgroundImg
        self.FriendRequestId = FriendRequestId
        self.CreatedAt = CreatedAt
        
    def serialize(self):
        return {
            'clientId': self.ClientId,
            'name': self.Name,
            'phoneNumber': self.PhoneNumber,
            'email': self.Email,
            'account': self.Account,
            'password': self.Password,
            'sex': self.Sex,
            'dayOfBirth': self.DayOfBirth,
            'avatar': self.Avatar,
            'backgroundImg': self.BackgroundImg,
            'friendRequestId': self.FriendRequestId,
            'createdAt': self.CreatedAt
        }
    
class GroupRequestInfo():
    ClientId = ""
    Name = ""
    PhoneNumber = ""
    Email = ""
    Account = ""
    Password = ""
    Sex = ""
    DayOfBirth = ""
    Avatar = ""
    BackgroundImg = ""
    GroupRequestId = ''
    GroupId = ""
    CreatedAt = ''
    
    def __init__(self,ClientId,Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImg,GroupRequestId,GroupId,CreatedAt):
        self.ClientId = ClientId
        self.Name = Name
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Account = Account
        self.Password = Password
        self.Sex = Sex
        self.DayOfBirth = DayOfBirth
        self.Avatar = Avatar
        self.BackgroundImg = BackgroundImg
        self.GroupRequestId = GroupRequestId
        self.GroupId = GroupId
        self.CreatedAt = CreatedAt
        
    def serialize(self):
        return {
            'clientId': self.ClientId,
            'name': self.Name,
            'phoneNumber': self.PhoneNumber,
            'email': self.Email,
            'account': self.Account,
            'password': self.Password,
            'sex': self.Sex,
            'dayOfBirth': self.DayOfBirth,
            'avatar': self.Avatar,
            'backgroundImg': self.BackgroundImg,
            'groupRequestId': self.GroupRequestId,
            'groupId': self.GroupId,
            'createdAt': self.CreatedAt
        }

class MemberInfo():
    ClientId = ""
    Name = ""
    PhoneNumber = ""
    Email = ""
    Account = ""
    Password = ""
    Sex = ""
    DayOfBirth = ""
    Avatar = ""
    BackgroundImg = ""
    GroupMemberId = ''
    GroupId = ""
    IsAdmin = False
    
    def __init__(self,ClientId,Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImg,GroupMemberId,GroupId,IsAdmin):
        self.ClientId = ClientId
        self.Name = Name
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Account = Account
        self.Password = Password
        self.Sex = Sex
        self.DayOfBirth = DayOfBirth
        self.Avatar = Avatar
        self.BackgroundImg = BackgroundImg
        self.GroupMemberId = GroupMemberId
        self.GroupId = GroupId
        self.IsAdmin = IsAdmin
        
    def serialize(self):
        return {
            'clientId': self.ClientId,
            'name': self.Name,
            'phoneNumber': self.PhoneNumber,
            'email': self.Email,
            'account': self.Account,
            'password': self.Password,
            'sex': self.Sex,
            'dayOfBirth': self.DayOfBirth,
            'avatar': self.Avatar,
            'backgroundImg': self.BackgroundImg,
            'groupMemberId': self.GroupMemberId,
            'groupId': self.GroupId,
            'isAdmin': self.IsAdmin
        }

class PostConfirmInfo():
    ClientId = ""
    NameClient = ""
    PhoneNumber = ""
    Email = ""
    Account = ""
    Password = ""
    Sex = ""
    DayOfBirth = ""
    Avatar = ""
    BackgroundImgClient = ""
    GroupId = ""
    NameGroup = ""
    GroupCreatedAt = ""
    BackgroundImgGroup = ""
    IsPrivate = ""
    PostConfirmId = ''
    PostConfirmCreatedAt = ''
    Content = ''
    PostConfirmImg = ''

    
    def __init__(self,ClientId,NameClient,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImgClient,GroupId,NameGroup,GroupCreatedAt,BackgroundImgGroup,IsPrivate,PostConfirmId,PostConfirmCreatedAt,Content,PostConfirmImg):
        self.ClientId = ClientId
        self.NameClient = NameClient
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Account = Account
        self.Password = Password
        self.Sex = Sex
        self.DayOfBirth = DayOfBirth
        self.Avatar = Avatar
        self.BackgroundImgClient = BackgroundImgClient
        self.GroupId = GroupId
        self.NameGroup = NameGroup
        self.GroupCreatedAt = GroupCreatedAt
        self.BackgroundImgGroup = BackgroundImgGroup
        self.IsPrivate = IsPrivate
        
        self.PostConfirmId = PostConfirmId
        self.PostConfirmCreatedAt = PostConfirmCreatedAt
        self.Content = Content
        self.PostConfirmImg = PostConfirmImg
        
    def serialize(self):
        return {
            'clientId': self.ClientId,
            'nameClient': self.NameClient,
            'phoneNumber': self.PhoneNumber,
            'email': self.Email,
            'account': self.Account,
            'password': self.Password,
            'sex': self.Sex,
            'dayOfBirth':self.DayOfBirth,
            'avatar': self.Avatar,
            'backgroundImgClient': self.BackgroundImgClient,
            'groupId': self.GroupId,
            'nameGroup': self.NameGroup,
            'groupCreatedAt':self.GroupCreatedAt,
            'backgroundImgGroup': self.BackgroundImgGroup,
            'isPrivate': self.IsPrivate,
            'postConfirmId': self.PostConfirmId,
            'postConfirmCreatedAt':self.PostConfirmCreatedAt,
            'content': self.Content,
            'postConfirmImg': self.PostConfirmImg
        }

class PostOfGroup():
    ClientId = ""
    NameClient = ""
    PhoneNumber = ""
    Email = ""
    Account = ""
    Password = ""
    Sex = ""
    DayOfBirth = ""
    Avatar = ""
    BackgroundImgClient = ""
    GroupId = ""
    NameGroup = ""
    GroupCreatedAt = ""
    BackgroundImgGroup = ""
    IsPrivate = ""
    PostId = ''
    PostCreatedAt = ''
    Content = ''
    PostImg = ''

    
    def __init__(self,ClientId,NameClient,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImgClient,GroupId,NameGroup,GroupCreatedAt,BackgroundImgGroup,IsPrivate,PostId,PostCreatedAt,Content,PostImg):
        self.ClientId = ClientId
        self.NameClient = NameClient
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Account = Account
        self.Password = Password
        self.Sex = Sex
        self.DayOfBirth = DayOfBirth
        self.Avatar = Avatar
        self.BackgroundImgClient = BackgroundImgClient
        self.GroupId = GroupId
        self.NameGroup = NameGroup
        self.GroupCreatedAt = GroupCreatedAt
        self.BackgroundImgGroup = BackgroundImgGroup
        self.IsPrivate = IsPrivate
        self.PostId = PostId
        self.PostCreatedAt = PostCreatedAt
        self.Content = Content
        self.PostImg = PostImg
        
    def serialize(self):
        return {
            'clientId': self.ClientId,
            'nameClient': self.NameClient,
            'phoneNumber': self.PhoneNumber,
            'email': self.Email,
            'account': self.Account,
            'password': self.Password,
            'sex': self.Sex,
            'dayOfBirth':self.DayOfBirth,
            'avatar': self.Avatar,
            'backgroundImgClient': self.BackgroundImgClient,
            'groupId': self.GroupId,
            'nameGroup': self.NameGroup,
            'groupCreatedAt':self.GroupCreatedAt,
            'backgroundImgGroup': self.BackgroundImgGroup,
            'isPrivate': self.IsPrivate,
            'postId': self.PostId,
            'postCreatedAt':self.PostCreatedAt,
            'content': self.Content,
            'postImg': self.PostImg
        }
    
class PostOfClient():
    ClientId = ""
    NameClient = ""
    PhoneNumber = ""
    Email = ""
    Account = ""
    Password = ""
    Sex = ""
    DayOfBirth = ""
    Avatar = ""
    BackgroundImgClient = ""
    PostId = ''
    PostCreatedAt = ''
    Content = ''
    PostImg = ''

    
    def __init__(self,ClientId,NameClient,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImgClient,PostId,PostCreatedAt,Content,PostImg):
        self.ClientId = ClientId
        self.NameClient = NameClient
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Account = Account
        self.Password = Password
        self.Sex = Sex
        self.DayOfBirth = DayOfBirth
        self.Avatar = Avatar
        self.BackgroundImgClient = BackgroundImgClient
        self.PostId = PostId
        self.PostCreatedAt = PostCreatedAt
        self.Content = Content
        self.PostImg = PostImg
        
    def serialize(self):
        return {
            'clientId': self.ClientId,
            'nameClient': self.NameClient,
            'phoneNumber': self.PhoneNumber,
            'email': self.Email,
            'account': self.Account,
            'password': self.Password,
            'sex': self.Sex,
            'dayOfBirth':self.DayOfBirth,
            'avatar': self.Avatar,
            'backgroundImgClient': self.BackgroundImgClient,
            'postId': self.PostId,
            'postCreatedAt':self.PostCreatedAt,
            'content': self.Content,
            'postImg': self.PostImg
        }
        
class CommentOfPost():
    ClientId = ""
    NameClient = ""
    PhoneNumber = ""
    Email = ""
    Account = ""
    Password = ""
    Sex = ""
    DayOfBirth = ""
    Avatar = ""
    BackgroundImgClient = ""
    CommentId = ''
    PostId = ''
    Content = ''
    CommentCreatedAt = ''
    
    def __init__(self,ClientId,NameClient,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImgClient,CommentId,PostId,Content,CommentCreatedAt):
        self.ClientId = ClientId
        self.NameClient = NameClient
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Account = Account
        self.Password = Password
        self.Sex = Sex
        self.DayOfBirth = DayOfBirth
        self.Avatar = Avatar
        self.BackgroundImgClient = BackgroundImgClient
        self.CommentId = CommentId
        self.PostId = PostId
        self.Content = Content
        self.CommentCreatedAt = CommentCreatedAt
        
    def serialize(self):
        return {
            'clientId': self.ClientId,
            'nameClient': self.NameClient,
            'phoneNumber': self.PhoneNumber,
            'email': self.Email,
            'account': self.Account,
            'password': self.Password,
            'sex': self.Sex,
            'dayOfBirth': self.DayOfBirth,
            'avatar': self.Avatar,
            'backgroundImgClient': self.BackgroundImgClient,
            'commentId': self.CommentId,
            'postId': self.PostId,
            'content': self.Content,
            'commentCreatedAt':self.CommentCreatedAt 
        }
    
class ReactionOfPost():
    ClientId = ""
    NameClient = ""
    PhoneNumber = ""
    Email = ""
    Account = ""
    Password = ""
    Sex = ""
    DayOfBirth = ""
    Avatar = ""
    BackgroundImgClient = ""
    ReactionId = ''
    PostId = ''
        
    def __init__(self,ClientId,NameClient,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImgClient,ReactionId,PostId):
        self.ClientId = ClientId
        self.NameClient = NameClient
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Account = Account
        self.Password = Password
        self.Sex = Sex
        self.DayOfBirth = DayOfBirth
        self.Avatar = Avatar
        self.BackgroundImgClient = BackgroundImgClient
        self.ReactionId = ReactionId
        self.PostId = PostId
        
    def serialize(self):
        return {
            'clientId': self.ClientId,
            'nameClient': self.NameClient,
            'phoneNumber': self.PhoneNumber,
            'email': self.Email,
            'account': self.Account,
            'password': self.Password,
            'sex': self.Sex,
            'dayOfBirth':self.DayOfBirth,
            'avatar': self.Avatar,
            'backgroundImgClient': self.BackgroundImgClient,
            'reactionId': self.ReactionId,
            'postId': self.PostId
        }

class Test():
    ClientId = ""
    NameClient = ""
    PhoneNumber = ""
    Email = ""
    Account = ""
    Password = ""
    Sex = ""
    DayOfBirth = ""
    Avatar = ""
    BackgroundImgClient = ""
    PostId = ''
    PostCreatedAt = ''
    Content = ''
    PostImg = ''
    ListComment = []

    
    def __init__(self,ClientId,NameClient,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImgClient,PostId,PostCreatedAt,Content,PostImg,ListComment):
        self.ClientId = ClientId
        self.NameClient = NameClient
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Account = Account
        self.Password = Password
        self.Sex = Sex
        self.DayOfBirth = DayOfBirth
        self.Avatar = Avatar
        self.BackgroundImgClient = BackgroundImgClient
        self.PostId = PostId
        self.PostCreatedAt = PostCreatedAt
        self.Content = Content
        self.PostImg = PostImg
        self.ListComment = ListComment
        
    def serialize(self):
        return {
            'clientId': self.ClientId,
            'nameClient': self.NameClient,
            'phoneNumber': self.PhoneNumber,
            'email': self.Email,
            'account': self.Account,
            'password': self.Password,
            'sex': self.Sex,
            'dayOfBirth':self.DayOfBirth,
            'avatar': self.Avatar,
            'backgroundImgClient': self.BackgroundImgClient,
            'postId': self.PostId,
            'postCreatedAt':self.PostCreatedAt,
            'content': self.Content,
            'postImg': self.PostImg,
            'listComment': self.ListComment
        }
        
class SearchFriendInfo():
    ClientId = ""
    ClientName = ""
    PhoneNumber = ""
    Email = ""
    Account = ""
    Password = ""
    Sex = ""
    DayOfBirth = ""
    Avatar = ""
    ClientBackgroundImg = ""
    FriendId = ''
    FriendClientId1 = ''
    FriendClientId2 = ''
    FriendRequestId = ''
    SenderId = ''
    ReceiverId = ''
    CreatedAt = ''
    
    def __init__(self,ClientId,ClientName,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,ClientBackgroundImg,FriendId,FriendClientId1,FriendClientId2,FriendRequestId,SenderId,ReceiverId,CreatedAt):
        self.ClientId = ClientId
        self.ClientName = ClientName
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Account = Account
        self.Password = Password
        self.Sex = Sex
        self.DayOfBirth = DayOfBirth
        self.Avatar = Avatar
        self.ClientBackgroundImg = ClientBackgroundImg
        self.FriendId = FriendId
        self.FriendClientId1 = FriendClientId1
        self.FriendClientId2 = FriendClientId2
        self.FriendRequestId = FriendRequestId
        self.SenderId = SenderId
        self.ReceiverId = ReceiverId
        self.CreatedAt = CreatedAt
    
    def serialize(self):
        return {
            'clientId': self.ClientId,
            'clientName': self.ClientName,
            'phoneNumber': self.PhoneNumber,
            'email': self.Email,
            'account': self.Account,
            'password': self.Password,
            'sex': self.Sex,
            'dayOfBirth':  json.dumps(self.DayOfBirth,indent=4,cls=DateTimeEncoder),
            'avatar': self.Avatar,
            'clientBackgroundImg': self.ClientBackgroundImg,
            'friendId': self.FriendId,
            'friendClientId1': self.FriendClientId1,
            'friendClientId2': self.FriendClientId2,
            'friendRequestId': self.FriendRequestId,
            'senderId': self.SenderId,
            'receiverId': self.ReceiverId,
            'createdAt': json.dumps(self.CreatedAt,indent=4,cls=DateTimeEncoder)
        }
        
class MessageInfo():
    ChatId = ""
    ClientId1 = ""
    ClientId2 = ""
    MessageId = ""
    SenderId = ""
    Content = ""
    CreatedAt = ""

    
    def __init__(self,ChatId,ClientId1,ClientId2,MessageId,SenderId,Content,CreatedAt):
        self.ChatId = ChatId
        self.ClientId1 = ClientId1
        self.ClientId2 = ClientId2
        self.MessageId = MessageId
        self.SenderId = SenderId
        self.Content = Content
        self.CreatedAt = CreatedAt
        
    def serialize(self):
        return {
            'chatId': self.ChatId,
            'clientId1': self.ClientId1,
            'clientId2': self.ClientId2,
            'messageId': self.MessageId,
            'senderId': self.SenderId,
            'content': self.Content,
            'createdAt': self.CreatedAt
        }
        
class ChatInfo():
    ChatId = ''
    ClientId1 = ''
    ClientId2 = ''
    ChatLastUpdate = ''
    MessageId = ""
    SenderId = ""
    Content = ""
    CreatedAt = ""
    
    def __init__(self,ChatId,ClientId1,ClientId2,ChatLastUpdate,MessageId,SenderId,Content,CreatedAt):
        self.ChatId = ChatId
        self.ClientId1 = ClientId1
        self.ClientId2 = ClientId2
        self.ChatLastUpdate = ChatLastUpdate
        self.MessageId = MessageId
        self.SenderId = SenderId
        self.Content = Content
        self.CreatedAt = CreatedAt
        
    def serialize(self):
        return {
            'chatId': self.ChatId,
            'clientId1': self.ClientId1,
            'clientId2': self.ClientId2,
            'chatLastUpdate': json.dumps(self.ChatLastUpdate,indent=4,cls=DateTimeEncoder),
            'messageId': self.MessageId,
            'senderId': self.SenderId,
            'content': self.Content,
            'createdAt': json.dumps(self.CreatedAt,indent=4,cls=DateTimeEncoder)
        }