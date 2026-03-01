# Selection Sort 
# Selection Sort is a simple comparison-based sorting algorithm. 
# It works by repeatedly finding the smallest (or largest) element, 
# from the unsorted portion of the array and swapping it with the first unsorted element.
arr=[2,3,4,1,3,5]
for i in range(0,len(arr)-1,1):
    index=i
    for j in range(i+1,len(arr)):
        if arr[index] > arr[j]:
            index=j
    arr[index],arr[i]=arr[i],arr[index]
print(arr)