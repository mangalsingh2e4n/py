#Nested dictionary means creating a new dictionary inside a old dictionary or same dictionary.
students_progess= {
    "name": "Mangal Singh",
    "subject-marks":{
        "HINDI":89,
        "TELUGU": 92,
        "ENGLISH": 73,
        "MATHS":85,
        "SCIENCE":77,
        "SOCIAL":89
    }

}

print(students_progess)
print(students_progess["subject-marks"])
print(students_progess["subject-marks"]["MATHS"])