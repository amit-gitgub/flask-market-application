list = [1, 2, 3, 4, 2, 3, 3, 20, 34, 22, 2, 77, 2, 3, 77, -17, 22, -17]
print(sum(list))
count = 0
new_list = []
for i in list:
    if list.count(i)>1:
        str1 = f"{i} occurred {list.count(i)} times"
        new_list.append(str1)


set1 = set(new_list)
#print(new_list)
for i in set1:
    print(i)








