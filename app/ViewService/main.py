import sqlite3
from sqlite3 import Error
from app.modelView import GroupInfo,ClientInfo,MemberInfo,FriendRequestInfo,GroupRequestInfo,PostConfirmInfo,PostOfClient,PostOfGroup,CommentOfPost,ReactionOfPost,Test,SearchFriendInfo,MessageInfo,ChatInfo
from app.models import Chat,Message
from sqlalchemy import or_

def GetAllGroupByClientId(clientId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute("select Groups.GroupId,Name,CreatedAt,BackgroundImg,IsPrivate from Groups inner join GroupMember on Groups.GroupId = GroupMember.GroupId where GroupMember.ClientId = ?",[(clientId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(GroupInfo(GroupId = row[0],Name=row[1],CreatedAt=row[2],BackgroundImg=row[3],IsPrivate=row[4]).serialize())
    cursor.close()
    return list

def GetAllGroupRequestByClientId(clientId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    cursor.execute('select Groups.GroupId,Name,GroupRequest.CreatedAt,BackgroundImg,IsPrivate from Groups join GroupRequest on Groups.GroupId = GroupRequest.GroupId where ClientId = ?',[(clientId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(GroupInfo(GroupId = row[0],Name=row[1],CreatedAt=row[2],BackgroundImg=row[3],IsPrivate=row[4]).serialize())
    cursor.close()
    return list

def GetFriendByClientId(clientId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImg from Client inner join Friend on Client.ClientId = Friend.ClientId1 where Friend.ClientId2 = ?',[(clientId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(ClientInfo(ClientId = row[0],Name=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImg=row[9]).serialize())
    cursor.close()
    return list

def GetFriendRequestByClientId(clientId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImg,FriendRequestId,CreatedAt from Client join FriendRequest on Client.ClientId = FriendRequest.ReceiverId where FriendRequest.SenderId = ?',[(clientId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(FriendRequestInfo(ClientId = row[0],Name=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImg=row[9],FriendRequestId=row[10],CreatedAt=row[11]).serialize())
    cursor.close()
    return list

def GetFriendResponseByClientId(clientId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImg,FriendRequestId,CreatedAt from Client join FriendRequest on Client.ClientId = FriendRequest.SenderId where FriendRequest.ReceiverId = ?',[(clientId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(FriendRequestInfo(ClientId = row[0],Name=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImg=row[9],FriendRequestId=row[10],CreatedAt=row[11]).serialize())
    cursor.close()
    return list

def GetAllClientFromGroupMember(groupId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImg,GroupMemberId,GroupId,IsAdmin from Client join GroupMember on Client.ClientId = GroupMember.ClientId where GroupId = ?',[(groupId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(MemberInfo(ClientId = row[0],Name=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImg=row[9],GroupMemberId = row[10],GroupId=row[11],IsAdmin=row[12]).serialize())
    cursor.close()
    return list

def GetAllClientFromGroupRequest(groupId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,BackgroundImg,GroupRequestId,GroupId,CreatedAt from Client join GroupRequest on Client.ClientId = GroupRequest.ClientId where GroupId = ?',[(groupId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(GroupRequestInfo(ClientId = row[0],Name=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImg=row[9],GroupRequestId = row[10],GroupId=row[11],CreatedAt=row[12]).serialize())
    cursor.close()
    return list

def GetAllPostConfirmByGroupId(groupId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Client.Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,Client.BackgroundImg,Groups.GroupId,Groups.Name,Groups.CreatedAt,Groups.BackgroundImg,IsPrivate,PostConfirmId,PostConfirm.CreatedAt,PostConfirm.Content,PostConfirm.Img from Groups  join PostConfirm on Groups.GroupId = PostConfirm.GroupId  join Client on PostConfirm.ClientId = Client.ClientId where Groups.GroupId = ? order by PostConfirm.CreatedAt desc',[(groupId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(PostConfirmInfo(ClientId = row[0],NameClient=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImgClient=row[9],GroupId=row[10],NameGroup=row[11],GroupCreatedAt=row[12],BackgroundImgGroup=row[13],IsPrivate=row[14],PostConfirmId=row[15],PostConfirmCreatedAt=row[16],Content=row[17],PostConfirmImg=row[18]).serialize())
    cursor.close()
    return list

def GetAllPostOfGroupByGroupId(groupId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Client.Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,Client.BackgroundImg,Groups.GroupId,Groups.Name,Groups.CreatedAt,Groups.BackgroundImg,IsPrivate,PostId,Post.CreatedAt,Post.Content,Post.Img from Groups  join Post on Groups.GroupId = Post.GroupId join Client on Post.ClientId = Client.ClientId where Post.GroupId = ? order by Post.CreatedAt desc',[(groupId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(PostOfGroup(ClientId = row[0],NameClient=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImgClient=row[9],GroupId=row[10],NameGroup=row[11],GroupCreatedAt=row[12],BackgroundImgGroup=row[13],IsPrivate=row[14],PostId=row[15],PostCreatedAt=row[16],Content=row[17],PostImg=row[18]).serialize())
    cursor.close()
    return list

def GetAllPostOfClientByClientId(clientId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Client.Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,Client.BackgroundImg,PostId,Post.CreatedAt,Post.Content,Post.Img from Post join Client on Post.ClientId = Client.ClientId where Post.ClientId = ? and Post.GroupId IS NULL order by Post.CreatedAt desc',[(clientId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(PostOfClient(ClientId = row[0],NameClient=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImgClient=row[9],PostId=row[10],PostCreatedAt=row[11],Content=row[12],PostImg=row[13]).serialize())
    cursor.close()
    return list

def GetAllPostOfFriendByClientId(clientId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Client.Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,Client.BackgroundImg,PostId,Post.CreatedAt,Post.Content,Post.Img from Post join Client on Post.ClientId = Client.ClientId where Post.GroupId IS NULL  and (Post.ClientId = ? or Post.ClientId in (select ClientId1 from Friend where ClientId2 = ?) ) order by Post.CreatedAt desc',[(clientId),(clientId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(PostOfClient(ClientId = row[0],NameClient=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImgClient=row[9],PostId=row[10],PostCreatedAt=row[11],Content=row[12],PostImg=row[13]).serialize())
    cursor.close()
    return list

def GetAllCommentOfPostByPostId(postId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Client.Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,Client.BackgroundImg,CommentId,Comment.PostId,Comment.Content,Comment.CreatedAt from Post join Comment on Post.PostId = Comment.PostId join Client on Client.ClientId = Comment.ClientId where Post.PostId = ? order by Comment.CreatedAt desc',[(postId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(CommentOfPost(ClientId = row[0],NameClient=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImgClient=row[9],CommentId=row[10],PostId=row[11],Content=row[12],CommentCreatedAt=row[13]).serialize())
    cursor.close()
    return list

def GetAllCommentOfPostByPostIdLimit(postId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Client.Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,Client.BackgroundImg,CommentId,Comment.PostId,Comment.Content,Comment.CreatedAt from Post join Comment on Post.PostId = Comment.PostId join Client on Client.ClientId = Comment.ClientId where Post.PostId = ? order by Comment.CreatedAt desc limit 3',[(postId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(CommentOfPost(ClientId = row[0],NameClient=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImgClient=row[9],CommentId=row[10],PostId=row[11],Content=row[12],CommentCreatedAt=row[13]).serialize())
    cursor.close()
    return list

def GetAllReactionOfPostByPostId(postId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Client.Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,Client.BackgroundImg,ReactionId,Reaction.PostId from Post join Reaction on Post.PostId = Reaction.PostId join Client on Client.ClientId = Reaction.ClientId where Post.PostId = ?',[(postId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(ReactionOfPost(ClientId = row[0],NameClient=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImgClient=row[9],ReactionId=row[10],PostId=row[11]).serialize())
    cursor.close()
    return list


def searchFriend(key):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Client.Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,Client.BackgroundImg,PostId,Post.CreatedAt,Post.Content,Post.Img from Post join Client on Post.ClientId = Client.ClientId where Post.ClientId = ? and Post.GroupId IS NULL order by Post.CreatedAt desc',[(clientId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(SearchFriendInfo(ClientId = row[0],NameClient=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],ClientBackgroundImg=row[9],FriendId=row[10],FriendClientId1=row[11],FriendClientId2=row[12],FriendRequestId=row[13],SenderId=row[14],ReceiverId=row[15],CreatedAt=row[16]).serialize())
    cursor.close()
    return list





def GetAllPostOfClient(clientId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Client.ClientId,Client.Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,Client.BackgroundImg,PostId,Post.CreatedAt,Post.Content,Post.Img from Post join Client on Post.ClientId = Client.ClientId where Post.ClientId = ? and Post.GroupId IS NULL order by Post.CreatedAt desc',[(clientId)])
    records = cursor.fetchall()
    
    list = []
    for row in records:
        cursor.execute('select Client.ClientId,Client.Name,PhoneNumber,Email,Account,Password,Sex,DayOfBirth,Avatar,Client.BackgroundImg,CommentId,Comment.PostId,Comment.Content,Comment.CreatedAt from Post join Comment on Post.PostId = Comment.PostId join Client on Client.ClientId = Post.ClientId where Post.PostId = ? order by Comment.CreatedAt desc',[(row[10])])
        record = cursor.fetchall()
        listComment = []
        for rowComment in record:
            listComment.append(CommentOfPost(ClientId = rowComment[0],NameClient=rowComment[1],PhoneNumber=rowComment[2],Email=rowComment[3],Account=rowComment[4],Password=rowComment[5],Sex=rowComment[6],DayOfBirth=rowComment[7],Avatar=rowComment[8],BackgroundImgClient=rowComment[9],CommentId=rowComment[10],PostId=rowComment[11],Content=rowComment[12],CommentCreatedAt=rowComment[13]).serialize())
        list.append(Test(ClientId = row[0],NameClient=row[1],PhoneNumber=row[2],Email=row[3],Account=row[4],Password=row[5],Sex=row[6],DayOfBirth=row[7],Avatar=row[8],BackgroundImgClient=row[9],PostId=row[10],PostCreatedAt=row[11],Content=row[12],PostImg=row[13],ListComment=listComment).serialize())
    cursor.close()
    return list

def GetAllMessageByClientId(client1,client2):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Chat.ChatId,ClientId1,ClientId2,MessageId,SenderId,Content,CreatedAt from Chat join Message on Chat.ChatId = Message.ChatId where (ClientId1 = ? and ClientId2 = ?) or (ClientId1 = ? and ClientId2 = ?) order by CreatedAt asc',[(client1),(client2),(client2),(client1)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(MessageInfo(ChatId=row[0],ClientId1=row[1],ClientId2=row[2],MessageId=row[3],SenderId=row[4],Content=row[5],CreatedAt=row[6]).serialize())
    cursor.close()
    return list

def GetAllMessageByChatId(chatId):
    sqliteConnection = sqlite3.connect('app.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute('select Chat.ChatId,ClientId1,ClientId2,MessageId,SenderId,Content,CreatedAt from Chat join Message on Chat.ChatId = Message.ChatId where Chat.ChatId = ? order by CreatedAt asc',[(chatId)])
    records = cursor.fetchall()
    list = []
    for row in records:
        list.append(MessageInfo(ChatId=row[0],ClientId1=row[1],ClientId2=row[2],MessageId=row[3],SenderId=row[4],Content=row[5],CreatedAt=row[6]).serialize())
    cursor.close()
    return list

def GetChatOfClient(clientId):
    chats = Chat.query.filter(or_(Chat.ClientId1 == clientId,Chat.ClientId2 == clientId)).order_by(Chat.ChatLastUpdate.desc()).all()
    list = []
    for chat in chats:
        message = Message.query.filter(Message.ChatId == chat.ChatId).order_by(Message.CreatedAt.desc()).first()
        if message is not None:
            list.append(ChatInfo(ChatId=chat.ChatId,ClientId1=chat.ClientId1,ClientId2=chat.ClientId2,ChatLastUpdate=chat.ChatLastUpdate,MessageId=message.MessageId,SenderId=message.SenderId,Content=message.Content,CreatedAt=message.CreatedAt).serialize())
    return list