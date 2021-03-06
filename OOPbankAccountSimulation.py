import time
class bankAccount:
    def __init__(self,name,password,balance):
        self.name = name
        self.password = password
        self.balance = balance
   
    def deposit(self,depositAmount):
        if depositAmount > 0:
            self.balance += depositAmount
            print("Request executed.")
            print("New Balance: " + str(self.balance))
        else:
            print("Your request cannot be executed.")
           
    def withdraw(self,withdrawAmount):
        pass_check = input("Enter your password to withdraw money: ")
        if pass_check == self.password:
            if withdrawAmount <= self.balance:
                self.balance -= withdrawAmount
                print("Request executed.")
                print("New Balance: " + str(self.balance))
            else:
                print("Your request cannot be executed.")
        else:
            print("The password you entered was incorrect.")
loop = 0 
while True:
    if loop == 0:
        print("Hello. Welcome to bank account simulation.")
        print("Let's create you an account, please enter your details here:")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        balance = int(input("Enter your initial deposit: "))
        print("Creating your account...")
        time.sleep(3)
        name = bankAccount(name,password,balance)
        print("Your account is all setup!")
        loop += 1

    print("You have 3 options")
    print("n = create new account")
    print("d = deposit")
    print("w = withdraw")
    print("e = exit simulation ")
    
    choice = input("What would you like to do? Enter an option: ")
    if choice == "n" or choice == "create new account":
        print("Let's create you a new account, please enter your details here:")
        newacc_name = input("Enter your name: ")
        newacc_password = input("Enter your password: ")
        newacc_balance = int(input("Enter your initial deposit: "))
        print("Creating your account...")
        time.sleep(3)
        name = bankAccount(newacc_name,newacc_password,newacc_balance)
        print("Your account is all setup!")
        loop += 1
     
    if choice == "d" or choice == "deposit":
        if loop >= 2:
            print("Which account would you like to use?")
            acc_choice = input("Please enter the name you used to register: ")
            deposit_amount = int(input("How much would you like to deposit: "))
            acc_choice.deposit(deposit_amount)
        else:
            deposit_amount = int(input("How much would you like to deposit: "))
            name.deposit(deposit_amount)
        
    if choice == "w" or choice == "withdraw":
        if loop >= 2:
            print("Which account would you like to use?")
            acc_choice = input("Please enter the name you used to register: ")
        withdraw_amount = int(input("How much would you like to withdraw: "))
        name.withdraw(withdraw_amount)
    if choice == "e" or choice == "exit":
        print("Thank you for trying out the simulation.")
        exit()
