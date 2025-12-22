#===Checking fot the greatest number among the multiple numbers===
#================================================================)

a=float(input("Please enter the number a="))
b=float(input("Please enter the number b="))
c=float(input("Please enter the number c="))
d=float(input("Please enter the number d="))

if(a>=b and a>=c and a>=d):
    print("The entered number a is greater:",a)
elif(b>=c and b>=d):
    print("The entered number b is greater:",b)
elif( c>=d):
    print("The entered number c is greater:",c)
else:
    print("The entered number d is greater:",d)

#<<==============================================================================>>

#Write a number to see that is multiple of 13 or not
#PROGRAM===

a=float(input("Please enter the numbber="))
remainder= a%13
if(remainder==0):
    print("The enter number a is multiple of 13:",a)
else:
    print("The entered number a is not a multiple of 13:",a)