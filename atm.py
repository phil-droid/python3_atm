print("")

print(".......................................Welcome to MOJO bank atm................................................\n")


user = {
    'pin': 1234,
    'balance':1000
}
def widthdraw_cash():
    while True:
        amount = int(input("Enter the amount of money to widthdraw: "))
        if amount > user['balance']:
            print("insufficient funds")
        else:
            user['balance'] = user['balance'] - amount
            print(f"{amount} pounds successfully widthdrawn your new balance is {user['balance']} pounds")
            print('')
            return False

def balance_enquiry():
    print(f"Total balance {user['balance']} pounds")
    print('')

def deposit_cash():
    while True:
        amount = int(input("Enter the amount to deposit: "))
        user['balance'] = user['balance'] + amount
        print(f"{amount} pounds successfully deposited your new balance is {user['balance']} pounds")
        print('')
        return False

is_quit = False

pin = int(input('Please enter your four digit pin: '))

if pin == user['pin']:
    while is_quit == False:
        print("select any option")
        print("1.Widthdraw Cash \n 2.Deposit cash\n 3.Balance Enquiry \n 4.Quit")

        query = int(input("Enter your choice: "))

        if query == 1:
            widthdraw_cash()
        elif query == 2:
            deposit_cash()
        elif query == 3:
            balance_enquiry()
        elif query == 4:
            is_quit = True
        else:
            print("Please enter a correct value shown")
else:
    print("Entered wrong pin")

print('................................THANK YOU FOR BANKING WITH MOJO BANK..............................................')
