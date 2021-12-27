# Python3 code to demonstrate working of
# Convert key-values list to flat dictionary
# Using dict() + zip()
from itertools import product

# initializing dictionary
rr = {}
list1 = ['a', 'b', 'c']
list2 = ['1', '2', '3']
for i in range(0,3):

    rr.update(dict(zip(list1[i], list2[i])))
print(rr)
test_dict = {'month' : [1, 2, 3],
			'name' : ['Jan', 'Feb', 'March']}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

res = dict(zip(test_dict['name'], test_dict['month']))

# printing result
print("Flattened dictionary : " + str(res))
