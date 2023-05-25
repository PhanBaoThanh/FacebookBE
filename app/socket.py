from flask_socketio import emit,disconnect
from app import socketio
from flask_login import current_user

user_online = []
@socketio.on('connect')
def connect_handler():
    print('connected')

@socketio.on('disconnect')
def disconnect():
    print('disconnect')
    
@socketio.on('addUser')
def addUser(user):
    check = False
    for item in user_online:
        if item == user:
            check = True
            break
    if check == False:
        user_online.append(user)
    print(user_online)
    emit('userResponse',user_online,broadcast=True)
    
@socketio.on('removeUser')
def removeUser(user):
    print('removeUser')
    user_online.remove(user)
    emit('userResponse',user_online,broadcast=True)
    
@socketio.on("comment")
def comment(data):
    print('comment')
    emit("commentResponse", data, broadcast=True)
    
@socketio.on('reaction')
def reaction(data):
    print('reaction')
    emit('reactionResponse',data,broadcast=True)
    
@socketio.on('clientInfo')
def clientInfo(data):
    print('clientInfo')
    emit('clientInfoResponse',data,broadcast=True)

@socketio.on('friendRequest')
def friendRequest(data):
    print('friendRequest')
    emit('friendRequestRes',data,broadcast=True)

@socketio.on('friendRequestConfirm')
def friendRequestConfirm(data):
    print('friendRequestConfirm')
    emit('friendRequestConfirmRes',data,broadcast=True)
    
@socketio.on('deleteFriend')
def deleteFriend(data):
    print('deleteFriend')
    emit('deleteFriendResponse',data,broadcast=True)

@socketio.on('post')
def post(data):
    print('post')
    emit('postResponse',data,broadcast=True)
    
@socketio.on('groupInfo')
def groupInfo(data):
    print('groupInfo')
    emit('groupInfoResponse',data,broadcast=True)
    
@socketio.on('groupMemberRequest')
def groupMemberRequest(data):
    print('groupMemberRequest')
    emit('groupMemberRequestRes',data,broadcast=True)
    
@socketio.on('groupMemberRequestConfirm')
def groupMemberRequestConfirm(data):
    print('groupMemberRequestConfirm')
    emit('groupMemberRequestConfirmRes',data,broadcast=True)

@socketio.on('postGroup')
def postGroup(data):
    print('postGroup')
    emit('postGroupResponse',data,broadcast=True)
    
@socketio.on('outGroup')
def outGroup(data):
    print('outGroup')
    emit('outGroupResponse',data,broadcast=True)

@socketio.on('deleteGroup')
def deleteGroup(data):
    print('deleteGroup')
    emit('deleteGroupResponse',data,broadcast=True)
    
@socketio.on('postConfirm')
def postConfirm(data):
    print('postConfirm')
    emit('postConfirmResponse',data,broadcast=True)
    
@socketio.on('message')
def message(data):
    print('message')
    emit('messageResponse',data,broadcast=True)