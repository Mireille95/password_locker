import unittest # Importing the unittest module
import pyperclip



from user import User,Credential # Importing the contact class

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
        self.new_user = User("James","Muriuki","pawsd12") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"James")
        self.assertEqual(self.new_user.last_name,"Muriuki")
        self.assertEqual(self.new_user.password,"pawsd12")
        

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
            test_user = User("Test","user","0712345678") # new contact
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","0712345678") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)


    def test_find_user_by_first_name(self):
        '''
        test to check if we can find a user by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0712345678") # new user
        test_user.save_user()

        found_user = User.find_by_first_name("Test")

        self.assertEqual(found_user.password,test_user.password)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0712345678") # new contact
        test_user.save_user()

        user_exists = User.user_exist("Test")

        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)

    # def test_copy_password(self):
    #     '''
    #     Test to confirm that we are copying the password address from a found contact
    #     '''

    #     self.new_user.save_user()
    #     User.copy_password("0712345678")

    #     self.assertEqual(self.new_user.password,pyperclip.paste())



class TestCredentials(unittest.TestCase):
    '''
    test class that defines a test cases dor the credentials class behaviors
    
    Args: 
    unittest.TestCase: helps in creating test cases
    '''
    
    def  test_check_user(self):
        '''
        function to test whether the login in function checuser woks as expected
        '''

        self.new_user= User('Mimi','Ng\'ang\'a','pswd100')
        self.new_user.save_user()
        user2 = User('fanny','Ng\'ang\'a','pswd100')
        user2.save_user()
        
        for user in User.user_list:
            if user.first_name ==  user2.first_name and user.password == user2.password:
                current_user = user.first_name
        return current_user
        
        self.assertEqual(current_user,Credential.check_user(user2.first_name,user2.password))
    
    def setUp(self):

        '''
        function to create an account credentials beforre each test
        '''
        self.new_credential = Credential('Mireille','Facebook','Mireille_Uwase','pswd100')
        
    def test__init__(self):
        '''
		Test to if check the initialization/creation of credential instances is properly done
		'''
        
        self.assertEqual(self.new_credential.user_name,'Mireille')
        self.assertEqual(self.new_credential.site_name,'Facebook')
        self.assertEqual(self.new_credential.account_name,'Mireille_Uwase')
        self.assertEqual(self.new_credential.password,'pswd100')
        
    def test_save_credentials(self):
        
        '''
		Test to check if the new credential info is saved into the credentials list
		'''
        
        self.new_credential.save_credentials()
        
        twitter = Credential('Jane','Twitter','maryjoe','pswd100')
        twitter.save_credentials()
        self.assertEqual(len(Credential.credentials_list),2)
        
    def tearDown(self):
        
        '''
		Function to clear the credentials list after every test
		'''
        
        Credential.credentials_list = []
        User.users_list = []
        
    def test_display_credentials(self):
        
        '''
		Test to check if the display_credentials method, displays the correct credentials.
		'''
        
        self.new_credential.save_credentials()
        twitter = Credential('Jane','Twitter','maryjoe','pswd100')
        twitter.save_credentials()
        gmail = Credential('Jane','Gmail','maryjoe','pswd200')
        gmail.save_credentials()
        
        self.assertEqual(len(Credential.display_credentials(twitter.user_name)),2)
        
    def test_find_by_site_name(self):
        '''
		Test to check if the find_by_site_name method returns the correct credential
		'''
        
        self.new_credential.save_credentials()

        twitter = Credential('Jane','Twitter','maryjoe','pswd100')
        twitter.save_credentials()
        credential_exists = Credential.find_by_site_name('Twitter')
        self.assertEqual(credential_exists,twitter)
        
    # def test_copy_credential(self):
        
    #     '''
	# 	Test to check if the copy a credential method copies the correct credential
	# 	'''
        
    #     self.new_credential.save_credentials()
    #     twitter = Credential('Jane','Twitter','maryjoe','pswd100')
    #     twitter.save_credentials()
    #     find_credential = None
    #     for credential in Credential.user_credentials_list:
    #         find_credential =Credential.find_by_site_name(credential.site_name)
    #     return pyperclip.copy(find_credential.password)
        
    #     Credential.copy_credential(self.new_credential.site_name)
    #     self.assertEqual('pswd100',pyperclip.paste())
    #     print(pyperclip.paste())



if __name__ ==  '__main__':
    unittest.main()
   
    