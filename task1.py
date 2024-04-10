# Developers: 
# Jayden Naylon
# https://github.com/JaydenWN
# A00150649
#
# Payal -
# A00135758
# -------------------------------

# 1 = = = = = = = = = =
print('= = = = Section 1 = = = =')

# We first must initialise a variable with the int value 1
i = 1

# As required, the while loop will run only when i is less than
# or equal to 10.
while i <= 10:
    # Using the print function will print the value of i each time the
    # loop is ran.
    print(i)

    # We then must use the += Assignment operator offered by python;
    # i will be assigned to the solution of i + 1
    # this will allow the loop to stop once i is greater than 10. i.e. 11.
    i+=1

# 2 = = = = = = = = = =
print('\n= = = = Section 2 = = = =')

# As required, using a for loop paired with the range() function, we can 
# skip each odd number by using the range() functions step functionality.
# https://www.w3schools.com/python/ref_func_range.asp#gsc.tab=0
for i in range(0,21,2):
    # As the example provided does not print the value 0,
    # we can use a if statement to ensure 0 isn't printed.
    if i > 0:
        print(i)

print('Additional Solution: ')

# Another solution would to be to use the modulo operator.
# Modulo returns the remainder of two expressions when divided.
# https://www.geeksforgeeks.org/what-is-a-modulo-operator-in-python/

for i in range(1,21):
    if i % 2 == 0:
        print(i)

# 3 = = = = = = = = = = =
print('\n= = = = Section 3 = = = =')

# To use a while loop as required, we would have to initialise a variable
# iterate with. So we initialise the variable with 1.
i = 1

# while i is less than or equal to 20, the loop will run.
# using the same modulo technique above we check if the divised variables
# carries a remainder, making it an 'uneven' number.
while i <= 20:
    if i % 2 == 1:
        print(i)
    i+=1

# 4 = = = = = = = = = = =
print('\n= = = = Section 4 = = = =')

# The final section of the task requires us to loop the equated sum using a
# for loop and the print function.

# First we declare the variable x, to iterate with later.
x = 1

# Declaring an empty list to append our values to.
numberList = []

# While the variable x is less than or equal to 10, we append the value x
# to our numberList.
# https://www.w3schools.com/python/ref_list_append.asp
while x <= 10:
    numberList.append(x)
    x+=1
# Using pythons built in sum() function we can add each value together at once.
# i.e. rather than writing 1 + 2 + 3 ... we can just use sum().
# then assign it to the variable numbers.
# https://www.w3schools.com/python/ref_func_sum.asp
numbers = sum(numberList)

# As the task requires us to use a for loop to print the equated value,
# we write a for loop.
# i.e. 'for the amount of numbers in the numberList we made, print
# the equated value'.
for n in numberList:
    print(numbers)