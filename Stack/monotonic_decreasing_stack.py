array = [1, 2, 3, 6, 5, 7,6,8,5,4,6,3,2]
stack = []

for num in array:
    while stack and stack[-1] < num:
        stack.pop()
    stack.append(num)

print(stack)