class Queue:
    def __init__(self, size):
        self.queue = [0] * size
        self.front = -1
        self.rear = -1
        self.size = size
    
    def enqueue(self,value):
        if self.rear >= self.size - 1:
            print("Queue Overflowed")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = value
        print(f"{value} is inserted")

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is Underflowed")
            return
        value = self.queue[self.front]
        self.front += 1
        print(f"{value} is dequeued")
        return value
    
    def peek(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflowed")
            return
        return self.queue[self.front]
    
    def is_empty(self):
        return self.front == -1 or self.front > self.rear
    

q = Queue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element:", q.peek())  # 10

q.dequeue()
print("Front element:", q.peek())  # 20
        
        