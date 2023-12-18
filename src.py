def instantiateCustomerDb():
    with open('customerDB.csv', 'w') as customerDB:
        customerDB.write("\n Surname, Name, Email, Password\n")
        customerDB.close()

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
        writeToCustomerDB(surname, name, email, password)
        checkCustomerStatus()
    else:
        print("Password mismatch")
        createAccount()

def login():
    print("Enter your email")
    email = input()
    print("Enter your password")
    password = input()
    with open('customerDB.csv', 'r') as customerDB:
        for line in customerDB:
            if email in line:
                if password in line:
                    print("Login successful")
                    parts = line.split(',')
                    surname = parts[0].strip()
                    name = parts[1].strip()
                    email = parts[2].strip()
                    customerDB.close()
                    homePage(name, surname)
                else:
                    print("Incorrect password")
                    login()
            else:
                print("Email not found. Please create an account or contact customer support at 1800-000-000")
                checkCustomerStatus()

def writeToCustomerDB(surname, name, email, password):
    with open('customerDB.csv', 'a') as customerDB:
        customerDB.write(surname + "," + name + "," + email + "," + password + "\n")

def homePage(name, surname, email):
    print("Welcome "+ name +" "+ surname)
    print("What would you like to do today ?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Print Statement")
    print("4. Exit")
    option = input()
    if option == '1':
        deposit(email)
    elif option == '2':
        withdraw()
    elif option == '3':
        printStatement()
    elif option == '4':
        exit()
    else:
        print("Invalid input")
        homePage()

                



if __name__ == "__main__":
    print("Welcome to Shakthi Bank")
    print()
    instantiateCustomerDb()
    checkCustomerStatus()