def instantiateCustomerDb():
    with open('customerDB.csv', 'w') as customerDB:
        customerDB.write("Surname,Name,Email,Password,Balance\n")
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
    balance = 0
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
        writeToCustomerDB(surname, name, email, password, balance)
        checkCustomerStatus()
    else:
        print("Password mismatch")
        createAccount()

def login():
    print("Enter your email")
    email = input()
    print("Enter your password")
    password = input()
    try:
        with open('customerDB.csv', 'r') as customerDB:
            for line in customerDB:
                if email in line:
                    parts = line.split(',')
                    if password in parts[3]:
                        print("Login successful")
                        homePage(parts[1], parts[0], parts[2])
                    else:
                        print("Invalid password")
                        login()
                else:
                    print("Email not found. Please create an account or contact customer support")
                    createAccount()
    except FileNotFoundError:
        print("The file 'customerDB.csv' was not found.")
    except PermissionError:
        print("You don't have permission to read the file 'customerDB.csv'.")
    except Exception as e:
        print("An error occurred:", e)


def writeToCustomerDB(surname, name, email, password, balance):
    with open('customerDB.csv', 'a') as customerDB:
        customerDB.write(surname + "," + name + "," + email + "," + password + "," + str(balance) + "\n")
        customerDB.close()

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


#TO DO DESPOIT
                
def deposit(email):
    print("Enter the amount you would like to deposit")
    amount = input()
    
    # Read the file content into memory
    with open('customerDB.csv', 'r') as file:
        lines = file.readlines()

    # Iterate through the lines and update the balance if email is found
    found = False
    with open('customerDB.csv', 'w') as customerDB:
        for line in lines:
            if email in line:
                parts = line.split(',')
                balance = int(parts[4].strip())
                newBalance = balance + int(amount)
                parts[4] = str(newBalance) + "\n"
                updated_line = ','.join(parts)
                customerDB.write(updated_line)
                found = True
                print("Deposit successful")
            else:
                customerDB.write(line)

        if not found:
            print("Email not found")


if __name__ == "__main__":
    print("Welcome to Shakthi Bank")
    print()
    instantiateCustomerDb()
    checkCustomerStatus()