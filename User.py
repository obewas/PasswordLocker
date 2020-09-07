
class User:
    userList = [] 

    '''Instance of creation of new users'''
    def __init__(self, username, password):
        self.username = username
        self.password = password
 

    """add users"""
    def saveUser(self):
        User.userList.append(self)

    """delete users"""
    def delUser(self):
        User.userList.remove(self)

    """search users"""
    @classmethod
    def search_by_name(cls, username):
        for user in cls.userList:
            if user.username == username:
                return True
        return False
    @classmethod
    def display_users(cls):
        return cls.userList

new_user = User("John","otieno")





    
