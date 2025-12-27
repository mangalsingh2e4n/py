students_progess= {
    "name": "Mangal Singh",
    "subjects-name":["Hindi","Telugu","Englisg","Maths","Science","Social"],
    "subjects-marks":[78,88,89,83,92,90]
    

}

#1- mydict.keys()---> returns all the keys.
students_progess.keys()
print(students_progess.keys())

#2- mydict.values()---> returns all the values.
students_progess.values()
print(students_progess.values())

#3- mydict.items()---> returns all the key:value pairs.
students_progess.items()
print(students_progess.items())

#4- mydict.get("key""")---> returns  the value according to entered key.
print(students_progess.get("subjects-name"))
#5- mydict.update(newdict)---> inserts the new specified items into the dictionaries.
students_progess.update({"GRADE": "A"})
print(students_progess)
students_progess.update({"father name":"Murari Singh"})
print(students_progess)