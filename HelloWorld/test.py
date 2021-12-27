list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]

#dic1 = {}
dic1 = {list1[i]: list2[i] for i in range(len(list2))}
print(dic1)
