from datetime import datetime

def instantiateCustomerDb():
    with open('customerDB.csv', 'w') as customerDB:
        customerDB.write("Surname,Name,Email,Password,Transactions")
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
        with open('customerDB.csv', 'a') as customerDB:
            customerDB.write("\n"+surname + "," + name + "," + email + "," + password + "," + "Deposit - "+ str(datetime.now().strftime("%d/%m/%Y"))+ " - "+ str(0) + " - " + str(0))
        customerDB.close()
        checkCustomerStatus()
    else:
        print("Password mismatch")
        createAccount()

def login():
    print("Enter your email")
    email = input()
    print("Enter your password")
    password = input()
    loginFlag = False
    try:

        # Read the file content into memory
        with open('customerDB.csv', 'r') as file:
            lines = file.readlines()
            
            for line in lines:
                if email in line:
                    parts = line.split(',')
                
                    if email == parts[2]:
                        if password == parts[3]:
                            print("Login successful")
                            loginFlag = True
                            homePage(parts[1], parts[0], parts[2])
                        else:
                            print("Invalid password")
                            login()
            if not loginFlag:
                print("Email not found. Please create an account or contact customer support")
                    
        file.close()

    except FileNotFoundError:
        print("The file 'customerDB.csv' was not found.")
    except PermissionError:
        print("You don't have permission to read the file 'customerDB.csv'.")
    except Exception as e:
        print("An error occurred:", e)
  

def homePage(name, surname, email):
    print("Welcome "+ name +" "+ surname)
    print("What would you like to do today ?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Print Statement")
    print("4. Exit")
    option = input()
    if option == '1':
        deposit(name, surname, email)
    elif option == '2':
        withdraw()
    elif option == '3':
        printStatement()
    elif option == '4':
        exit()
    else:
        print("Invalid input")
        homePage()


             
def deposit(name, surname, email):
    print("Enter the amount you would like to deposit")
    amount = input()
    
    # Read the file content into memory
    with open('customerDB.csv', 'r') as file:
        lines = file.readlines()

    # Iterate through the lines and update the balance if email is found
    with open('customerDB.csv', 'a') as customerDB:
        for line in lines:
            if email in line:
                parts = line.split(',')
                if email == parts[2]:
                    lastTransaction = parts[-1].strip()
                    balance = float(lastTransaction.split('-')[3].strip())
                    newBalance = balance + float(amount)
                    customerDB.write(", Deposit - "+ str(datetime.now().strftime("%d/%m/%Y"))+ " - "+ str(amount) + " - " + str(newBalance))
                    print("Deposit successful")
    
    customerDB.close()
    anotherTransaction(name, surname, email)


def anotherTransaction(name, surname, email):
    print("Would you like to do another transaction ? (y/n)")                
    transactionFlag = input()
    if transactionFlag == 'y':
        homePage(name, surname, email)
    elif transactionFlag == 'n':
        print("Thank you for banking with us. Have a nice day")
        exit()
    else:
        print("Invalid input")
        anotherTransaction(name, surname, email)


if __name__ == "__main__":
    print("Welcome to Shakthi Bank")
    print()
    instantiateCustomerDb()
    checkCustomerStatus()