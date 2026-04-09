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
#deleting at index 2
k=2
for _ in range(k-1):
    curr=curr.next
curr.next=curr.next.next

 
traverse(head)
 
 
 