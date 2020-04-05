""" Katie Simek
    Assignment 4.1
    This program asks the user for their company name, length of fiber
    optic cable needed to be installed and then uses a function to
    calculate the cost.
    There is a bulk discount for purchases over 100 feet.
    0-100 = $.87/foot
    101-250 = $.80/foot
    251-500 = $.70/foot
    501+ = $.50/foot
    The program prints a receipt for the user.
"""

print('Hello, welcome to the fiber optic cable installation '
      'cost estimater.')

company = input('Please enter your company name: ')
length = float(input('Enter the number of feet of fiber optic cable to'
               ' be installed: '))
def install_cost(length, cost):
    return float(cost*length)

if length <= 100:
    cost = 0.87
elif length > 100 and length <= 250:
    cost = 0.80
elif length > 250 and length <= 500:
    cost = 0.70
else:
    cost = 0.50

print()
print()
print('RECEIPT for:', company)
print('Number of feet of cable to be installed: ',length)
if length > 100:
    print('**A bulk discount has been applied to your per foot cost.**')
print('Calculated cost: ', length,' feet at',
      '${0:.2f}'.format(cost),' per foot')
print('Total cost of installation: ','${:,.2f}'.format(install_cost(length,cost)))