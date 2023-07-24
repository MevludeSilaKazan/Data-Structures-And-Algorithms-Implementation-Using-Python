class Stack(object):
    def __init__(self, limit = 10):
        self.stack = []
        self.limit = limit
 
    # Function for pushing an element on to the stack (Yigina eleman ekleme)
    def push(self, data):
        if len(self.stack) >= self.limit:
            print('Stack Overflow')
        else:
            self.stack.append(data)
            
    # Function for popping the uppermost element (Yigindan eleman cikarma)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise Exception("Stack is empty. Cannot pop element.")
            
    # for peeking the top-most element of the stack (En ustteki elemani okuma/gozetleme)
    def peek(self):
        if len(self.stack) <= 0:
            print('Stack Underflow')
        else:
            return self.stack[-1]
        
    # Function to check if stack is empty (Yigin bos mu?)
    def isEmpty(self):
        return len(self.stack) == 0
    
    # Function for checking the size of stack (Yigin uzunlugu bulma)
    def size(self):
        return len(self.stack)

myStack = Stack()
for i in range(10):
    myStack.push(i)
print(myStack.stack)

myStack.pop()            
print(myStack.stack)
myStack.peek()         
myStack.isEmpty()
myStack.size()