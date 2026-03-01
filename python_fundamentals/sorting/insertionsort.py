# Insetion Sort
# Insertion sort: It works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list.
a=[34,5,3,4,5,1]
for i in range(1,len(a),1):
    for j in range(i,0,-1):
        if a[j]<a[j-1]:
            a[j],a[j-1]=a[j-1],a[j]
        else:
            break
print(a)