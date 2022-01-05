"""
This program is to authenticate the user provided userid and password against the set of dictionary

"""

def authenticateuser(user, dict):
    for key in userdictionary.keys():
        if user not in userdictionary.keys():
            print("Invalid user!")
            break
        if key == user:
            password= input("Valid User! Enter the password: ")
            while password != userdictionary[key]:
                password = input("Incorrect Password Try again: ")

            print(" You are authenticated!")


userdictionary = {'amit':'1234','shalabh':'234','vipul':'345'}
user = input(f" Enter the username: ")
authenticateuser(user, userdictionary)