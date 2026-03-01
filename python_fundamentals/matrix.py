row=int(input("Enter row:"))
col=int(input("Enter column:"))
matrix=[]
print("Enter Element of matrix: ")
for i in range(row):
    rows=[] #For each row, you create a new empty list rows. This list will store the numbers of that row
    for j in range(col):
        rows.append(int(input())) #Python takes an input,Converts it to an integer,Adds it to the current row list
    matrix.append(rows)
print("\n2D matrix is:")
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()