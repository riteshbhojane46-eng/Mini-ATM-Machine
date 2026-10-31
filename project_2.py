# creating mini ATM Machine project

account = {
    "name":"Ritesh",
    "balance":50000,
    "pin":"1234",
    "type":"saving_account"
}

print("==== MINI ATM ====")
pin =input("Enter your pin :")
if pin == account["pin"]:
    while True:
        print("==== ATM MENU ====")
        print("1.CHECK BALANCE")
        print("2.DEPOSIT MONEY")
        print("3.WITHDRAW MONEY")
        print("4.ACCOUNT DETAILS")
        print("5.EXIT")
        choice = input("Enter your choice:")
        if choice == "1":
            print("Your balance is :",account["balance"])
        elif choice == "2":
            amount = int(input("Enter your amount:"))
            if amount > 0:
                account["balance"]=account["balance"] + amount
                print("Money Deposit Successfully")
                # print("Collect your cash.")
                print("New balance",account["balance"])
        elif choice == "3":
            amount = int(input("Enter your amount:"))
            if amount > 0:
                account["balance"]=account["balance"] - amount
                print("Please collect your cash")
                print("New balance",account["balance"])
        elif choice == "4":
            print("\nAccount name:",account["name"])
            print("\nAccount balance:",account["balance"])
            print("\nAccount type:",account["type"])
        elif choice == "5":
            print("Thank You")
            print("Visit Again")
            break
        else:
            print("Invalid Choice")

    else:
        print("Ivalid pin")
        print("Access Denied")
