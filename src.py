def checkCustomerStatus():
    print("Are you an existing customer ? (y/n)")
    customerStatusFlag = input()
    if customerStatusFlag == 'y':
        print("Welcome back, customer")
    elif customerStatusFlag == 'n':
        print("Welcome, new customer")
    else:
        print("Invalid input")
        checkCustomerStatus()


print("Welcome to Shakthi Bank")
print()
checkCustomerStatus()