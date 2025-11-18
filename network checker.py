# ⿦ Phone Network Checker
# Ask for number.
# If starts with 070/080 → MTN
# 081 → Airtel
# 090 → Glo
# Else → Unknown network

airtel = '081'
mtn = ['070', '080']
glo = '090'

user_network = input('Enter your network: ')
if user_network in mtn:
    print('This is MTN')
elif user_network in glo:
    print('This is GLO')
elif user_network in airtel:
    print('This is Airtel')
else:
    print('Please enter a valid network')

