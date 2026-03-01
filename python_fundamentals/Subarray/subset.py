arr=[3,4,2,5]
subarray=[[]]
for x in arr:
    subarray += [s+[x] for s in subarray]
print(subarray)