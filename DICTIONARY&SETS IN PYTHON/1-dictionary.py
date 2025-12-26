# DICTIONARIES--> 1.these stores the data in key-value pairs,these are mutable and dosent allow any duplicate keys.

students_data = {
    "name":"mona", #after each key value the other pair must be seperated by ,
    "age": 12, #integers shoul be inside the ""->it may e treated as string
    "class": 10,
    "subjects": ("hindi","telugu","english","maths","science","social"),
    "marks": [23,22,21,19,18,24],
     12: 1212, #it can take key values as integer,float,boolean
     3.99: 2.2,
     True: "value"
}

print(students_data)
print(type(students_data))



