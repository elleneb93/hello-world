# Define the variables
a = input('1st angle? ')
b = input('2nd angle? ')
c = input('3rd angle? ')

# Convert the variables
a = float(a)
b = float(b)
c = float(c)

# Print the basic arithmetics.
if a > 0 and b > 0 and c > 0:
    if a + b + c == 180:
        print('Possible triangle')
    else:
        print('The sum of the angles is not equals to 180.')
else:
    print('One of the angle (or more then one) is zero.')
