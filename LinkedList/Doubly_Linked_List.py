class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
        
class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        
    def insertAtBeginning(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            
 
    def insertAtEnd(self, data):
        new_node = Node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = new_node
        new_node.previous = temp
        
   
    def delete(self, data):
        temp = self.head
        if(temp.next != None):
            # if head node is to be deleted
            if(temp.data == data):
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    temp = temp.next
                if(temp.next):
                    # if element to be deleted is in between
                    temp.previous.next = temp.next
                    temp.next.previous = temp.previous
                    temp.next = None
                    temp.previous = None
                else:
                    # if element to be deleted is the last element
                    temp.previous.next = None
                    temp.previous = None
                return
        
        if (temp == None):
            return
        
    # for printing the contents of linked lists
    def printdll(self):
        temp = self.head
        while(temp != None):
            print(temp.data, end=' ')
            temp = temp.next
            
doubleLinkedList = DoublyLinkedList()
doubleLinkedList.insertAtBeginning(1)
doubleLinkedList.insertAtBeginning(2)
doubleLinkedList.insertAtEnd(3)
doubleLinkedList.insertAtBeginning(4)
doubleLinkedList.printdll()
doubleLinkedList.delete(2)
print()
doubleLinkedList.printdll()