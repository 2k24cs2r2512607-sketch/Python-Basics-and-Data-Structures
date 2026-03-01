keys=['apple','banana']
values=[2,3]
res={k:v for k,v in zip(keys,values)}
# also we can use it-
# res=dict(zip(keys,values))
print(res)
 
#  The zip() function in Python is used to combine two or more iterables (like lists, tuples, strings, dictionaries, etc.)
#  into a single iterator of tuples. Each tuple contains elements that share the same index across the input iterables.