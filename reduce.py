from functools import reduce
x=[1,2,3,4]
sum_=reduce(lambda x,y:x+y,x)
print(sum_)