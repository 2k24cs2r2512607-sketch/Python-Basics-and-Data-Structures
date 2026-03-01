a = [2, 4, 5]
subarrays = []

for start in range(len(a)):
    current = []
    for end in range(start, len(a)):
        current.append(a[end])
        subarrays.append(current.copy())
# copy() makes a separate duplicate of the original list so that changing one list does not affect the other.
print(subarrays)

