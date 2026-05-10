"""try:
    print("this gets Executed First")
except:
    print("this gets executed inly if there is an error")


try:
    x=1/0
    print(x)
    print("let's try one example")
except:
    print("Something bad happened")"""

"""try:
    num1=int(input("enter number 1:"))
    num2=int(input("enter number 2:"))
    result=num1/num2
    print(result)
except Exception as e: #excepiton is used to show actual error(built in function)
    print("The value entered is not correct")
    print(e)
print("The next line of code will be executed.")"""
"""try:
    num1=int(input("enter number 1:"))
    num2=int(input("enter number 2:"))
    result=num1/num2
except Exception as e:
    print("Error occured")#This happens only if it fails,Error occur
    print(e)
else:
    print(result)#This happens only if it succeeds(no error occur)
finally:
    print("This happens no matter what")"""
'''try:
    num1=int(input("enter number 1:"))
    num2=int(input("enter number 2:"))
    result=num1/num2
    print(res3ult)
except ZeroDivisionError as z:
    print("Error occured")#This happens only if it fails,Error occur
    print(z)
except NameError as n:
    print("Error occured")#This happens only if it fails,Error occur
    print(n)
else:
    print("code run successfully") 
finally:
    print("This happens no matter what")'''
'''try:
    num1=int(input("Enter integer 1:"))
    num2=int(input("Enter integer 2:"))
    result=num1/num2
except ZeroDivisionError as z:
    print("Error Occurred")
    print(z)
except ValueError as u:
    print("Both values must be integer")
    print(u)
else:
    print(result)'''
# write a program to access a element in a list and handles both index error and value error seperately
try:
    list1=[3,2,4,2,1]
    n=int(input("Enter index:"))
    try:
        print(list1[n])
    except IndexError as i:
        print("index out of range")
    else:
        print("No index error")
    finally:
        print("Index error handled")
except ValueError as v:
    print(v)
else:
    print("suc")
finally:
    print("Fd")



    



