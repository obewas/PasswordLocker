import pyperclip
class Credentials:
    '''
    class that creates instaces of user accounts
    '''
    cred_list = []

    #Initialise credentials
    def __init__(self, account , email , secretlock):
    
        self.account = account
        self.email = email
        self.secretlock = secretlock


    #save credentials

    def save_cred(self):
        '''
        saving credentials in cred_list
        '''
        Credentials.cred_list.append(self)

    #Delete credentils

    def delete_cred(self):
        '''
        deleting credentials from cred_list
        '''
        Credentials.cred_list.remove(self)    

   #search for credentials

    @classmethod
    def find_account(cls, account):
        '''
        searching for credentials
        '''
        for cred in cls.cred_list:
            if cred.account == account:
                return cred    
    #confirm if credentials exist

    @classmethod
    def cred_exists(cls, account):
        '''
        confirming if a credential exists
        '''
        for cred in cls.cred_list:
            if cred.account == account:
                return True
        return False            

    #Displaying credentials

    @classmethod
    def display_cred(cls):
        '''
        Displays all credentials
        '''
        return cls.cred_list

    #copy passwords


    @classmethod
    def copy_secretlock(cls, secretlock):
            find_account = Credentials.find_account(secretlock)
            pyperclip.copy(find_account.secretlock)    






    