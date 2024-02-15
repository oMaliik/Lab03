employees = {}
while True:
    name = input("Enter the name of the employee:")
    if name == "no":
        break

    salary = input("Enter the salary of the employee:")
    employees[name] = salary
    print("Employee added successfully!")
print("\nStopped due to user entering 'no'")
print("\nHere is the list of Employees and their salaries:")

print(employees)