def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

nums = [9,8,7,6,5,4,3,2,1]
target = 3
print(search(nums, target))
