#Katie Simek
#DSC510-T303
#Assignment 6.1
#Ask user for list of temperatures, determine the number of temperatures,
# determine the largest temperature, and the smallest temperature.

temperatures = []

while True:
    value = input('Enter a temperature or "done" to complete the list: ')
    if value == 'done':
        break
    else:
        try:
            temp = float(value)
            temperatures.append(temp)
        except ValueError:
            print('Invalid entry. Enter a temperature or "done" to complete the list.')
            continue

print()
print('The list contains ', len(temperatures), ' temperatures.')
print('The largest temperature is ', max(temperatures))
print('The smallest temperature is ', min(temperatures))