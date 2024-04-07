# To convert the provided for loop into a while loop we first
# must declare a variable i and assign it to 1 as the provided range()
# functions first step will begin at the int 1.
i = 1

# By converting the provided for loop into a while loop we declare
# that the while loop is ran as long as i is greater than 0 and less 
# than 10. i.e. will only run if i is equal to the ranges between 1 & 9.
while i > 0 and i < 10:
    # The print function will run on each iteration of the loop.
    print(i, i*i)

    # Using the += Assignment operator offered by python;
    # i will be assigned to the outcome of i + 1
    # https://www.w3schools.com/python/python_operators.asp
    i+=1
