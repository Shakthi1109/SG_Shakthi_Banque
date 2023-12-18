def checkCustomerStatus():
    print("Are you an existing customer ? (y/n)")
    customerStatusFlag = input()
    if customerStatusFlag == 'y':
        print("Welcome back, customer")
        login()
    elif customerStatusFlag == 'n':
        print("Hello! new customer")
        createAccount()
    else:
        print("Invalid input")
        checkCustomerStatus()

def createAccount():
    print("Let's create an account for you")
    print("Enter your Surname")
    surname = input()
    print("Enter your name")
    name = input()
    print("Enter your email")
    email = input()
    print("create a password")
    password = input()
    print("Confirm your password")
    confirmPassword = input()
    if password == confirmPassword:
        print("Account created successfully")
        print("Would you like to login ? (y/n)")
        loginFlag = input()
        if loginFlag == 'y':
            login()
        elif loginFlag == 'n':
            print("Thank you for creating an account. See you soon !")
        else:
            print("Invalid input")
            createAccount()
    else:
        print("Password mismatch")
        createAccount()

def login():
    print("Enter your email")
    email = input()
    print("Enter your password")
    password = input()

print("Welcome to Shakthi Bank")
print()
checkCustomerStatus()