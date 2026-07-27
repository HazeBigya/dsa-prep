def valid_parentheses(s):
    stack = []
    closed_brackets = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    for char in s:
        if char not in closed_brackets:
            stack.append(char)
        else:
            if not stack or stack.pop() != closed_brackets[char]:
                return False
    return not stack

s = '{[]}'
print("The string is a valid parenthesis: ", valid_parentheses(s))