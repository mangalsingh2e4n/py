age_group=[32,35,21,35,67,78]
print(age_group)
#if you want to replace any value in group we can [NOTE:List is mutable]
age_group[3]=44 # it replaces the value in the list.
print(age_group)
print(age_group[3]) #prints the index value which we want.

#<===SLICING IN LIST===>
print(age_group[1:5])
#<===NEGATICE SLICING===>
print(age_group[-4:-2])