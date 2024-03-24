# This project helps determine if a string is "chaotic" or not. A string is considered chaotic if all characters of the string appear a different number of times. If chaotic, return "TOHRU". Else, return "ELMA".

# As an example, consider the string s = ‘abbccc’. The string s is chaotic since every character occurs a number of times distinct from every other character, {‘a’ : 1, ‘b’ : 2, ‘c’ : 3}. 
# However, the string ‘abcc’ is not chaotic because the characters ‘a’ and ‘b’ both appear the same number of times as each other, namely once. 
# Function Description: Write a function is_chaotic() that takes a parameter s and returns the string ‘TOHRU’ if s is valid; the string ‘ELMA’ otherwise. 
# Additional Constraints The string provided as parameter to the function is_chaotic() will only contain characters [a - z]. 
# Sample Test Cases:

# is_chaotic(‘aabbcd’) = 'ELMA'
# is_chaotic(‘aaaabbbccd’) = 'TOHRU'
# is_chaotic(‘abaacccdee’) = 'ELMA'

def is_chaotic(s):
    counter = {}
    for i in s:
        if i not in counter.keys():
            counter[i] = 0
        else:
            continue
    for j in s:
        counter[j] += 1
    
    unique_value = set(counter.values())
    if len(unique_value) == len(counter):
        return 'TOHRU'
    else:
        return 'ELMA'

print(is_chaotic('abaacccdee'))