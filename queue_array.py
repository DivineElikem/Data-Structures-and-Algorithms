class queue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)
        return
    
    def dequeue(self):
        if self.is_empty():
            return "No element in queue"
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            return "No element in queue"
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    

#Usecase
queue1 = queue()
queue1.enqueue(3)
queue1.enqueue(5)
queue1.enqueue(7)
queue1.enqueue(2)
queue1.enqueue(4)

print("Queue: ", queue1.queue)

queue1.dequeue()
print("After dequeuing: ", queue1.queue)

print("Current peek: ", queue1.peek())

print("Current queue is empty: ", queue1.is_empty())

print("Size of current queue: ", queue1.size())