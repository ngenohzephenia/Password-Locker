import random
import string
import pyperclip
class Credential:
    """
    Class that generates new instances of credentials.
    """

    credential_list = [] # Empty credential list

  
    def __init__(self,account,username, password):
        """
        method that defines user credential to be stored
        """
        self.account = account
        self.username = username
        self.password = password
        
    def save_credential(self):
        '''
        method that saves credential objects into application
        '''
        Credential.credential_list.append(self)
        
    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)
        
        
    @classmethod
    def find_credential(cls, account):
        """
        Method that takes in a account_name and returns a credential that matches that account_name.
        """
        for credential in cls.credential_list:
            if credential.account == account:
                return credential
            
    @classmethod
    def credential_exist(cls,name):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            name: name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.name == name:
                    return True

        return False       
 
 
    @classmethod
    def display_credential(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list 
    
    
    # def generatePassword(stringLength=8):
    #     """Generate a random password string of letters and digits and special characters"""
    #     password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
    #     return ''.join(random.choice(password) for i in range(stringLength))