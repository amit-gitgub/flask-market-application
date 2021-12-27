from operator import itemgetter

lis = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

print(sorted(lis, key=itemgetter("age"), reverse=True))

liste = [2,3,1,6,4,5,7,7]
print(liste.count(7))
print("\n")
print(sorted(liste))


