class Queue(object):
    def __init__(self, limit = 10):
        self.queue = []
        self.head = None
        self.tail = None
        self.limit = limit
        self.size = 0

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # Function to check if queue is empty (Kuyruk bos mu?)
    def isEmpty(self):
        return self.size <= 0

    # Function to add an element of the queue (Kuyruga eleman eklemek)
    def enqueue(self, data):
        if self.size >= self.limit:
            return -1          # queue overflow
        else:
            self.queue.append(data)

        if self.head is None:
            self.head = self.tail = 0
        else:
            self.tail = self.size 

        self.size += 1

    # Function to pop an element from the front end of the queue (Kuyrugtan eleman cikarma)
    def dequeue(self):
        if self.isEmpty():
            return -1          # queue underflow
        else:
            self.queue.pop(0)
            self.size -= 1
            if self.size == 0:
                self.head = self.tail = 0
            else:
                self.tail = self.size - 1

    def getSize(self):
        return self.size

if __name__ == '__main__':
    myQueue = Queue()
    for i in range(10):
        myQueue.enqueue(i)
    print(myQueue)
    print('Queue Size:',myQueue.getSize())
    myQueue.dequeue()
    print(myQueue)
    print('Queue Size:',myQueue.getSize())