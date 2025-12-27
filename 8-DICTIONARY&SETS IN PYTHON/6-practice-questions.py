#EXAMPLE-1--->store following word meaning in python dictionary  --> table:"a piece of furniture", "list of facts & figures" cat:"a samll animal"

dictionary={
    "cat": "a samll animal",
    "table":["a piece of furniture","list of facts & figures"] # we can store the two different values of same keyword by storing it in the list.
}
print(dictionary)

#EXAMPLE-2--->You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.-->"python", "java", "C++", "python", "javascript" "java", "python", "java", "C++", "C"
subject={
    "python", "java", "C++", "python", "javascript" "java", "python", "java", "C++", "C"
}
print(subject) #--->as we know it count duplicate values omly once
print(len(subject)) #--->length is equal to the number of classrooms.