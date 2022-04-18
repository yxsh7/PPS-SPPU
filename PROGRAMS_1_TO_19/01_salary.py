"""
To calculate salary of an employee given his basic pay (take as input from user). 
Calculate gross salary of employee. Let HRA be 10 % of basic pay and TA be 5% of 
basic pay. Let employee pay professional tax as 2% of total salary. Calculate net salary 
payable after deductions.
"""

# INPUT
basic_pay = int(input("Enter Salary"))

# CALCULATE 

HRA = basic_pay * (10/100)

TA = basic_pay * (5/100)

TAX = basic_pay * (2/100)

net_salary = basic_pay + HRA + TA - TAX

# DISPLAY
print("HRA",HRA)
print("TA",TA)
print("TAX",TAX)
print("NET SALARY",net_salary)

# GITHUB: yxsh7

