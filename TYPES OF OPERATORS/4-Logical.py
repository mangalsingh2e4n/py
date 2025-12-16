# not , and, or

# NOT operator prints the opposite of assigned value to it
print(not True) 
print(not False)
# Example
a=55
b=66
print(b>a) #prints True
print(not b>a) #prints False
#===============================================================================

# and operates on two operands
#NOTE: if two values are True prints True
a= True
b= True
c=False
print("and operator:", a and b)
print("and operator:", a and c)

# or operator also operates on two operands 
#NOTE: if any any operand is True it returns True
d=32
e=33
print("OR operator:", (d==e) or (d<e))

sam= True
sem= False
print("OR operator:", (sam==sem) or (sam!=sem))