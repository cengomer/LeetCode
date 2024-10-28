class Solution(object):
    def isValid(self, s):
        stack = []
        parenthes_dict = {'(': ')', '[': ']', '{': '}'}
        
        for char in s:
            if char in parenthes_dict:  # If the character is an opening bracket
                stack.append(char)
            elif char in parenthes_dict.values():  # If the character is a closing bracket
                if not stack:  # If the stack is empty, no matching opening bracket
                    return False
                top_element = stack.pop()
                if parenthes_dict[top_element] != char:  # Check if the top of the stack matches the current closing bracket
                    return False
        
        return not stack  # If the stack is empty, all brackets are matched

"""
def are_brackets_balanced(input_str):
    brackets = set(["(", ")", "[", "]", "{", "}"])
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []

    for character in input_str:
        if character not in brackets:
            # Skipping non-bracket characters
            continue
        if character in open_par:
            stack.append(character)
        elif stack and character == bracket_map[stack[-1]]:
                stack.pop()
        else:
            return False
    return len(stack) == 0

"""