class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.lenght = 0
    def push(self,x):

        self.lenght += 1
        if self.front is None:
            newnode=Node(x)
            self.front=newnode
            self.rear=newnode
            return
        else:
            newnode=Node(x)
            self.rear.next=newnode
            self.rear=newnode
            return
    def pop(self):
        if self.front == None:
            return "Empty Queue"
        self.lenght -= 1
        self.front = self.front.next
        if self.front == None:
            self.rear = None
    def getfront(self):
        if self.front == None:
            return "Empty Queue"
        return self.front.data
    def size(self):
        return self.lenght
queue=Queue()
queue.push(5)
queue.push(4)
queue.push(3)
queue.push(1)
print(queue.getfront())
queue.pop()
print(queue.getfront())
print(queue.size())
