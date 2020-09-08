from User import User 
from Credentials import Credentials
import random


def create_user(username, password):
    """Function to create a new user account"""
    new_user = User(username, password)
    return new_user

def save_users(user):
    """Function to save contacts"""
    user.saveUser()
def del_users(user):
    """Function to delete a contact"""
    user.delUser()
def save_credentials(credentials):
    """Function to save user credentials"""
    credentials.save_credentials

def display_users():
    return User.display_users()
def create_credentials(account, email, secretlock):
    '''
    method credentials details
    '''
    new_cred = Credentials(account, email, secretlock)
    return new_cred


def save_cred(cred):
    '''
    save credentials
    '''
    cred.save_cred()


def display_cred():
    '''
    method to display all the saved credentials
    '''
    return Credentials.display_cred()


def find_account(account):
    '''
    method to search for an account
    '''
    return Credentials.find_account(account)


def delete_cred(account):
    '''
    method to delete account
    '''
    account.delete_cred()


def main():
    # Beginning with user class first
    print("Welcome to Password Vault! Please enter your name:  ")
    name = input ()
    print(f"{name}, Sign up to continue")
    print('\n')
    print("-" * 80)
    print("Reply with  : cc - Sign Up,  ex -exit ")
    print("-" * 80)

    while True:
        short_code = input().lower()

        if short_code == 'cc':
            print("Creating account...")
            print("Key in these details:")
            print("Username: ")
            username = input()

            print("Password: ")
            password = input()

            save_users(create_user(username, password))
            print('\n')
            print(f"{name}'s Account information: ")
            print(f"Username: {username} , Password:{password}")
            print('\n')
            print(f"Logged in. Welcome {username}!")
            print("-" * 80)
            
            #working with credentials now###
            print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the contact list ")
            print("*" * 80)

        elif short_code == "ca":
            print("Enter account details: ")
            print("Enter your preferred account Name: ")
            account = input()
            print("Email: ")
            email = input()
        
            print("Would you like an auto generated password, yes or no?")
            if input()=="yes":
                letters= "ghijklmnopqrstuvwxyz0123456789FGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                how_many = len(letters)
                print("How many digits is your preferred password? ")
                print(f"Maximum digits {how_many}")
                lent = int(input())
                secretlock = "".join(random.sample(letters, lent))
                print(f"Your password has {lent} characters ")
                print(secretlock)
                save_cred(create_credentials(account, email, secretlock))
                print("Credentials saved! Enter 'da' to see account")
                print("*" * 80)
                print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the contact list ")
                print("*" * 80)
            elif input() == "no":
                print("Password: ")
                secretlock=input()
                save_cred(create_credentials(account, email, secretlock))
                print("Credentials saved! Enter 'da' to see account")
                print("*" * 80)
                print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, gp - generate a random password , ex -exit the contact list ")
                print("*" * 80)

                save_user(create_credentials(account, email,secretlock)) # create and save new secretlock.
                save_credentials(create_credentials(account, email,secretlock))
                print ('\n')
                print(f"New User {account} {email} created")
                print ('\n')


            else:
                print("i dont get it please use shortcode 'ca' and start again")

        elif short_code == "da":
            print(f"These are your credentials for {name}:")
            print("*" * 30)
            for cred in display_cred():
                print(f"{cred.account}\n {cred.email}\n {cred.secretlock}")
            else:
                print("*" * 30)
                print("If empty, you do not have any accounts saved")

        elif short_code == "fa":
            print("Key in  the account you are searching for (ie.'Facebook'): " )
            search_cred= input()
            if find_account(search_cred):
                search_acc = find_account(search_cred)
                print(f"{search_acc.account} {search_acc.email} { search_acc.secretlock}")
            else: print("This account does not exist")
            
        elif short_code == "gp":
                letters= "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                how_many = len(letters)
                print("How long would you like your password to be? ")
                print(f"p.s: Maximum length of password is {how_many}")
                lent = int(input())
                password = "".join(random.sample(letters, lent))
                print(f"Your password has {lent} characters ")
                print(password)
                
            

        elif short_code == 'ex':
            print("*"*30)
            print("logging out...")
            print('\n')
            print('\n')
            print("logged out")
            print("*"*30)
            break


        else:
            print("Invalid, please  use these short codes : ca - create a new account, da - display accounts, fa -find an account, de- delete account , gp - generate a random password , ex -logout")
if __name__ == '__main__':
    main()  