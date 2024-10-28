class MinStack(object):

    def __init__(self):
        self.val = []
        self.min_stack = []

    def push(self, val):
        self.val.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

        

    def pop(self):
        if self.val.pop() == self.min_stack[-1]:
            self.min_stack.pop()

        
        

    def top(self):
        return self.val[-1]
        

    def getMin(self):
        return self.min_stack[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()