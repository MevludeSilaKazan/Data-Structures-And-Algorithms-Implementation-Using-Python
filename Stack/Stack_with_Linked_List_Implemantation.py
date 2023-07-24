class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:

    def __init__(self):
        self.top = None

    
    def push(self,data):

        new_node = Node(data)
        if self.top:
            new_node.next=self.top

        self.top =new_node

    def pop(self):

        if self.top is None:
            return None

        else:
            popped_node =self.top
            self.top=self.top.next
            popped_node.next=None 
            return popped_node.data

    def peek(self):

        if self.top:
            return self.top.data
        else :
            return None


if __name__ == '__main__':
    # Örnek oluşturma
    my_stack = Stack()

    # Stack'e eleman eklemek için push işlemi
    my_stack.push(5)
    my_stack.push(10)
    my_stack.push(15)
    my_stack.push(21)
    my_stack.push(4)
    my_stack.push(83)
    my_stack.push(62)
    my_stack.push(35)



    # Peeking at the top element  (Peek işlemi ile en üstteki elemana bakma)
    top_element = my_stack.peek()
    print("Top element:", top_element)

    # Removing the top element with the pop operation (Pop işlemi ile en üstteki elemanı çıkarma)
    popped_element = my_stack.pop()
    print("Popped element:", popped_element)

    
  
    top_element = my_stack.peek()
    print("Top element:", top_element)

    
    popped_element = my_stack.pop()
    print("Popped element:", popped_element)


    # Display remaining top element after Pop and Peek (Pop ve Peek sonrası kalan üstteki elemanı görüntüleme)
    top_element = my_stack.peek()
    print("Top element after popping:", top_element)

    current_node = my_stack.top
    listforprint=[]
    print("my_stack elements:")
    while current_node:
        listforprint.append(current_node.data)
        current_node = current_node.next
    print(listforprint)





