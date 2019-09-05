#!/usr/bin/env python3.6
from user import User , Credential

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
def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Password ...")
                            p_password = input()


                            save_contacts(create_contact(f_name,l_name,p_password)) # create and save new contact.
                            print ('\n')
                            print(f"New Contact {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_users():
                                    print("Here is a list of all your users")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.first_name} {user.last_name} .....{contact.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any account saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_first_name = input()
                            if check_existing_users(search_first_name):
                                    search_user = find_user(search_first_name)
                                    print(f"{search_user.first_name} {search_user.last_name}")
                                    print('-' * 20)

                                    print(f"Password.......{search_contact.password}")
                                   
                            else:
                                    print("That user does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()