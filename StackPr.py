text_stack = []

text_stack.append("Hello, world!")
text_stack.append("Hello, CodeSignal")

print(text_stack)

def is_empty(stack):
    return len(stack) == 0

if not is_empty(text_stack):
    previous_text = text_stack.pop()
    print(text_stack)
    print(f'After "undo", the text is: {previous_text}')
else:
    print("Cannot perform undo operation,There are no historic changes.")