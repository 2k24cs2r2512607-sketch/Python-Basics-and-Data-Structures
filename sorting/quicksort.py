#Time Complexity - Average Case - O(nlogn)
#Space Complexity - Average Case - O(logn) - Due to recursive Call
#Time Complexity - Worst Case - O(n^n) - (if data is sorted in ascending or descending order)
#Space Complexity - Worst Case - O(n)
'''Quick Sort performance depends on how balanced the recursion tree is.
Balanced tree → fast
Skewed tree → slow
Pivot controls this balance.'''

 
def quick_sort(arr,start,end):
    if start >= end:
        return
    
    pivot = partition(arr,start,end)
    
    quick_sort(arr,start,pivot-1)
    quick_sort(arr,pivot+1,end)

def partition(arr,start,end):
    pos = start
    for i in range(start,end+1):
        if arr[i] <= arr[end]:
            arr[i],arr[pos] = arr[pos],arr[i]
            pos += 1
    return pos-1

arr = [6,5,4,3,2,1]
quick_sort(arr,0,len(arr)-1)
print(arr)