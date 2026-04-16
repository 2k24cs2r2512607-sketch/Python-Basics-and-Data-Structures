class DoublyLinkedlist:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
a=DoublyLinkedlist(9)
b=DoublyLinkedlist(2)
a.next=b.data
b.prev=a.data
print(b.next)