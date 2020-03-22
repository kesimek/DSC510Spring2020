""" Katie Simek
    Assignment 2.1
    This program asks the user for their company name, length of fiber
    optic cable needed to be installed and then computes the cost.
    The program prints a receipt for the user.
"""

print('Hello, welcome to the fiber optic cable installation '
      'cost estimater.')

company = input('Please enter your company name: ')
length = float(input('Enter the number of feet of fiber optic cable to'
               'be installed: '))
cost = length * 0.87    # the total cost per foot

print()
print()
print('RECEIPT for:')
print(company)
print('Number of feet of cable to be installed: ',length)
print('Calculated cost: ', length,' feet at $0.87 per foot')
print('The total cost of installation: $', cost)