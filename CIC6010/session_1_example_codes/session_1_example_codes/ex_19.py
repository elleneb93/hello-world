# Define the variables
sum = 0  # For storing the summarised numbers
n = input('How many number would you like to enter? ')

# Conversion
n = int(n)

# For loop
for i in range(n):
    number = input('Enter a number: ')
    number = float(number)
    sum = sum + number

# Calculate the average
print(sum / float(n))  # inline conversion
