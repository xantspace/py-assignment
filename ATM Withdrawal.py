print('Welcome to XantBank Ltd')
customer_name = input('what is your name? ')


member = "Promise"
#password = input('What is your password? ')
passwords = "12345"

attempt = 0
while True:
    if  attempt >= 3:
        print('You have reached the maximum number of attempts')
        quit()

    print('Please enter your login details')

    username = input('Username: ').capitalize()
    password = input('Password: ')

    if username in member and password == passwords:
        print('You are logged in!')

    else:
        attempt = attempt + 1
        remaining = 3 - attempt
        print(f'You have  {remaining} attempts left.Try logging in again!')


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