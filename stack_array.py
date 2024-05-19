class stack():
    def __init__(self) -> None:
        self.stack = []

    def push(self, element):
        self.stack.append(element)
        return

    def pop(self):
        if self.is_empty():
            return "No element in stack"
        return self.stack.pop()
        
    def peek(self):
        if self.is_empty():
            return "No element in stack"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    

#Usecase
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

print("current peek: ", stack1.peek())

print("Current stack is empty: ", stack1.is_empty())

print("Current stack size: ", stack1.size())

