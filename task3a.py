# Original Author: Payal
#
# Contributors : Jayden Naylon
# https://github.com/JaydenWN
# -------------------------------

# Sets the integer 10 to the variable b.
b=10

# It would seem that the original developer is trying to write a while loop,
# that will only run while b is less than 10.
# However, the attempted while loop malfunctions due to incorrect declaration.
# i.e. The capital 'W', brackets and lack of semicolon will lead to a syntax error.
# Also this loop will never run due to b being initialised as 10.
# https://docs.python.org/3/reference/compound_stmts.html#while
While (b<10)

# It would seem that the original developer is trying to print 'Hello' to the terminal.
# The print function should be written with a lowercase p, and no trailing whitespace between the
# end of the function name and the first bracket.
# It also seems like the original developer was trying to include this in the aforementioned while loop,
# however they never indented the line.
# This would lead to a syntax error.
# https://docs.python.org/3/library/functions.html#print
Print (“Hello”)
       
# This line is programmed correctly, however it seems the original developer wished for this
# to be contained in the aforementioned while loop. This would take the current variable of b, add 1,
# then assign that value back to b.
# It should also be noted this would never run, due to the previous syntax errors, and the fact
# that b is already initialised as 10.
b+=1

# After analysing the provided code, we show the corrected way of writing the provided program:

b = 0

while b < 10:
    print("Hello")
    b+=1
