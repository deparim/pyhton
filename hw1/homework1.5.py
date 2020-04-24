# 5

revenue = int(input('Please enter the revenue value in $: '))
expenses = int(input('Please enter the expenses value in $: '))
profit = revenue - expenses
profit_margin = profit / revenue

if revenue > expenses:
    print('The company made profit.')
    if True: print(f'The profit margin is: {profit_margin}')
    employees = int(input('Please enter the number of employees: '))
    profit_per_employee = profit / employees
    print(f'The profit per employee equals: {profit_per_employee} $ per person.')
else:
    print('The company bears expenses.')




