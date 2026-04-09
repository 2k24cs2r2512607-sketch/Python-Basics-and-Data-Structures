class Node:
    def __init__(self, data):
        self.data = data   
        self.next = None 
def traverse(head):
    curr = head
    while curr!=None:
        print(curr.data,end=" ")
        curr= curr.next

head=Node(5) 
curr=head       
second=Node(10) 
third=Node(2)
four=Node(8)
head.next = second  
head.next.next = third 
head.next.next.next=four

#Let suppose we want to insert at kth index
k=2
newNode=Node(25)
for i in range(k-1):
    curr=curr.next
newNode.next=curr.next
curr.next=newNode

traverse(head)
 
 