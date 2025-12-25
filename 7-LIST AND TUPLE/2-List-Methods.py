age_group=[32,35,21,39,67,78]
print(age_group)

#> 1- list.append(any value you want to add)-->it adds at the new value at the end of the list.
age_group.append(69)

# >2- list.sort()--> sorts the values in ascending order.
age_group.sort()
print(age_group)

# >3- list.sort(reverse=TRUE)--> sorts in descending order.
age_group.sort(reverse=True)
print(age_group)

# >4- list.reverse()--> it reverse the lit values.

age_group.reverse()
print(age_group)

#>5- list.insert(index,val)--> it adds the element at the desired index value or location.
age_group.insert(2,565)
print(age_group)

# >6- list.remove()--> removes the first occurence in the list.
age_group.remove(67)
print(age_group)

# >7- list.pop()--> pops the element out from the list from the given index number.
age_group.pop(4)
print(age_group)
