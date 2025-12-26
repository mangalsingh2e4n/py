# # #program to enter the 3 mob=vie names and store them in the list

movie_1=input("enter the name of the movie-1=")
movie_2=input("enter the name of the movie-2=")
movie_3=input("enter the name of the movie-3=")
movie=[movie_1,movie_2,movie_3]

print(movie)


# #2-code to check the entered word is aplindrome or not
word = input("Enter the word = ")

if word == word[::-1]: #--> it reverses the entered word
    print("The word is palindrome")
else:
    print("The word is not palindrome")


#3-code to check the entered value is aplindrome or not in list
num = [1, 1, 1, 1, 1, 1]
# Original list

num_1 = num.copy()
# Creates a copy of the original list so the original is not changed

num_1.reverse()
# Reverses the copied list in place

if num == num_1:
# Compares original list with reversed list

    print("The entered list is palindrome")
    # Executes if both lists are same

else:
    print("The entered list is not palindrome")
    # Executes if both lists are different

# count the number of students with grade A

students_grades=("A","B","D","E","F","C","A","E","C","D","A","A","F")
print("The number of students with GRADE-A are=",students_grades.count("A"))


#store the above tuple in the list and sort them from A-D

grades_list=list(students_grades)
grades_list.sort()
print(grades_list)