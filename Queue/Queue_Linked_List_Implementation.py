class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data) 

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head:
            current_node = self.head
            self.head = current_node.next
            dequeued_element = current_node.data
            current_node.next = None
            return dequeued_element

        if self.head is None:
            self.tail = None
            return None


if __name__ == '__main__':

    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)

    dequeued_element = queue.dequeue()
    print("Dequeued element:", dequeued_element)  
    dequeued_element = queue.dequeue()
    print("Dequeued element:", dequeued_element) 

   
    queue.enqueue(50)
    queue.enqueue(60)

    dequeued_element = queue.dequeue()
    print("Dequeued element:", dequeued_element)  
    dequeued_element = queue.dequeue()
    print("Dequeued element:", dequeued_element)  
   
    dequeued_element = queue.dequeue()
    print("Dequeued element:", dequeued_element)  

    dequeued_element = queue.dequeue()
    print("Dequeued element:", dequeued_element) 
