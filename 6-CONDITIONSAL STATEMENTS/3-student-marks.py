#======Conditional statement example using the students marks as data======
marks=float(input("Enter the marks obtained by the student="))
if(marks>=90):
    print("Mubaarak ho aapka bachaa top kar gaya-->GRADE-A")
elif(marks>=80 and marks<=90):
    print("koi baat nahi beta agli baar try karna-->GRADE-B")
elif(marks>=70 and marks<=80):
    print("Beta ab to sharam karle,sharma uncle ke bete ne top kiya hai-->GRADE-c")
elif(marks>=60 and marks<=70):
    print("Tum IAS ki taiyaari chod do-->GRADE-E")
else:
    print("Beta tu padhaayi bhoolja aur mera pakad ke jhool jaa-->GRADE-E")
