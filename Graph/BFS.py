from collections import deque
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
queue=deque()
ans=[]
visited=[False]*n
queue.append(0)
ans.append(0)
visited[0]=True
while len(queue)!=0:
    front=queue.popleft()
    for i in adjList[front]:
        if not visited[i]:
            queue.append(i)
            ans.append(i)
            visited[i]=True
print(ans)


