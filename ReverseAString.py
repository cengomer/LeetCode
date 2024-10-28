def reverse_strng(input_str):
    stack = list(input_str)
    result = ''

    while len(stack):
        result += stack.pop()
    return result