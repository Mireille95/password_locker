#!/usr/bin/env python3.6

import pyperclip

from user import User ,Credential



def create_user(fname,lname,password):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,password)
    return new_user

def save_user(user):
    '''
    Function to save a user
    '''
    user.save_user()

def verify_user(first_name,password):
        '''
        function that verfiess the existance of the user before creating crede
        '''
        checking_user = Credential.check_user(first_name,password)
        return checking_user

def generate_password():
        '''
        function to generate a password automatically
        '''
        gen_pass = Credential.generate_password()
        return gen_pass

def create_credential(user_name,site_name,account_name,password):
        '''
        function to create a new credential
        '''
        new_credential = Credential(user_name,site_name,account_name,password)
        return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)


def display_credentials(user_name):
        '''
        function to display credenial saved by user
        '''
        return Credential.display_credentials(user_name)

def main():
	print(' ')
	print('---------------Welcome to Password Locker App--------------')
	while True:
		print(' ')
		
		print('Use these short_codes to access....: \n ca-Create an Account... \n li-Log In... \n dl-Delete... \n ex-Exit...')
		short_code = input('Enter choice: ').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'ca':
			
			
			print('To create a new account:')
			first_name = input('Enter your first name - ').strip()
			last_name = input('Enter your last name - ').strip()
			password = input('Enter your password - ').strip()
			save_user(create_user(first_name,last_name,password))
			print(" ")
			print(f'New Account Created for: {first_name} {last_name} using password: {password}')
		elif short_code == 'li':
			
			print(' ')
			print('To login, enter your account details:')
			user_name = input('Enter your first name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = verify_user(user_name,password)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}. Please choose an option to continue.')
				print(' ')
				while True:
					
					print('short_codes to access...: \n cc-Create a Credential... \n dc-Display Credentials... \n ex-Exit...')
					short_code = input('Enter a choice: ').lower().strip()
					
					if short_code == 'ex':
						print(" ")
						print(f'Goodbye {user_name}')
						break
					elif short_code == 'cc':
						print(' ')
						print('Enter your credential details:')
						site_name = input('Enter the site\'s name- ').strip()
						account_name = input('Enter your account\'s name - ').strip()
						while True:
							print(' ')
							
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							
							if psw_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'gp':
								password = generate_password()
								break
							elif psw_choice == 'ex':
								break
							else:
								print('Oops! Wrong option entered. Try again.')
						save_credential(create_credential(user_name,site_name,account_name,password))
						print(' ')
						print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if display_credentials(user_name):
							print('Here is a list of all your credentials')
							print(' ')
							for credential in display_credentials(user_name):
								print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any credentials saved yet")
					
			else: 
				print(' ')
				print('Oops! Wrong details entered. Try again or Create an Account.')		
		
		else:
			
			print(' ')
			print('Oops! Wrong option entered. Try again.')
				






if __name__ == '__main__':
	main()




