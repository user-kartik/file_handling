class Stack:
    def _init_(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else "Stack is empty"

    def peek(self):
        return self.stack[-1] if not self.is_empty() else "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0


stack = Stack()
stack.push(10)
stack.push(20)
print(stack.peek())  
print(stack.pop())   
print(stack.pop())   
print(stack.pop())
