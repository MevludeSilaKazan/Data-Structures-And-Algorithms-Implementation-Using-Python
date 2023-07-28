class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BST():
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0


    def insert(self, data):
        new_node = TreeNode(data)
        if self.root == None:
            self.root = new_node
            self.number_of_nodes += 1
            return
        else:
            current_node = self.root
            while(current_node.left_child != new_node) and (current_node.right_child != new_node):
                if new_node.data > current_node.data:
                    if current_node.right_child == None:
                        current_node.right_child = new_node
                    else:
                        current_node = current_node.right_child
                elif new_node.data < current_node.data:
                    if current_node.left_child == None:
                        current_node.left_child = new_node
                    else:
                        current_node = current_node.left_child
            self.number_of_nodes += 1
            return 
        
    def search(self,data):
        if self.root == None:
            return "Tree Is Empty"
        else:
            current_node = self.root
            while True:
                if current_node == None:
                    return "Not Found"
                if current_node.data == data:
                    return "Found"
                elif current_node.data > data:
                    current_node = current_node.left_child
                elif current_node.data < data:
                    current_node = current_node.right_child


    def remove(self, data):
        if self.root == None: #Tree is empty
            return "Tree Is Empty"
        current_node = self.root
        parent_node = None
        while current_node!=None: #Traversing the tree to reach the desired node or the end of the tree
            if current_node.data > data:
                parent_node = current_node
                current_node = current_node.left_child
            elif current_node.data < data:
                parent_node = current_node
                current_node = current_node.right_child
            else: #Match is found. Different cases to be checked
                #Node has left child only
                if current_node.right_child == None:
                    if parent_node == None:
                        self.root = current_node.left_child
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left_child = current_node.left_child
                            return
                        else:
                            parent_node.right_child = current_node.left_child
                            return

                #Node has right child only
                elif current_node.left_child == None:
                    if parent_node == None:
                        self.root = current_node.right_child
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left_child = current_node.right_child
                            return
                        else:
                            parent_node.right_child = current_node.right_child
                            return

                #Node has neither left nor right child
                elif current_node.left_child == None and current_node.right_child == None:
                    if parent_node == None: #Node to be deleted is root
                        current_node = None
                        return
                    if parent_node.data > current_node.data:
                        parent_node.left_child = None
                        return
                    else:
                        parent_node.right_child = None
                        return

                #Node has both left and right child
                elif current_node.left_child != None and current_node.right_child != None:
                    del_node = current_node.right_child
                    del_node_parent = current_node.right_child
                    while del_node.left_child != None: #Loop to reach the leftmost node of the right subtree of the current node
                        del_node_parent = del_node
                        del_node = del_node.left_child
                    current_node.data = del_node.data #The value to be replaced is copied
                    if del_node == del_node_parent: #If the node to be deleted is the exact right child of the current node
                        current_node.right_child = del_node.right_child
                        return
                    if del_node.right_child == None: #If the leftmost node of the right subtree of the current node has no right subtree
                        del_node_parent.left_child = None
                        return
                    else: #If it has a right subtree, we simply link it to the parent of the del_node
                        del_node_parent.left_child = del_node.right_child
                        return
        return "Not Found"




binary_search_tree = BST()
binary_search_tree.insert(6)
binary_search_tree.insert(4)
binary_search_tree.insert(8)
binary_search_tree.insert(2)
binary_search_tree.insert(14)
binary_search_tree.insert(66)
binary_search_tree.insert(1)
binary_search_tree.insert(11)
'''
            6
        4       8
    2               14
1                11     66
'''

(binary_search_tree.remove(14))

'''
            6
        4       8
    2               66
1                11     
'''

binary_search_tree.remove(6)

'''
            8
        4      66
    2        11         
1                 
'''

binary_search_tree.remove(4)

'''
            8
        2      66
    1        11         
                 
'''

binary_search_tree.remove(8)

'''
            11
        2      66
    1                 
                 
'''

binary_search_tree.remove(2)

'''
            11
        1      66
                     
                 
'''
binary_search_tree.remove(1)

'''
            11
               66
                     
                 
'''

binary_search_tree.remove(11)
'''
           66
                
                     
'''
binary_search_tree.remove(66)
'''
           
                
'''

binary_search_tree.insert(10)
'''
        10


'''
print(binary_search_tree.root.data)
#10