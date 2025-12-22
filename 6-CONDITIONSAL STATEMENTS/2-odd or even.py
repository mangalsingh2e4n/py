#Example for checking the entered number is odd or even.

num=float(input("Enter the number you want to check for:"))
a=num%2
if(a==0):
    print("The entered number is even")
elif(a!=0):
    print("The entered number is odd")
else:
    print("The entered number is invalid")