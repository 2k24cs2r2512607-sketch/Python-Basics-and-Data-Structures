class Node:
    def __init__(self,data):
        self.ans=[]
        self.data=data
        self.left=None
        self.right=None
    def preorder(self,root):
        if root is None:
            return self.ans
        
        self.preorder(root.left)
        self.preorder(root.right) 
        self.ans.append(root.data)   
root=Node(5)
root.left=Node(10)
root.left.right=Node(2)
root.right=Node(13)
 