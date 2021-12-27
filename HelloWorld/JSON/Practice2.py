import json

sampleJson = """[ 
   {
  "people" : [
    {
       "firstName": "Joe",
       "lastName": "Jackson",
       "gender": "male",
       "age": 28,
       "number": "7349282382"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "Emily",
       "lastName": "Jones",
       "gender": "female",
       "age": 24,
       "number": "456754675"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    }

  ]
}
]"""
data = []
data = json.loads(sampleJson)
print(data)
itemlist = [item for item in data]

print(itemlist)
