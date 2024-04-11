# Developers: 
# Jayden Naylon
# https://github.com/JaydenWN
# A00150649
#
# Payal -
# A00135758
# -------------------------------
# This assigns the integer 1 to the variable i 
i=1

# This will create a while loop. It is not required to have whitespace
# within the conditional statement, however it could improve readability.
# Its important to note that the while loop will not do anything as the preceding
# lines are not indented.
while i<3:

# This will print the variable i to the terminal.
# As the variable i is set to the integer 1, it will print the integer 1.
# We could confirm that it is printing an integer by using print(type(i))
# https://www.geeksforgeeks.org/python-type-function/
print(i)

# This line will take the variable i, then add 1 to it, then will assign that outcome
# to the variable i.
# This would make the variable i now equal 2, as 1 + 1 = 2.
# An easier way to achieve this would be to use the addition assignment operator (+=)
# https://python-reference.readthedocs.io/en/latest/docs/operators/addition_assignment.html
# It seems that the original developer wished to increment i by 1, each time the loop ran,
# to avoid an infinite loop.
i=i+1

# As previously mentioned the original developer seemed to want to write a while loop,
# however did not properly indent their code.
# 'else:' must be preceded by a conditional statement or loop.
# Therefore writing 'else:' here will generate a syntax error, and break the code, as 
# i=i+1 is not a conditional statement nor loop.
else:

# This will print the integer 0 to the terminal, However since the previous line
# generates a syntax error, the line will never be executed.
print(0)


# After analysing the provided code, we show the corrected way of writing the provided program:
i = 1
while i < 3:
    print(i)
    i+=1
else:
    print(0)