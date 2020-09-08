import pyperclip
class Credentials:
    '''
    class that creates instaces of user accounts
    '''
    cred_list = []

#########Assign propety to credentil list#########
    def __init__(self, account , email , passlock):
    
        self.account = account
        self.email = email
        self.passlock = passlock


        #########save credentials##########

    def save_cred(self):
        '''
        self credentials in cred_list
        '''
        Credentials.cred_list.append(self)

        ############Delete credentils#########

    def delete_cred(self):
        '''
        delete credentials 
        '''
        Credentials.cred_list.remove(self)    

        ###########search for credentials#######

    @classmethod
    def find_account(cls, account):
        '''
        search for accounts
        '''
        for cred in cls.cred_list:
            if cred.account == account:
                return cred    

                ##############confirm credentials########

    @classmethod
    def cred_exists(cls, account):
        '''
        confirm a class actually exists
        '''
        for cred in cls.cred_list:
            if cred.account == account:
                return True
        return False            


        #################Display credentials################

    @classmethod
    def display_cred(cls):
        '''
        method that returns all credentials
        '''
        return cls.cred_list

    ##########copy passwoed############


    @classmethod
    def copy_passlock(cls, passlock):
            find_account = Credentials.find_account(passlock)
            pyperclip.copy(find_account.passlock)    






    