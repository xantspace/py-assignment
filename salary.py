print('SALARY CALCULATOR')

user_name = input('Enter your name: ')
salary = input('What is your salary? ₦')
bonus = input('what is your salary bonus? ₦')
tax = 0.05
gross = int(salary) - tax
net = int(salary) + int(bonus)
tax_rate = int(net) * tax
print(f'Your net is ₦{net}')
print(f'Your gross is {gross}')
print(f'Dear {user_name}, Your tax for the month is ₦{tax_rate}')

