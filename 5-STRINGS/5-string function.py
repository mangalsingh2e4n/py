str="hello iam munna singh"
#<---ENDSWITH--->
print(str.endswith("gh")) #check for the words which ends with given letter in our sentence/string, if it's there returns TRUE or else FALSE

#<---CAPITALIZE--->
print(str.capitalize()) #It capitalises the first word of the sentence or the string
#[NOTE:] it dosent make changes in our original string if we run pritn(str) it returns our original string

#If we want to make changes in our original string wwe need to store it in other function
str=(str.capitalize())
print(str)

#<---REPLACE--->
#If we want to replace any specific text in string str.replace(old,new)
print(str.replace("munna","chuna"))

#<---FIND--->search for the first occurence of the word in the sentence it returns the first index value
print(str.find("munna"))
print(str.find("o"))

#<---COUNT---> counts for how much the word occured in the string
print(str.count("o"))
 

#PROBLEM SOLVING
name=input("please enter your name")
print(len(name)) #or
print("length of your name is:",len(name))

#stopped at 30min
