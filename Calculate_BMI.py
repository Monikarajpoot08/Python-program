#calculating BMI
# the condition are wt =in kgs ,ht= in meters ,BMI should be in integer type
weight=int(input("Enter your weight(in kgs):"))
height=float(input("Enter your height(in m):"))
BMI=weight/(height** 2)
#output(BMI) will be in integer (whole no.) type
print("Your integer type  BMI is",int(BMI))
print("Your normal BMI is",BMI)