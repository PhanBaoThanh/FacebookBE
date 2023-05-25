from app.models import Message,Chat
from app import db
from datetime import datetime

def Create(chatId,senderId,content):
    message = Message(ChatId = chatId,SenderId = senderId,Content=content,CreatedAt=datetime.now())
    chat = Chat.query.filter(Chat.ChatId == chatId).first()
    chat.ChatLastUpdate = datetime.now()
    db.session.add(message)
    db.session.commit()
    return message

def FindById(id):
    return Message.query.filter(Message.MessageId == id).first_or_404()

def Delete(id):
    message = Message.query.filter(Message.MessageId == id).first()
    db.session.delete(message)
    db.session.commit()
    return "Deleted"

def DeleteByClientIdAndChatId(chatId,clientId):
    message = Message.query.filter(Message.SenderId == clientId,Message.ChatId == chatId).first()
    db.session.delete(message)
    db.session.commit()
    return 'Deleted'