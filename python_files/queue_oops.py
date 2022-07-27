#!/usr/bin/python3

class Queue:
    def __init__(self,size):
        self.QUEUE = []
        self.size = size
        self.rear = None
        self.front = None

    def enqueue(self,element):
        if len(self.QUEUE)<self.size:
            self.QUEUE.append(element)
            print(element, ' is added to the Queue')
            self.rear = self.QUEUE[-1]
            self.front = self.QUEUE[0]
        else :
            print('Queue is full')

    def dequeue(self):
        if not self.QUEUE:
            print('QUEUE is empty')
        else :
            e = self.QUEUE.pop(0)
            print('Removed element : ',e)
            if not self.QUEUE:
                self.rear = None
                self.front = None
            else :
                self.rear = self.QUEUE[-1]
                self.front = self.QUEUE[0]

    def display(self):
        print(self.front,self.rear)
        print(self.QUEUE)


def main():
    queue = Queue(3)
    queue.display()
    queue.enqueue(10)
    queue.display()
    queue.enqueue(20)
    queue.display()
    queue.enqueue(30)
    queue.display()
    
    queue.dequeue()
    queue.display()
    queue.dequeue()
    queue.display()
    queue.dequeue()
    queue.display()
    queue.dequeue()
    queue.display()

if __name__ == '__main__':
	main()