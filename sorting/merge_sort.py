# Merge Sort - Divide and Conquer Algorithm
#Time Complexity-O(nlogn)
#SpaceComplexoty=O(n)
def Sorting(nums):
    n=len(nums)
    temp=[0]*n #Allocate Once
    def Merge_sort(left,right):
        if left>=right:
            return 
        mid=(left+right)//2
        Merge_sort(left,mid)
        Merge_sort(mid+1,right)
        merge(left,mid,right)
    def merge(left,mid,right):
        i=left
        j=mid+1
        k=left
        while i<=mid and j<=right:
            if nums[i]<=nums[j]:
                temp[k]=nums[i]
                i += 1
            else:
                temp[k]=nums[j]
                j += 1
            k += 1
        while i<=mid:
            temp[k]=nums[i]
            i += 1
            k += 1
        while j<=right:
            temp[k]=nums[j]
            j += 1
            k += 1
        #Copy Back to original array
        for idx in range(left,right+1):
            nums[idx]=temp[idx]
        #print(nums) - See each step
    Merge_sort(0,n-1)
    return nums
num=[5,3,4,2,1]
print(Sorting(num))