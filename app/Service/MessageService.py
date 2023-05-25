from app.Repository import MessageRepository

def createMessage(chatId,senderId,content):
    return MessageRepository.Create(chatId,senderId,content)

def findMessageById(id):
    return MessageRepository.FindById(id)

def deleteMessage(id):
    return MessageRepository.Delete(id)

def deleteMessageByClientIdAndChatId(chatId,clientId):
    return MessageRepository.DeleteByClientIdAndChatId(chatId,clientId)