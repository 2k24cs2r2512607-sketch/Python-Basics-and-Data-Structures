class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
        self.length=0
    def push(self,x):
        self.length += 1
        if self.top is None:
            self.top = Node(x)
            return
        else:
            newNode=Node(x)
            newNode.next=self.top
            self.top=newNode
    def pop(self):
        if self.top==None:
            return -1
        self.length -= 1
        x=self.top.data
        self.top=self.top.next
        return x
    def gettop(self):
        if self.top==None:
            return -1
        return self.top.data
    def size(self):
        return self.length
stk=Stack()
stk.push(1)
stk.push(3)
stk.push(4)
stk.push(6)
stk.pop()
stk.gettop()
print(stk.pop())
print(stk.gettop())
print(stk.size())