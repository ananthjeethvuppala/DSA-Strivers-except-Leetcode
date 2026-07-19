class stack:
    def __init__(self, size):
        self.stack = [0] * size
        self.top = -1
        self.size = size
    def push(self, value):
        if self.top == self.size - 1:
            print('Stack is Overflowed')
            return
        self.top += 1
        self.stack[self.top] = value
        print(f"{value} is pushed into the stack")

    def pop(self):
        if self.top == -1:
            print('Staxk is Underflowed')
            return
        value = self.stack[self.top]
        self.top -= 1
        print(f"{value} poped")
        return value
    
    def peek(self):
        if self.top == -1:
            print("Stack is Empty")
            return
        return self.stack[self.top]
    
    def is_empty(self):
        self.top == -1

s = stack(5)

s.push(10)
s.push(20)
s.push(30)

print("Top element:", s.peek())  # 30

s.pop()
print("Top element:", s.peek())  # 20