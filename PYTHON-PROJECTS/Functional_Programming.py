# Function Description: Write a function, winning_function() that takes three parameters as input: a list of integers and two functions that each take an integer as input and return a Boolean value. 
#winning_function() will then count how many times each function returns True
# when applied to the elements of the input list. The function that returns True the most is the
# winning function. Return the name of the winning function as a string. If both functions return
# True the same number of times, then return the string, ‘TIE’. For this problem, we will pass
# the even() and odd() functions to winning_function():

# def even(x):
# return x % 2 == 0

# def odd(x):
# return x % 2 == 1

# For example, if the input list is a = [2,3,4,5,6,8], then calling winning_function(a, even, odd) would return ‘even’ because the even()
# function will return True 4 times when applied to the elements of the list a, while the odd()
# function will only return True 3 times.

def even(x):
    return x % 2 == 0
def odd(x):
    return x % 2 == 1

def winning_function(a, even, odd):
    even_counter = 0
    odd_counter = 0

    for i in a:
        if even(i):
            even_counter += 1
        elif odd(i):
            odd_counter += 1

    if even_counter > odd_counter:
        return 'even'
    elif even_counter < odd_counter:
        return 'odd'
    else:
        return 'TIE'

print(winning_function([2,3,4,5,6,8],even, odd))