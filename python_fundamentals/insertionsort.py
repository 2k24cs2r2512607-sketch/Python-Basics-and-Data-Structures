# Insertion sort in decreasing order
arr=[2,1,4,2,3]
for i in range(len(arr),0,1):
    for j in range(0,i,1):
        if arr[j] < arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
        else:
            break
print(arr)

