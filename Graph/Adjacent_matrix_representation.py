#For undirected graph

n=6#number of vertices
e=7#number of edges
edges=[(0,1), (0,3), (0,4), (1,2), (1,5), (2,4), (3,4)]  # edges
adjMatrix=[]
for i in range(n):
    adjMatrix.append([-1]*n)
for edge in edges:
    x=edge[0]
    y=edge[-1]
    adjMatrix[x][y]=1
    adjMatrix[y][x]=1
for i in adjMatrix:
    print(i)
