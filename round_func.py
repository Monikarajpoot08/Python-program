# Round function in python
wt=int(input("Enter your weight in kgs: "))
ht=float(input("Enter your height in meters: "))
bmi=wt/ht**2
print(f"your bmi is {round(bmi,3)}")
