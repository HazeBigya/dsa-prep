def eval_rpn(tokens):
    operand = {"+", "-", "*", "/"}
    stack = []
    
    for token in tokens:
        if token in operand:
            a = stack.pop()
            b = stack.pop()
            if token == "+":
                stack.append(b + a)
            elif token == "-":
                stack.append(b -a)
            elif token == "*":
                stack.append(b * a)
            elif token == "/":
                stack.append(int(b / a))
        else:
            stack.append(int(token))
    print("Value of the expression =", stack.pop())
            
            
token = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
eval_rpn(token)