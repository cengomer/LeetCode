def findSmallerPreceeding(numbers):
    result = [-1]
    stack = []
    for num in numbers:
        while stack and stack[-1] >= num:
            stack.pop()
        result.append(stack[-1] if stack else -1)
        stack.append(num)
    return result[1:]