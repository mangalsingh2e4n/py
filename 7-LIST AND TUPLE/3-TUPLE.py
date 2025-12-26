#-->TUPLE= Its is an built in data type in python and it is immutable.They are stored as ==> tuple()
marks=(78,90,78,65,44,56,90,93,73)
print(type(marks)) #-->The type of the marks is tuple

#--.METHODS IN TUPLE ARE SIMILAR AS THE LIST

#1--> tup.index(element) returns the index of the entered element in the tuple.
print(marks.index(78))
print(marks.index(73))

#2--> tup.count(element): counts the total number of occurence
print(marks.count(78))
print(marks.count(73))



