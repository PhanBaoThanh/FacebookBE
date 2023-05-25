from app.Repository import ChatRepository

def CreateChat(client1,client2):
    return ChatRepository.Create(client1,client2)

def GetAllChatByClientId(client):
    return ChatRepository.GetAllByClientId(client)

def FindChatById(id):
    return ChatRepository.FindById(id)

def DeleteChatById(id):
    return ChatRepository.DeleteById(id)

def DeleteChatByClientId(client1,client2):
    return ChatRepository.DeleteByClientId(client1,client2)