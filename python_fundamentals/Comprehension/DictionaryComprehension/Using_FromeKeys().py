# Python dictionary fromkeys() function returns the dictionary with key mapped
# and specific value. It creates a new dictionary from the given sequence with the specific value.
seq = {'a', 'b', 'c', 'd', 'e'}

# creating dict with default values as None
res_dict = dict.fromkeys(seq)

print("The newly created dict with None values : " + str(res_dict))

# creating dict with default values as 1
res_dict2 = dict.fromkeys(seq, 1)

print("The newly created dict with 1 as value : " + str(res_dict2))

# using the fromkeys() method that returns a dictionary with specific keys and values.
Dictionary=dict.fromkeys(range(5),True)
print(Dictionary)