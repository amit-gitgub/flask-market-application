import getpass

username = input("Enter the Username: ")
user_dict = {"amit": "123", "nikki": "456"}
lister = user_dict.get
print(lister)


for i in user_dict.keys():
    print("---user-----> " +username)
    print("---iiiii-----> " + i)

    if username == i:
        password = getpass.getpass("Enter your password: ")
        while password != user_dict.get(i):

            password = getpass.getpass(" Enter the password again.")
        print(f"correct password {password}")
        break

    else:
        print("Enter the correct username ")
        username = input("Enter the Username: ")






