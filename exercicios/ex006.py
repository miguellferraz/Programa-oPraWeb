employees = []

while True:
    print("\n-- Employee Registration --")
    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))
    position = str(input("Enter your position: "))
    salary = float(input("Enter your salary: "))

    employee = {
        "name": name,
        "age": age,
        "position": position,
        "salary": salary 
    }

    employees.append(employee)


    continues = input("Do you want to add more employees? (y/n): ").strip().lower()
    if continues != 'y':
        break

print("\n-- Employees List --")

for f in employees:
    print(f"Name: {f['name']} | Age: {f['age']} | Position: {f['position']} | Salary: US$ {f['salary']:.2f}")

if employees:
    averageSalary = sum(f['salary'] for f in employees) / len(employees)
    print(f"\nAverage Salary: US$ {averageSalary:.2f}")
else:
    print("\nNo registred employee.")

print("\n--- List of employees with salary above US$ 5.000,00 ---")
above5000 = [f['name'] for f in employees if f['salary'] > 5000]
if above5000:
    for name in above5000:
        print(name)
else:
    print("No employee with salary above 5.000,00")


