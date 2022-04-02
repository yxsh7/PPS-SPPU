"""
To accept student’s five courses marks and compute his/her result. Student is passing if 
he/she  scores  marks  equal  to  and  above  40  in  each  course.  If  student  scores  aggregate 
greater  than  75%,  then  the  grade  is  distinction.  If  aggregate  is  60>=  and  <75  then  the 
grade if first division. If aggregate is 50>= and <60, then the grade is second division. If 
aggregate is 40>= and <50, then the grade is third division
"""

# INPUT
Course1 = int(input("Enter Course-1 Marks"))
Course2 = int(input("Enter Course-2 Marks"))
Course3 = int(input("Enter Course-3 Marks"))
Course4 = int(input("Enter Course-4 Marks"))
Course5 = int(input("Enter Course=5 Marks"))

# CALCULATE
total = Course1 + Course2 + Course3 + Course4 + Course5
marks = (total / 500) * 100

# CHECK

if marks > 75 and marks < 100:
    print("Distinction", marks, "%")
elif marks >= 60 and marks < 75:
    print("First Divison", marks, "%")
elif marks >= 50 and marks < 60:
    print("Second Divsion", marks, "%")
elif marks >= 40 and marks < 50:
    print("Third Divsion", marks, "%")
elif marks < 40 and marks >= 0:
    print("Fail", marks, "%")
else:
    print("Invalid Input")

# GITHUB: yxsh7
