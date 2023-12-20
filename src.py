from datetime import datetime

def instantiateCustomerDb():
    with open('customerDB.csv', 'w') as customerDB:
        customerDB.write("Surname,Name,Email,Password,Transactions")
        customerDB.close()

def checkCustomerStatus():
    customerStatusFlag = input("Are you an existing customer ? (y/n) : ")[:1].lower()
    if customerStatusFlag == 'y':
        print("Welcome back!")
        login() 
    elif customerStatusFlag == 'n':
        print("Hello! new customer")
        createAccount()
    else:
        print("Invalid input")
        checkCustomerStatus()

def createAccount():
    print("Let's create an account for you.\n")
    surname = input("Enter your Surname (MAX 50 Chars) : ")[:50]
    name = input("Enter your name (MAX 50 Chars) : ")[:50]
    email = input("Enter your email (MAX 50 Chars) : ")[:50]
    password = input("Create a password (MAX 50 Chars) : ")[:50]
    confirmPassword = input("Confirm your password : ")
    if password == confirmPassword:
        print("Account created successfully")
        firstTransaction = "Deposit - "+ str(datetime.now().strftime("%d/%m/%Y"))+ " - "+ str(0) + " - " + str(0)
        with open('customerDB.csv', 'a') as customerDB:
            customerDB.write("\n"+surname + "," + name + "," + email + "," + password + "," + firstTransaction )
        customerDB.close()
        checkCustomerStatus()
    else:
        print("Password mismatch. Try again\n")
        createAccount()

def login():
    email = input("Enter your email (MAX 50 Chars) : ")[:50]
    password = input("Create a password (MAX 50 Chars) : ")[:50]
    loginFlag = False
    try:

        with open('customerDB.csv', 'r') as file:
            lines = file.readlines()
            
            for line in lines:
                if email in line:
                    parts = line.split(',')
                    if email == parts[2]:
                        if password == parts[3]:
                            print("\n*****Login successful*****\n")
                            loginFlag = True
                            homePage(parts[1], parts[0], parts[2])
                        else:
                            print("\nInvalid password. Try again\n")
                            login()
            if not loginFlag:
                print("\nEmail not found. Please create an account or contact customer support.\n")
                    
        file.close()

    except FileNotFoundError:
        print("The file 'customerDB.csv' was not found.")
    except PermissionError:
        print("You don't have permission to read the file 'customerDB.csv'.")
    except Exception as e:
        print("An error occurred:", e)
  

def homePage(name, surname, email):
    print("\nWelcome "+ name +" "+ surname)
    print("\nWhat would you like to do today ?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Print Statement")
    print("4. Download Statement")
    print("5. Show Balance")
    print("6. Exit")
    option = input()[:1]
    if option == '1':
        deposit(name, surname, email)
    elif option == '2':
        withdraw(name, surname, email)
    elif option == '3':
        printStatement(name, surname, email)
    elif option == '4':
        downloadStatement(name, surname, email)
    elif option == '5':
        showBalance(name, surname, email)
    elif option == '6':
        print("\nThank you for banking with us. Have a nice day.\n")
        exit()
    else:
        print("\nInvalid input\n")
        homePage(name, surname, email)



             
def deposit(name, surname, email):
    amount = input("\nEnter the amount you would like to deposit : ")[:50]
    
    with open('customerDB.csv', 'r') as file:
        lines = file.readlines()

    with open('customerDB.csv', 'a') as customerDB:
        for line in lines:
            if email in line:
                parts = line.split(',')
                if email == parts[2]:
                    lastTransaction = parts[-1].strip()
                    balance = float(lastTransaction.split('-')[3].strip())
                    newBalance = balance + float(amount)
                    customerDB.write(", Deposit - "+ str(datetime.now().strftime("%d/%m/%Y"))+ " - "+ str(round(float(amount),2)) + " - " + str(round(float(newBalance),2)))
                    print("\n*****Deposit successful*****\n")
    
    customerDB.close()
    anotherTransaction(name, surname, email)

def withdraw(name, surname, email):
    print("\nEnter the amount you would like to withdraw: ")
    amount = input()[:50]
    
    with open('customerDB.csv', 'r') as file:
        lines = file.readlines()

    with open('customerDB.csv', 'a', encoding='utf-8') as customerDB:
        for line in lines:
            if email in line:
                parts = line.split(',')
                if email == parts[2]:
                    lastTransaction = parts[-1].strip()
                    balance = float(lastTransaction.split('-')[3].strip())
                    if balance < float(amount):
                        print("\nInsufficient balance\n")
                        withdraw(name, surname, email)
                    else:  
                        newBalance = balance - float(amount)
                        # Fix the line below to correct the formatting issue
                        customerDB.write(",Withdraw - " + str(datetime.now().strftime("%d/%m/%Y")) + " - " + str(round(float(amount), 2)) + " - " + str(round(float(newBalance), 2)))
                        print("\n*****Withdraw successful*****\n")
    
    anotherTransaction(name, surname, email)



def printStatement(name, surname, email):
    with open('customerDB.csv', 'r') as file:
        lines = file.readlines()

    for line in lines:
        if email in line:
            parts = line.split(',')
            if email == parts[2]:
                print("Name: "+ parts[1])
                print("Surname: "+ parts[0])
                print("Email: "+ parts[2])
                print("Transactions: ")
                for transaction in parts[4:]:
                    print(transaction.strip())
    print("\n*****End of Statement*****\n")
    anotherTransaction(name, surname, email)


def downloadStatement(name, surname, email):
    with open('customerDB.csv', 'r') as file:
        lines = file.readlines()

    for line in lines:
        if email in line:
            parts = line.split(',')
            if email == parts[2]:
                filename= parts[1]+parts[0]+"_statement.txt"
                with open(filename, 'w') as file:
                    file.write(f"Name: {parts[1]}\nSurname: {parts[0]}\nEmail: {parts[2]}\nTransactions:\nOperation - Date - Amount - Balance\n")
                    for transaction in parts[4:]:
                        file.write(transaction.strip()  + "\n")
                    file.write("\n*****End of Statement*****\n")
                    file.close()
                    print("\n*****Statement downloaded successfully*****\n")
    
    anotherTransaction(name, surname, email)

def showBalance(name, surname, email):

    with open('customerDB.csv', 'r') as file:
        lines = file.readlines()

        for line in lines:
            if email in line:
                parts = line.split(',')
                if email == parts[2]:
                    lastTransaction = parts[-1].strip()
                    balance = round(float(lastTransaction.split('-')[3].strip()),2)
                    print("Your balance is: "+ str(balance))

    anotherTransaction(name, surname, email)
    

def anotherTransaction(name, surname, email):                
    transactionFlag = input("\nWould you like to do another transaction ? (y/n) : ")[:1].lower()
    if transactionFlag == 'y':
        homePage(name, surname, email)
    elif transactionFlag == 'n':
        print("\nThank you for banking with us. Have a nice day\n")
        exit()
    else:
        print("Invalid input")
        anotherTransaction(name, surname, email)


if __name__ == "__main__":
    print("\n########################")
    print(" Welcome to Shakthi Bank")
    print("########################\n")
    instantiateCustomerDb()
    checkCustomerStatus()