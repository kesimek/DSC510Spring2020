def performCalculation(operator):
    while True:
        if operator == '*':
            break
        elif operator == '/':
            break
        elif operator == '+':
            break
        elif operator == '-':
            break
        else:
            print('Error.  Please enter a valid mathematical operation.')
            break
    while True:
        try:
            number1 = float(input('Enter the first number: '))
            break
        except ValueError:
            print('Invalid entry.  Please enter the first number.')
            continue
    while True:
        try:
            number2 = float(input('Enter the second number: '))
            if operator == '/':
                if number2 == 0:
                    print('Invalid entry.  Cannot divide by zero.')
                    continue
                else:
                    break
            else:
                break
        except ValueError:
            print('Invalid entry.  Please enter the second number.')
            continue
    if operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    elif operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2


def calculateAverage():
    quantity = int(input('How many values would you like to average? '))
    q = 0
    sum_num = 0
    while q < quantity:
        number = float(input('Enter the number:  '))
        sum_num = sum_num + number
        q = q + 1
    return(sum_num / quantity)


while True:
    calculation = input('What type of operation would you like to perform?\n'
                        '    Enter "1" for mathematical operation.\n'
                        '    Enter "2" to calculate the average of numbers.  ')
    if calculation == 1:
        operation = input('Please enter the mathematical operation you'
                          ' would like to perform as "*", "/", "+" or "-".')
        print(performCalculation(operation))

    elif calculation == 2:
        print(calculateAverage())

    while True:
        another = input('Enter "Y" to complete another '
                        'calculation or "N" to terminate the program.  ')
        if another == 'Y':
            continue
        elif another == 'N':
            break
        else:
            print('Invalid entry. Enter "Y" to complete another calculation '
                  'or "N" to terminate the program.\n')
