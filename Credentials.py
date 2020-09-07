import pyperclip
import random 
class Credentials:
    '''
    class that creates instaces of user accounts
    '''
    def __init__(self, username, password, time_of_expiry):
        self.__username = ""
        self.__password = ""
        self.__time_of_expiry = -1

    """setter of attributes"""
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,username):
        while (username == ''):
            username = input('Enter your chosen username, not blank')
        self.__username = username
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__key = Fernet.generate_key()
        f = Fernet(self.__key)
        self.__password = f.encrypt(password.encode()).decode()
        del f
    @property
    def expiry_time(self):
        return self.__time_of_expiry

    @expiry_time.setter
    def expiry_time(self, exp_time):
        if (exp_time >= 2):
            self.__time_of_expiry = exp_time
    """Function for encrypting password, storing the key and create credential file with username"""
    def create_cred(self):
        cred_filename = 'key.txt'
        with open(cred_filename, "w") as file_in:
            file_in.write("#Credential file:\nUsername={}\nPassword={}\nExpiry={}\n".format(self.__username, self.__password, self.__time_of_expiry))
            file_in.write("++"*20)  
    