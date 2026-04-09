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
head.next = second  
head.next.next = third 
 
last=Node(9)
while curr.next!=None:
    curr=curr.next
else:
    curr.next=last

traverse(head)
 
 