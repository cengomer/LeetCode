def evaluate_postfix(expression):
    stack = []
    for element in expression.split(' '):   
        if element.isdigit():             
            stack.append(int(element))

        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if element == '+': stack.append(operand1 + operand2)
            elif element == '-': stack.append(operand1 - operand2)
            elif element == '*': stack.append(operand1 * operand2)
            elif element == '/': stack.append(operand1 / operand2)
    
    return stack[0]