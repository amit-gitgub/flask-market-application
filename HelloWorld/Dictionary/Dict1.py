
dict = {3: "Am", 1: "learning", 2: "python"}


dict[0] = "hello"
dict["value"] = 2,3,4
dict[1] = 'I am'


#print(f"printing dictionary {dict}")
print(dict["value"])
print(type(dict))

nested_d = {'Students': {'boys': 5, 'girls': 7},
            'Subjects': {'computer': 10, 'math': 6}}

print(nested_d.get('Subjects').get('math'))


