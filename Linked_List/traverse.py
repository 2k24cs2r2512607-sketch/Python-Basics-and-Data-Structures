class Node:
    def __init__(self, data):
        self.data = data   
        self.next = None
head=Node(5)        
second=Node(10) 
third=Node(2)
head.next = second  
head.next.next = third  
def traverse(head):
    curr = head
    while curr!=None:
        print(curr.data,end=" ")
        curr= curr.next
traverse(head)