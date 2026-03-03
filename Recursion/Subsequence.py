def subsequence(arr, index, n, ans, temp):
    if index == n:
        ans.append(temp.copy())   # Append a copy
        return
    
    # Not included
    subsequence(arr, index + 1, n, ans, temp)
    
    # Included
    temp.append(arr[index])
    subsequence(arr, index + 1, n, ans, temp)
    
    # Backtrack - Backtracking is needed to restore the list to its previous state after exploring one choice.
    temp.pop()

arr = [1, 2, 3]
ans = []
temp = []

subsequence(arr, 0, len(arr), ans, temp)
print(ans)