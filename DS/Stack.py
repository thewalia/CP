class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def getSize(self):
        return len(self.stack)
    
    def isEmpty(self):
        return self.stack == []

# Driver Code
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.getSize())

print(f"Popped: {stack.pop()}")
print(f"Popped: {stack.pop()}")
print(stack.getSize())

print(stack.peek())
print(stack.getSize())