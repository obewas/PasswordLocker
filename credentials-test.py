import unittest
from Credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        initial setup before a test is run
        '''
        self.new_cred = Credentials("Yahoo", "obewas1202@gmail.com", "obewas1202")
    def tearDown(self):
        '''
        Resets a test after test run
        '''
        Credentials.cred_list = []

        #Test initialization

    def test_init(self):
        '''
        check if test instances initialize as expected
        '''
        self.assertEqual(self.new_cred.account, "Yahoo")
        self.assertEqual(self.new_cred.email, "obewas1202@gmail.com")
        self.assertEqual(self.new_cred.passlock, "obewas1202")

        #7th test - saving credentials

    def test_save_credentials(self):
        '''
        checking if credentials are saving
        '''  
        self.new_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),1)

        #8th test - saving multiple credentials

    def test_saving_multiple_creds(self):
        '''
        checking if users can store multiple credentials
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("Google", "obewas","obewas1202")
        test_cred.save_cred()
        self.assertEqual(len(Credentials.cred_list),2)

        #9th test - deleting credentials

    def test_delete_credentials(self):
        '''
        test if you can delete credentials test
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("Google", "obewas","obewas1202")
        test_cred.save_cred()
        self.new_cred.delete_cred()
        self.assertEqual(len(Credentials.cred_list), 1)


        #10th test - searching for credentials

    def test_search_for_cred(self):
        '''
        test if credentials can be searched for
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("Google", "obewas","obewas1202")
        test_cred.save_cred()
        find_cred= Credentials.find_account("Google")
        self.assertEqual(find_cred.account, test_cred.account)
        
        #11th confirming account credentials
    def test_confirm_cred_exists(self):
        '''
        confirm that credentials actually exists
        '''
        self.new_cred.save_cred()
        test_cred = Credentials("Google", "obewas","obewas1202")
        test_cred.save_cred()
        cred_exists = Credentials.cred_exists("Google")
        self.assertTrue(cred_exists)


        #12th - displaing account credentials

        
    def test_display_credentials(self):
        '''
        test if all credentials can be displayed
        '''
        self.assertEqual(Credentials.display_cred(), Credentials.cred_list)



        #13th test - copying password

    def test_copy_password(self):
        '''
        test whether generated password can be copied
        '''
        self.new_cred.save_cred()
        Credentials.copy_passlock("obewas1202")
        self.assertEqual(self.new_cred.passlock, pyperclip.paste())   