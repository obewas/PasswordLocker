import pyperclip
import random 
from cryptography.fernet import Fernet 

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

        #If there exists an older key file, This will remove it. 
        if(os.path.exists(self.__key_file)): 
            os.remove(self.__key_file) 
   
        #Open the Key.key file and place the key in it. 
        #The key file is hidden. 
        try: 
   
            os_type = sys.platform 
            if (os_type == 'linux'): 
                self.__key_file = '.' + self.__key_file 
   
            with open(self.__key_file,'w') as key_in: 
                key_in.write(self.__key.decode()) 
                #Hidding the key file. 
                #The below code snippet finds out which current os the script is running on and does the taks base on it. 
                if(os_type == 'win32'): 
                    ctypes.windll.kernel32.SetFileAttributesW(self.__key_file, 2) 
                else: 
                    pass
   
        except PermissionError: 
            os.remove(self.__key_file) 
            print("A Permission error occurred.\n Please re run the script") 
            sys.exit() 
   
        self.__username = "" 
        self.__password = "" 
        self.__key = "" 
        self.__key_file 
     






    