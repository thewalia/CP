class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]
    
    def getLength(self):
        return len(self.queue)
    
    def isEmpty(self):
        return self.queue == []

# Driver Code
queue = Queue()

print(queue.isEmpty())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print(queue.peek())
print(queue.getLength())

queue.dequeue()
queue.dequeue()

print(queue.getLength())
print(queue.peek())
print(queue.isEmpty())