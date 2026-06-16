
n=6#number of vertices
e=7#number of edges
edges=[(0,1), (0,3), (0,4), (1,2), (1,5), (2,4), (3,4)]  # edges
adjList=[]
for i in range(n):
    adjList.append([])
for edge in edges:
    x=edge[0]
    y=edge[-1]
    adjList[x].append(y)
    adjList[y].append(x)
stack=[]

ans=[]
visited=[False]*n
stack.append(0)
ans.append(0)
visited[0]=True
while len(stack)!=0:
    front=stack.pop()
    for i in adjList[front]:
        if not visited[i]:
            stack.append(i)
            ans.append(i)
            visited[i]=True
print(ans)


