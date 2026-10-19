i = 1
while i <= 5:
    print("\nEnter details of student", i)

    name = input("Enter student name: ")
    sub1 = int(input("Enter subject 1 marks: "))
    sub2 = int(input("Enter subject 2 marks: "))
    sub3 = int(input("Enter subject 3 marks: "))
    sub4 = int(input("Enter subject 4 marks: "))
    sub5 = int(input("Enter subject 5 marks: "))

    avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

    print("Name:", name)
    print("Average marks:", avg)

    if avg >= 33:
        result = "Pass"
    else:
        result = "Fail"

    print("Result:", result)

    choice = int(input("Do you want to continue? (1 = Yes, 0 = No): "))

    if choice == 0:
        print("Program stopped.")
        break

    i += 1