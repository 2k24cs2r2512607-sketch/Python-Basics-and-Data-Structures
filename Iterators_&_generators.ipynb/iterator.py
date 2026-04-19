items=iter(["Python","is","a","Language"])
print(next(items))
print(next(items))
print(next(items))
print(next(items))


'''
iter() converts the list into an iterator.
next() fetches values one by one.
It remembers its position and does not restart automatically.'''