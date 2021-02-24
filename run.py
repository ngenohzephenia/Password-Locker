#!/usr/bin/env python3.6
import getpass
import string

from user import User
from credential import Credential

def create_user(username,password):
    '''
    function to create  new user
    '''
    new_user= User(username,password)
    return new_user
    
def save_user(user):
    '''
    function to save new user
    '''
    User.save_user()
        
def delete_user(user):
    '''
    function that deletes a user
    '''
    User.delete_user() 
        
def find_user(username):
    '''
    function that finds a user
    '''
    return User.find_by_username( username)
    
def check_existing_users(username):
    '''
    function that checks if a user exist
    '''
    return User.user_exist(username)
    
def display_all_users():
    '''
    function that returns all the saved users in the application
    '''
    return User.user.display_all_users()


def create_credential(self, account, username, password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential( account, username, password)
    return new_credential


def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()


def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    Credential.credential_list.remove(self)


def find_credential(username):
    '''
    Function that finds a credential by username and returns the credential
    '''
    return Credential.find_credential(username)


def check_existing_credential(username):
    '''
    Function that check if a credential exists with that username and return a Boolean
    '''
    return Credential.credential_exist(username)


def display_credential():
    '''
    Function that returns all the saved credential
    '''
    return Credential.display_credential()


def main():
    print("Hi! welcome to an application that help you manage your credentials")
    print("\n")
    print('please use the following short codes to perform any task you want ca = create account,' )
    short_code = input().lower()
    if short_code == 'ca':
        print('Create  your account details here')
        print('*' * 10)
        username = input('Enter  your Username: ')
        while True:
            print('use :  ep = to  enter your own password')
            password_choice = input().lower()
            if password_choice == 'ep':
                password = input('Enter Password: ')
                break
            else:
                print('You have entered a wrong short code. kindly try again')
                
            save_user(create_user(username, password))
        print('*' * 10)
        print(f'Welcome {username} to Password locker.Your new account  password is <--- {password} --->')
        print('*' * 10)
    while True:
        print('Use the following  short codes to manage  your credentials: \n cc = create credential, \n dc = display credentials,\n fc =     find credential  \n Dd = delete credential, \n  EX = exit application')
        short_code = input().lower()
        if short_code == 'cc':
            print('Enter your new credential details')
            print('*' * 10)
            account = input('Account Name : ')
            username1 = input('Username : ')
            while True:
                print('Use: ep =  enter  your own password?')
                password_choice = input().lower()
                if password_choice == 'ep':
                    password = input('Enter password : ')
                    break
                else:
                    print('You have entered a wrong  short code. kindly try again')
                print('*' * 10)
            save_credential(create_credential(account, username1, password,password))
            print('*' * 10)
            print(f'Your {account} account details has been saved in our application')
            print('*' * 10)
        elif short_code == 'dc':
            if display_credential():
                print('Your  credentials are as follows:')
                for account in display_credential():
                    print('-' * 10)
                    print(f'Username: {username1} \n Password: {password}')
                    print('-' * 10)
            else:
                print('*' * 10)
                print('You have no account. Please Create a new account')
                print('*' * 10)
        elif short_code == 'dd':
            print('Enter Account name to delete...')
            name = input('Acount Name : ')
            print('*' * 10)
            if find_credential(name):
                name_result = find_credential(name)
                name_result.delete_credential()
                print(f'Account {name} has been deleted successfully ')
                print('*' * 10)
            else:
                print('Incorrect account name.kindly type the correct again')
                print('*' * 10)
        elif short_code == 'fc':
            print('Enter Account Name To Search...')
            search = input('Account Name : ')
            print('*' * 10)
            if find_credential(search):
                search = find_credential(search)
                print(f'Account Name: {search} ')
                print('*' * 10)
            else:
                print(' the Credential  you are searching does not exist')
                print('*' * 10)
        elif short_code == 'ex':
            print('thanks for using our password-locker to keep your credentials')
            print('*' * 10)
            break
        else:
            print(' You have entered invalid Short code. Kindly  try again!')
            print('*' * 10)
if __name__ == '__main__':
    main()
