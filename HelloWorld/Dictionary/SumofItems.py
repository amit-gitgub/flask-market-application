my_d = {'gif': [2, 3, 4],
        'png': [4, 5, 3],
        'jpeg': [1, 2, 3]}

Unique_list = [elem for val in my_d.values() for elem in val]

print(Unique_list)

print(sum(Unique_list))
