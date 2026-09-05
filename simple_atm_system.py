balance = 10000
def check_balance():
    print(f"Your Available Balance is {balance} ")
def debit():
    global balance
    a = float(input("Enter Withdraw Ammount: "))
    if a > balance:
        print("Insufficient balance!")
    else:
        print(f"{a} debited from your Account")
        balance= balance - a
        print(f"Your Available Balance is {balance} ")
def credit():
    global balance
    a = float(input("Enter deposit Ammount: "))
    print(f"{a} credited in your Account")
    balance= balance + a
    print(f"Your Available Balance is {balance} ")
print("Welcome to our ATM")
while True:
    print("\n1. Check balance\n2. Debit\n3. Credit\n4. Exit")
    c=int(input("\nChoose option(1-4): "))
    if c ==1:
        check_balance()
    elif c==2:
        debit()
    elif c== 3:
        credit()
    elif c ==4:
        print("THANKS FOR USING ATM")
        break
    else:
        print("Invalid option")



    