# Create an empty stack 
stack = []

# push elements 
stack.append('A')
stack.append('B')
stack.append('C')

print(stack)

# pop an element 
topElement = stack.pop()
print(f"Popped Element: {topElement}")
print(stack)
newTopElement = stack[-1]
print(f"Top Element after Pop: {newTopElement}")
print(stack)
