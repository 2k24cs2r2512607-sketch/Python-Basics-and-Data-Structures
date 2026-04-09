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
second=Node(10) 
third=Node(2)
head.next = second  
head.next.next = third 

newnode=Node(7)
newnode.next=head
head=newnode
 
traverse(head)