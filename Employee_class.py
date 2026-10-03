class Employee:

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)

    def increase_salary(self, percentage):
        self.salary += self.salary * percentage / 100


name = input("Enter employee name: ")
salary = float(input("Enter salary: "))
department = input("Enter department: ")

emp = Employee(name, salary, department)

emp.display()

emp.increase_salary(10)

print("\nAfter salary increment:")
emp.display()