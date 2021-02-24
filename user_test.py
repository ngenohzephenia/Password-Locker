import unittest # Importing the unittest module
from user import User # Importing the User class
from credential import Credential
class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("NgenohZephenia","51201003") # create user object
        
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []
        

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"NgenohZephenia")
        self.assertEqual(self.new_user.password,"51201003")
       
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)


    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()  
        test_user = User("Test","user") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Test","user") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)
            
            

            
class TestCredentials(unittest.TestCase):        
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''      
            
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("zef","twitter", "messi","Zefo2575")
            
     
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.name,"zef")
        self.assertEqual(self.new_credential.account,"twitter")
        self.assertEqual(self.new_credential.username,"messi")
        self.assertEqual(self.new_credential.password,"zefo2575")    
            
    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the  credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)
        
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []  

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("twitter","messi","zefo2575") # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)
        
        
        def test_delete_credential(self):
            '''
            test_delete_credential to test if we can delete a credential from credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("twitter","messi","zefo2575") # new credential
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting a credential object
            self.assertEqual(len(Credential.credential_list),1)
            

        def test_find_credential_by_username(self):
            '''
            test to check if we can find a credential by username and display information
            '''
            self.new_credential.save_credential()
            test_credential = Credential("twitter","messi","zefo2575") # new credential
            test_credential.save_credential()

            found_credential = Credential.find_by_username("messi")

            self.assertEqual(found_credential.username,test_credential.username)   


        def test_credential_exists(self):
            '''
            test to check if we can return a Boolean  if we cannot find the credential.
            '''
            self.new_credential.save_credential()
            test_credential = Credential("twitter","messi","zefo2575") # new credential
            test_credential.save_credential()

            credential_exists = Credential.credential_exist("messi")

            self.assertTrue(credential_exists)


        def test_display_all_credential(self):
            '''
            method that returns a list of all credential saved
            '''

            self.assertEqual(Credential.display_credentials(),Credential.credential_list)    

if __name__ == '__main__':
    unittest.main()

