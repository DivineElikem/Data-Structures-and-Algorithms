class stack():
    def __init__(self) -> None:
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            return "No element in stack"
        else:
            return self.stack.pop()
        
    def peek(self):
        if len(self.stack) == 0:
            return "No element in stack"
        else:
            return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def size(self):
        return len(self.stack)
    

#Use Case
stack1 = stack()
print("Pop: ", stack1.pop())
stack1.push(2)
stack1.push(5)
stack1.push(3)
stack1.push(7)
stack1.push(1)

print("Stack: ", stack1.stack)

print("Pop: ", stack1.pop())
print("After poping: ", stack1.stack)

print("Peek: ", stack1.peek())
print("After finding peek: ", stack1.stack)

print("Stack empty: ", stack1.is_empty())

print("Stack size: ", stack1.size())

