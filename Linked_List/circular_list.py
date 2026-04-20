# Simple implementation of a singly linked list in Python
class Node:
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.next = None  # Pointer to the next node  
 
head=Node(5)       # First node (head of the linked list)
second=Node(10)  
third=Node(34)   
head.next =second 
second.next=third  
third.next=head

curr=head
while True:
    print(curr.data)
    curr=curr.next
    if curr==head:
        break