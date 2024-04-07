# The Range function takes a start int, followed by a stop int, and a step definition:
# https://docs.python.org/3/library/functions.html#func-range

#rangeList = list(range(10, 0,-1))
# https://docs.python.org/3/library/functions.html#func-list
# https://www.w3schools.com/python/ref_func_range.asp#gsc.tab=0

#rangeList.sort()
# https://www.w3schools.com/python/python_lists_sort.asp

# By setting i to 10, we set our start position to 10 without using range.
i = 10

# We should use s instead of 'sum' as 'sum' is a built in python function.
# https://docs.python.org/3/library/functions.html#sum
s = 0

# Converting the provided for loop to a while loop; we declare that the while loop
# Should only run while i is greater than the value 0.
while i > 0:
    # We add s to to i, then assign the value to s.
    s+=i

    #print(rangeList[i-1] == i)
    
    # We decrease our 'step' by one by subtracting i by 1, then assigning the value to i.
    # This is similar to how the stepping functionality works in the range() function.
    i-=1

# Because our while loop subtracts i by 1 if i is greater than 0, i becomes 0 when i equals 1
# Therefore if we wished to achieve the same output as the provided for loop, we must;
# assign +1 to i.
i += 1

# To prove the above is correct, we could create a list using the list() function and the range() as
# an argument;
#    rangeList = list(range(10, 0,-1))
#
# Then due to i decreasing from 10 we should reverse the list;
# rangeList.sort()
#
# Then in our while loop, we should write -1 (due to pythons zero indexing with lists, i.e. accessing position 10 would throw an error
# as it would not exist in our created list);
#    print(rangeList[i-1] == i)
#
# This would compare if the value provided by the range() function is the same as the loops iteration
# represented by i and will print True if correct.

# Finally to complete the conversion of the provided for loop we print the result;
print(i, s)
