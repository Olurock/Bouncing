
def isValid(s):
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

if __name__ == '__valid__':
    line = input(' ')
    if isValid(line):
        print('valid')
    else:
        print('not valid')


