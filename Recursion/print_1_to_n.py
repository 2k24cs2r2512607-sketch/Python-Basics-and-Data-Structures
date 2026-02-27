def recursion(start,n):
    if start==n:
        print(n)
        return 
    print(start)
    recursion(start+1,n)
n=7
recursion(1,n)