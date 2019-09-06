
import pyperclip
import random
import string


global users_list 
class User:
	'''
	Class to create user accounts and save their information
	'''
	
	users_list = []
	def __init__(self,first_name,last_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		self.first_name = first_name
		self.last_name = last_name
		self.password = password

	def save_user(self):
		'''
		Function to save a newly created user instance
		'''
		User.users_list.append(self)

class Credential:
	'''
	Class to create  account credentials, generate passwords and save their information
	'''
	
	credentials_list =[]
	user_credentials_list = []

	@classmethod
	def check_user(cls,first_name,password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user
        
        
    
	def save_credentials(self):
		'''
		Function to save a newly created user instance
		'''
		# global users_list
		Credential.credentials_list.append(self)
	

	def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate an 8 character password for a credential
		'''
		gen_pass=''.join(random.choice(char) for _ in range(size))
		return gen_pass

	def __init__(self,user_name,site_name,account_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.user_name = user_name
		self.site_name = site_name
		self.account_name = account_name
		self.password = password


	@classmethod
	def display_credentials(cls,user_name):
		'''
		Class method to display the list of credentials saved
		'''
		user_credentials_list = []

		for credential in cls.credentials_list:
			if credential.user_name == user_name:
				user_credentials_list.append(credential)
		return user_credentials_list
				

	
	@classmethod
	def find_by_site_name(cls, site_name):
		'''
		Method that takes in a site_name and returns a credential that matches that site_name.
		'''
		for credential in cls.credentials_list:
			if credential.site_name == site_name:
				return credential

	@classmethod
	def copy_credential(cls,site_name):
		'''
		Class method that copies a credential's info after the credential's site name is entered
		'''
		find_credential = Credential.find_by_site_name(site_name)
		return pyperclip.copy(find_credential.password)



#     def delete_user(self):

#         '''
#         delete_user method deletes a saved user from the user_list
#         '''

#         User.user_list.remove(self)

#     # @classmethod
#     # def find_by_first_name(cls,first_name):
#     #     '''
#     #     Method that takes in a name and returns a contact that matches that name.

#     #     Args:
#     #         number: name to search for
#     #     Returns :
#     #         user of person that matches the name.
#     #     '''

#     #     for user in cls.user_list:
#     #         if user.first_name == first_name:
#     #             return user
#     # @classmethod
#     # def user_exist(cls,first_name,password):
#     #     '''
#     #     Method that checks if a user exists from the user list.
#     #     Args:
#     #         number: first_name to search if it exists
#     #     Returns :
#     #         Boolean: True or false depending if the user exists
#     #     '''
#     #     for user in cls.user_list:
#     #         if user.first_name == first_name and user.password == password:
#     #                 return True

#     #     return False
#     # @classmethod
#     # def display_users(cls):
#     #     '''
#     #     method that returns the user list
#     #     '''
#     #     return cls.user_list

#     # @classmethod
#     # def copy_password(cls,first_name):
#     #     user_found = User.find_by_first_name(first_name)
#     #     pyperclip.copy(user_found.password)
      



# class Credential:
#     '''
#     class to create account credintials, generate password and save the info
#     '''
#     credentials_list =  []
#     user_credentials_list = []

#     @classmethod
#     def check_user(cls,first_name,password):
#         '''
#         method that checks if the name and passwword entered match
#         '''
#         current_user = ''
#         for user in User.user_list:
#             if (user.first_name == first_name and user.password == password):
#                 current_user = user.first_name
#         return current_user

#     def __init__(self,user_name,site_name,account_name,password):
#         '''
#         method to define the properties for each user object will hold
#         '''

#         # instance variable
#         self.user_name = user_name
#         self.site_name = site_name
#         self.account_name = account_name
#         self.password =  password

#     def save_credentials(self):
#         '''
#         function to save a new created user insatnce
#         '''

#         Credential.credentials_list.append(self)

#     def generate_password(size=8,char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
#         '''
#         function to generate an 8 character password
#         '''
#         gen_pass =''.join(random.choice(char) for _ in range(size))

#         return gen_pass

#     @classmethod
#     def display_credentials(cls,user_name):
#         '''
#         class method to display the list of credentials saved in 
#         '''

#         user_credentials_list = []
#         for credential in cls.credentials_list:
#             if credential.user_name == user_name:
#                 user_credentials_list.append(credential)
#         return user_credentials_list

#     def delete_credential(self):

#         '''
#         delete_user method deletes a saved user from the user_list
#         '''

#         Credential.credential_list.remove(self)


        
    # @classmethod
    # def find_by_site_name(cls, site_name):
    #     '''
    #     method that takes in a site_name and returns a credential that matches
    #     '''
    #     for credential in cls.credentials_list:
    #         if credential.site_name == site_name:
    #             return credential

    # @classmethod
    # def copy_credential(cls,site_name):
    #     '''
    #     class method that copies a credential
    #     '''
    #     find_credential = Credential.find_by_site_name(site_name)
    #     return pyperclip.copy(find_credential.password)

pass


     