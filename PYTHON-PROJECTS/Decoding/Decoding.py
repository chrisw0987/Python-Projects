def lexical_position(x):
        result = x
        alphabet_position = (result % 26) + ord('a')
        letter = chr(alphabet_position)
        return letter

def decode(ct):
    output = ""
    first_index = 0
    ascii_sum = 0
    for i in ct:
        if i.isalpha():
            if first_index == 0:                         #for first letter case
                x = (ord(i) + 59) % 26
                output += lexical_position(x)
                first_index += 1
                ascii_sum += ord(i)
            else:
                x = (ord(i) + ascii_sum)%26
                output += lexical_position(x)
                ascii_sum += ord(i)
        else:
            output += i
    return output
x = "this is a test."
print(decode(x))


def lexical_position(n):
    return chr(n + ord('a'))

def decode(ct):
    output = ""
    total_ascii = ord('a') 
    for index, char in enumerate(ct):
        if char.isalpha():
            if index == 0:
                x = (ord(char) - total_ascii) % 26
            else:
                x = (ord(char) + 7 - total_ascii) % 26
            char_decode = lexical_position(x)
            output += char_decode
            total_ascii += ord(char_decode)
        else:
            output += char
    return output

print(decode("tmny zk d pmxj."))
