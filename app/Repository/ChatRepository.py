from app.models import Chat
from app import db
from datetime import datetime
from sqlalchemy import or_,and_

def Create(client1,client2):
    chat = Chat(ClientId1 = client1,ClientId2 = client2)
    db.session.add(chat)
    db.session.commit()
    return chat

def GetAllByClientId(client):
    return Chat.query.filter(or_(Chat.ClientId1 == client,Chat.ClientId2 == client)).order_by(Chat.ChatLastUpdate.desc()).all()

def FindById(id):
    return Chat.query.filter(Chat.ChatId == id).first_or_404()

def DeleteById(id):
    chat = Chat.query.filter(Chat.ChatId == id).first()
    db.session.delete(chat)
    db.session.commit()
    return 'Deleted'

def DeleteByClientId(client1,client2):
    chat = Chat.query.filter(or_(and_(Chat.ClientId1 == client1,Chat.ClientId2 == client2),and_(Chat.ClientId1==client2,Chat.ClientId2==client1))).first()
    db.session.delete(chat)
    db.session.commit()
    return 'Deleted'