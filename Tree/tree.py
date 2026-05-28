class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
         
root=Node(5)
root.left=Node(10)
root.left.right=Node(2)
print(root.left.right.data)