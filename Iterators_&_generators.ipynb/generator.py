def square_number(n):
    for i in range(1,n+1):
        yield i*i
a=square_number(6)
print(next(a))
print(next(a))
'''
yield sends one value at a time without ending the function.
Each next() call resumes the function from where it stopped.
Values are produced only when needed.'''


'''
iterator:
 How it is created - Using a class and implementing __iter__() and __next__()
 Memory usage	-Can be higher; needs more code to manage states	
  Local variables	No automatic saving of state	 '''

'''
Generator:
How it is created - Using a function with the yield keyword
Memory Usage- Very memory-efficient; produces values only when needed
Local variables	- Automatically saves state between yields'''