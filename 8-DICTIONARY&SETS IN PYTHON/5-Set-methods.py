#---> SET METHODS
#set is mutable but the elements are immutable.
marks={23,23,18,24,25,17,16,17}
print(marks)

#1- set.add(el)--> add an element.
marks.add(45)
print(marks)

#2- set.remove(el)--> remove the element from the set.
marks.remove(23)
print(marks)

#3- set.clear() -->empties the set.
marks.clear()
print(marks)
#4- set.pop() -->remove an random value.
set={"mona","mina","maina","moon","mikasa","mona"}
print(set.pop())  #-->prints a random value from the set everytime.

#6- set.union()-->union set combines the two sets and gives us a new set.
set1={1,2,3,4,5,6,}
set2={0,9,8,7,7,66,55,33,221}
a=set1.union(set2)
print(a)

#7- set.intersection() --> creates the set with the common values from the both sets.
set3={33,44,55,66,78,89,87,65,21,31,32}
set4={33.44,55,31,32,99,87,90,93}
b=set2.intersection(set3)
print(b)
