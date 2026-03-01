# Insertion sort in decreasing order
a=[2,1,4,2,3]
for i in range(1,len(a),1):
    for j in range(i,0,-1):
        if a[j]>a[j-1]:
            a[j],a[j-1]=a[j-1],a[j]
        else:
            break
print(a)

