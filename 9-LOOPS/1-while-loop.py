#A while loop in Python is used to repeat a block of code as long as a condition is TRUE.

#EXAMPLE-1
m=1
while m<=69:
    print("mangal singh")
    m+=1
print(m)

#EXAMPLE-2 print the values from 5 to 1.
M=5
while M>=1:
    print(M)
    M-=1

#Printing table of n
n=int(input("enetr the value="))
k=1
while k<=10:
    print(n*k)
    k+=1

#printing the square root of n
n=int(input("please enter the value="))
while n<=10:
    print(n**2)
    n+=1
print(n)

#Printing a value from the tuple by the index number with loop and conditional statement.

Politicians=("Lalu","Modi","Awaisi","Gandhi","AMIT","Farukh","KCR","KTR")
find="AMIT"
i=0
while i<len(Politicians):
    if (Politicians[i]==find):
        print("politician fount at=",i)
        break  
    i+=1
else:
    print("The entered politician is not found at the index")
        
lol=(1,2,3,4,5,6,7,8,9,0,)
print(500)