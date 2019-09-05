import pyperclip
class User:
    """
    Class that generates new instances of users.
    """

    user_list = [] # Empty contact list

    def __init__(self,first_name,last_name,password):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
       

    def save_contact(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_first_name(cls,first_name):
        '''
        Method that takes in a name and returns a contact that matches that name.

        Args:
            number: name to search for
        Returns :
            user of person that matches the name.
        '''

        for user in cls.user_list:
            if user.first_name == first_name:
                return user
    @classmethod
    def user_exist(cls,number):
        '''
        Method that checks if a user exists from the user list.
        Args:
            number: first_name to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.first_name == first_name:
                    return True

        return False
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def copy_password(cls,first_name):
        user_found = User.find_by_first_name)
        pyperclip.copy(user_found.password)
  
pass


     