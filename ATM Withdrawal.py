print('Welcome to XantBank Ltd')
customer_name = input('what is your name? ')
start_balance = 40000
print(start_balance)
amount = input("Enter your amount: ")
withdraw = int(amount) - start_balance

if int(amount) > start_balance:
    print("Insufficient Funds")
    print()
elif int(amount) <= 10:
    print('Invalid Amount')
else:
   print(f'Withdrawn ₦{amount}\n')
   start_balance -= int(amount)
   print(f'New Balance is {start_balance}')