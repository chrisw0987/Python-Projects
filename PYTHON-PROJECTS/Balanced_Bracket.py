# A bracket is considered to be any one of: (, ), {, }, [, or ]

# A sequence of brackets is balanced if the following conditions are met:
# 1. It contains no unmatched brackets
# 2. The subset of brackets enclosed within the confines of a matched pair of brackets is also a
# matched pair of brackets.

# Function Description: Write a function is_balanced() that takes a string, where each
# character in the string is a bracket, and returns the Boolean value True if the brackets are
# balanced; otherwise, returns the Boolean value False

# Sample Test Case
# 1. is_balanced(‘{[()]}’) = True
# 2. is_balanced(‘{[(])}’) = False
# 3. is_balanced(‘{{[[(())]]}}’) = True

def is_balanced(s):
    stack = []
    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if (top=='(' and char != ')') or (top=='{' and char != '}') or (top=='[' and char != ']'):
                return False
    return len(stack) == 0

print(is_balanced("{{[[(())]]}}"))