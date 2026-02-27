def min_element(arr,index,size):
    if index==size-1:
        return arr[index]
    return min(arr[index],min_element(arr,index+1,size))
arr=[3,4,2,4,1,8]
print(min_element(arr,0,6))
                