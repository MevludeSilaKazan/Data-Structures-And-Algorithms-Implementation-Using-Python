# nstead of creating a stack from scratch each time, 
#we can leverage the LifoQueue class from Python's queue module. 
#LifoQueue behaves like a stack. This is not to be confused with queues, 
#a different type of data structure. After importing queue, 
#we can create a new LifoQueue with a maxsize. If maxsize is zero, 
#the stack will be infinite. We can add elements using the put method, 
#get the size of the stack with the qsize method, pop elements from 
#the stack using get, which also returns the popped element, 
#and check if the stack is empty, among other functionalities.
import queue

# Initialize LIFO Queue
LIFOq = queue.LifoQueue(maxsize=0)


# Data Inserted as 5->9->1->7,
# same as Queue
LIFOq.put(5)
LIFOq.put(9)
LIFOq.put(1)
LIFOq.put(7)


# Displaying if the Queue is full
print("Full: ", LIFOq.full())

# Displaying size of queue
print("Size: ", LIFOq.qsize())

# Data will be accessed in the
# reverse order Reverse of that
# of Queue
print(LIFOq.get())
print(LIFOq.get())
print(LIFOq.get())

# Displaying if the queue is empty or not
print("Empty: ", LIFOq.empty())
