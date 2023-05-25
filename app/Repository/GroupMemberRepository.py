from app.models import GroupMember,PostConfirm,Post,Comment,Reaction
from app import db
from sqlalchemy import and_

def Create(manhom,manguoidung,isAdmin):
    groupMember = GroupMember(GroupId = manhom, ClientId = manguoidung,IsAdmin = isAdmin)
    db.session.add(groupMember)
    db.session.commit()
    return groupMember

def Update(manhom,manguoidung,isAdmin):
    groupMember = GroupMember.query.filter(GroupMember.GroupId == manhom, GroupMember.ClientId == manguoidung).first()
    groupMember.IsAdmin = isAdmin
    db.session.commit()
    return groupMember

def FindGroupMemberByClientIdAndGroupId(clientId,groupId):
    return GroupMember.query.filter(GroupMember.GroupId == groupId,GroupMember.ClientId == clientId).first_or_404()

def GetAllByGroupId(manhom):
    return GroupMember.query.filter(GroupMember.GroupId == manhom).all()

def FindById(id):
    return GroupMember.query.filter(GroupMember.GroupMemberId == id).first_or_404()

def GetAllByClientId(manguoidung):
    return GroupMember.query.filter(GroupMember.ClientId == manguoidung).all()

def Delete(id):
    groupMember = GroupMember.query.filter(GroupMember.GroupMemberId == id).first()
    posts = Post.query.filter(Post.ClientId == groupMember.ClientId,Post.GroupId == groupMember.GroupId).all()
    for post in posts:
        reactions = Reaction.query.filter(Reaction.PostId == post.PostId).all()
        comments = Comment.query.filter(Comment.PostId == post.PostId).all()
        if reactions is not None:
            for reaction in reactions:
                db.session.delete(reaction)
        if comments is not None:
            for comment in comments:
                db.session.delete(comment)
        db.session.delete(post)
    postsConfirm = PostConfirm.query.filter(PostConfirm.ClientId == groupMember.ClientId,PostConfirm.GroupId == groupMember.GroupId).all()
    for postConfirm in postsConfirm:
        db.session.delete(postConfirm)
    db.session.delete(groupMember)
    db.session.commit()
    return "Deleted"

def DeleteByClientIdAndGroupId(clientId,groupId):
    posts = Post.query.filter(Post.ClientId == clientId,Post.GroupId == groupId).all()
    for post in posts:
        reactions = Reaction.query.filter(Reaction.PostId == post.PostId).all()
        comments = Comment.query.filter(Comment.PostId == post.PostId).all()
        if reactions is not None:
            for reaction in reactions:
                db.session.delete(reaction)
        if comments is not None:
            for comment in comments:
                db.session.delete(comment)
        db.session.delete(post)
    postsConfirm = PostConfirm.query.filter(PostConfirm.ClientId == clientId,PostConfirm.GroupId == groupId).all()
    for postConfirm in postsConfirm:
        db.session.delete(postConfirm)
    groupMember = GroupMember.query.filter(GroupMember.GroupId == groupId, GroupMember.ClientId == clientId).first()
    db.session.delete(groupMember)
    db.session.commit()
    return 'Deleted'

def DeleteAndUpdateNewAdmin(clientId,groupId,adminId):
    posts = Post.query.filter(Post.ClientId == clientId,Post.GroupId == groupId).all()
    for post in posts:
        reactions = Reaction.query.filter(Reaction.PostId == post.PostId).all()
        comments = Comment.query.filter(Comment.PostId == post.PostId).all()
        if reactions is not None:
            for reaction in reactions:
                db.session.delete(reaction)
        if comments is not None:
            for comment in comments:
                db.session.delete(comment)
        db.session.delete(post)
    postsConfirm = PostConfirm.query.filter(PostConfirm.ClientId == clientId,PostConfirm.GroupId == groupId).all()
    for postConfirm in postsConfirm:
        db.session.delete(postConfirm)
    client = GroupMember.query.filter(GroupMember.ClientId == clientId,GroupMember.GroupId == groupId).first()
    admin = GroupMember.query.filter(GroupMember.ClientId == adminId, GroupMember.GroupId == groupId).first()
    admin.IsAdmin = True
    db.session.delete(client)
    db.session.commit()
    return 'Deleted'
    