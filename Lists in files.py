#Using Lists
employees = []

file_path = input("Enter the file path: ")


number_employees = int(input("Enter the amount of employees: "))
for counter in range(1,number_employees+1):
    employee = input("Enter employee name: ")
    employees.append(employee)

with open(file_path, "w") as file:
    for employee in employees:
        file.write("\n"+employee)
    print(f"The JSON file {file_path} has been updated.")


