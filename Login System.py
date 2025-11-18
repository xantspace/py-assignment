# ⿢ Login System (3 Attempts)
# Username = Promise
# Password = 12345
# User has only 3 tries.
# If wrong 3 times → print "Account locked".
# If correct → "Welcome back".

print('TechRise Login System')

#user_name = input('What is your username? ')
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
        break
    else:
        attempt = attempt + 1
        remaining = 3 - attempt
        print(f'You have  {remaining} attempts left.Try logging in again!')

