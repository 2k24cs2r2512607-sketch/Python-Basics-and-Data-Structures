class Stack:
    def __init__(self):
        self.st=[]
    def push(self,x):
        self.st.append(x)
        return self.st
    def pop(self):
        if len(self.st)==0:
            return "Empty Stack"
        x=self.st[-1]
        self.st.pop()
        return x
    def top(self):
        return self.st[-1]
    def size(self):
        return len(self.st)
stk=Stack()
stk.push(1)
stk.push(3)
stk.push(4)
stk.push(6)
stk.pop()
stk.top()
print(stk.pop())
print(stk.top())
print(stk.size())

