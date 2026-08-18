mat=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(mat)):
    for j in range(i+1,len(mat[0])):
        mat[j][i],mat[i][j]=mat[i][j],mat[j][i]

print(mat)
row=len(mat)
low=0
high=len(mat[0])-1
while low<high:
    for i in range(row):
        mat[i][low],mat[i][high]=mat[i][high],mat[i][low]
    low += 1
    high -=1
print(mat)