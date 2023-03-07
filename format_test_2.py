#input
x = 1
y = 3
z = 4
#Math operations
sum = x+y+z
average = sum/3
minimum = min(x,y,z)
maximum = max(x,y,z)
#formatting
sum_formatted = "{0:.2f}".format(sum)
average_formatted = "{0:.2f}".format(average)
minimum_formatted = "{0:.2f}".format(minimum)
maximum_formatted = "{0:.2f}".format(maximum)
#output

print(f'the sum of x, y and z is {sum_formatted}' )
print(f'the average of x,y and z is {average_formatted}')
print(f'the minimum of x,y and z is {minimum_formatted}')
print(f'the maximum of x,y and z is {maximum_formatted}')