
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
 


visited=[False]*n
def cycle(i,parent,adjList,visited):
    visited[i]=True
    for x in adjList[i]:
        if x==parent:
            continue
        if visited[x]:

            return True
        if cycle(x,i,adjList,visited):
            return True
    return False
cycle(0,-1,adjList,visited)
        