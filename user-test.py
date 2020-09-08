import unittest
from User import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("John","Paul")

    def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        User.userList = []

        #2nd test

    def test__init(self):
        '''
        check if class is initialiazing as expected
        '''
        self.assertEqual(self.new_user.username, "John")
        self.assertEqual(self.new_user.password, "obewas1202@gmail.com")


    def test_saveUser(self):
        '''
        check whether the user information can be saved 
        in the user list
        '''
        self.new_user.saveUser()
        self.assertEqual(len(User.userList), 1)

        #3rd test - adding  multiple users

    def test_add_mutliple_users(self):
        '''
        check whether you can store more than one user
        '''
        self.new_user.saveUser()
        test_user = User("Tony", "Tryne")
        test_user.saveUser()
        self.assertEqual(len(User.userList), 2)

        #4th test - Deleting user

    def test_delUser(self):
        '''
        check whether one can delete a user account
        '''
        self.new_user.saveUser()
        test_user = User("Tony", "Tryne")
        test_user.saveUser()
        self.new_user.delUser()
        self.assertEqual(len(User.userList), 1)


    #5th test

    def test_search_by_name(self):
        '''
        find a user using name
        '''
        self.new_user.saveUser()
        test_user = User("Tony", "Tryne")
        test_user.saveUser()
        found_user = User.search_by_name("Tryne")
        self.assertEqual(found_user, self.new_user.username)

    def test_display_users(self):
        """Method that returns a list of all users"""
        self.assertEqual(User.display_users(),User.userList)
        


if __name__ == "__main__":
    unittest.main()
