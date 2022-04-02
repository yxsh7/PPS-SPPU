"""
Create class EMPLOYEE for storing details (Name, Designation, gender, Date of Joining 
and  Salary).  Define  function  members  to  compute  a)total  number  of  employees  in  an 
organization b) count of  male and   female  employee  c) Employee with salary  more than 
10,000 d) Employee with designation “Asst Manager
"""

# CREATING CLASS
class Employee:
    # SET EMPLOYEE COUNT TO 0
    count = 0
    def __init__(self, name, designation, gender, date_of_joining, salary):
        self.name = name
        self.designation = designation
        self.gender = gender
        self.date_of_joining = date_of_joining
        # CONVERT TO INT FROM STR
        self.salary = int(salary)
        Employee.count += 1

    # TOTAL EMPLOYEES
    def total_employees(self):
        print("Total Employees:", Employee.count) 

    # COUNT OF MALE AND FEMALE EMPLOYEES
    def gender_count(self, person):
        male = 0
        female = 0
        for letter in person:
            if letter.gender == "M":
                male += 1
            else:
                female += 1
        print(" Males:", male, " \n Females:", female)

    # EMPLOYEE WITH SALARY MORE THAN 10,000
    def salary_count(self, person):
        for letter in person:
            if letter.salary > 10000:
                print("Employees with salary more than 10,000 are: \n", letter.name)

    # EMPLOYEE WITH DESIGNATION : Asst Manager
    def designation_display(self, person):
        for letter in person:
            if letter.designation == "Asst Manager":
                print("Asst Manager:", letter.name)

# DATA OF EMPLOYEES, ADD MORE IF YOU WISH
person1 = Employee("someone","Asst Manager", "M", "04-03-2022", "100000")
person2 = Employee("someone2","Coder","F","04-03-2022","1000")
person3 = Employee("someone3","Coder","F","04-03-2022","1000")

combine = []
combine.extend([person1,person2])

person1.total_employees()
person1.gender_count(combine)
person1.salary_count(combine)
person1.designation_display(combine)

