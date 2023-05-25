from app.Repository import PostConfirmRepository

def createPostConfirm(manhom,manguoidung,noidung,anh):
    return PostConfirmRepository.Create(manhom,manguoidung,noidung,anh)

def updatePostConfirm(postConfirmId,content,img):
    return PostConfirmRepository.Update(postConfirmId,content,img)

def getAllPostConfirmByGroupId(manhom):
    return PostConfirmRepository.GetAllByGroupId(manhom)

def finedPostConfirmById(id):
    return PostConfirmRepository.FindById(id)

def deletePostConfirm(id):
    return PostConfirmRepository.Delete(id)

def confirmed(id):
    return PostConfirmRepository.Confirm(id)