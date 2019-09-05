#!/usr/bin/env python3.6
from user import User ,Credential

def create_user(fname,lname,pswd):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,pswd)
    return new_user
def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
def find_user(first_name):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_first_name(first_name)
def check_existing_users(first_name):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(first_name)
def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def verify_user(first_name,password):
        '''
        function that verfiess the existance of the user before creating crede
        '''
        checking_user = Credential.check_user(first_name,password)

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
        function to save a new created credntial
        '''

        Credential.save_credentials(credential)

def display_credentials(user_name):
        '''
        function to display credenial saved by user
        '''
        return Credential.display_credentials(user_name)

def copy_credential():
        '''
        function to copy a credentials details to the clipborad
        '''
        return Credential.copy_credential(site_name)

def main():
    print("Welcome to your Password_locker App !!!")
#     user_name = input()

#     print(f"Hello {user_name}. what would you like to do?")
#     print('\n')

    while True:
                    print("Use these short codes : cc - create a new user, dc - display users, fc -find a user, ex -exit the user list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New User")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Password ...")
                            p_password = input()


                            save_users(create_user(f_name,l_name,p_password)) # create and save new contact.
                            print ('\n')
                            print(f"New User {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_users():
                                    print("Here is a list of all your users")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.first_name} {user.last_name} .....{user.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any account saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the name you want to search for")

                            search_first_name = input()
                            if check_existing_users(search_first_name):
                                    search_user = find_user(search_first_name)
                                    print(f"{search_user.first_name} {search_user.last_name}")
                                    print('-' * 20)

                                    print(f"Password.......{search_user.password}")
                                   
                            else:
                                    print("That user does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()