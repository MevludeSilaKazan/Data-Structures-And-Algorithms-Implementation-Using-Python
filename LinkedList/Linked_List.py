class Node(object):

    # Initilazing the Node (Dugum temelini olusturalim.)

    def __init__(self, data):
        self.data = data
        self.next = None
        
    # To set data (Dugume deger atama)
    def setDataToNode(self, data):
        self.data = data
        
    # To get data of a particular node (Dugumden veri alma)
    def getDataFromNode(self):
        return self.data
    
    # To set next node (Bir sonraki dugumu ayarlama)
    def setNextNode(self, next):
        self.next = next
        
    # To get the next node (Bir sonraki dugume ulasma)
    def getNextNode(self):
        return self.next
    
class LinkedList(object):

    # Initilazing the linked list (Bagli liste temelini olusturalim.)
    def __init__(self):
        self.head = None
        self.tail = None
        
    # Printing the data in the linked list (Bagli listeyi yazdıralim.)
    def showLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next
            
    # Inserting the node at the beginning (Baslangicta dugum ekleyelim)
    def insertAtBeginning(self, data):

        new_node=Node(data)
        if self.head:
            new_node.next=self.head
            self.head= new_node
        else:
            self.head = new_node
            self.tail = new_node
        
    # inserting the node in between the linked list (after a specific node)
    def insertBetween(self, previousNode, data):
        if not previousNode:
            print("Previous node cannot be None.")
            return

        new_node = Node(data)

        # Check if previousNode is the tail node
        if previousNode == self.tail:
            self.tail = new_node

        new_node.next = previousNode.next
        previousNode.next = new_node

               


    def insertAtEnd(self, newElement):
    
        #1 & 2 & 3. allocate node, assign data element
        #          assign null to the next of new node
        newNode = Node(newElement)
        
        #4. Check the Linked List is empty or not,
        #   if empty make the new node as head 
        if(self.head == None):
            self.head = newNode
            self.tail = newNode
            return
        else:
            
            #5. Else, traverse to the last node
            temp = self.head
            while(temp.next != None):
                temp = temp.next
                
            #6. Change the next of last node to new node  
            temp.next = newNode


    # deleting an item based on data(or key)
    def delete(self, data):
        temp = self.head
        # if data/key is found in head node itself
        if (temp.next is not None):
            if(temp.data == data):
                self.head = temp.next
                temp = None
                return
            else:
                #  else search all the nodes
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    prev = temp          #save current node as previous so that we can go on to next node
                    temp = temp.next
                
                # node not found
                if temp == None:
                    return
                
                prev.next = temp.next
                return



            
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else :
                current_node = current_node.next
        return False
  
            
if __name__ == '__main__':
    List = LinkedList()
    List.head = Node(1)                   # create the head node
    node2 = Node(2)
    List.head.setNextNode(node2)           # head node's next --> node2
    node3 = Node(3)
    node2.setNextNode(node3)                # node2's next --> node3
    List.insertAtBeginning(4)                   # node4's next --> head-node --> node2 --> node3
    List.insertBetween(node2, 5)     # node2's next --> node5
    List.insertAtEnd(6)
    List.showLinkedList()
    print()
    List.delete(3)
    List.showLinkedList()
    print()
    print(List.search(1))