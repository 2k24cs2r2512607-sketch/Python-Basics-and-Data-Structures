# Bubble Sort
# It repeatedly compares adjacent elements in a list and swaps them if they are in the wrong order. 
# This process continues until the list is sorted. The algorithm derives its name from the way larger elements "bubble up" to their correct positions in each iteration.
arr=[1,2,3,4,5]
for i in range(len(arr)-2,-1,-1):
    seq=0
    for j in range(0,i+1,1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j] 
            seq=1
    if seq==0:
        break
print(arr) 