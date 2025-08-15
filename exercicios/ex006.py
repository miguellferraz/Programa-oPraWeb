employees = [] # Lista que armazena os dados de cada funcionário

while True: # Cria uma repetição
    print("\n-- Employee Registration --")
    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))
    position = str(input("Enter your position: "))
    salary = float(input("Enter your salary: "))

    employee = { # Dicionário com os dados de um funcionário
        "name": name,
        "age": age,
        "position": position,
        "salary": salary 
    }

    employees.append(employee) # Adiciona os dados de um novo funcionário a lista de funcionários


    continues = input("Do you want to add more employees? (y/n): ").strip().lower() # strip() remove espaços vazios e lower() deixa a string minúscula
    if continues != 'y': # Se o input for diferente de "y", vai parar de repetir o while
        break

print("\n-- Employees List --")

for f in employees: # Imprime na tela, de forma formatada, o nome, idade, cargo e salário de cada funcionário na lista employees
    print(f"Name: {f['name']} | Age: {f['age']} | Position: {f['position']} | Salary: US$ {f['salary']:.2f}")

if employees:
    averageSalary = sum(f['salary'] for f in employees) / len(employees) # Cria averageSalary, somando o salário de cada funcionário e dividindo pelo número total de funcionários para obter a média.
    print(f"\nAverage Salary: US$ {averageSalary:.2f}")
else:
    print("\nNo registred employee.")

print("\n--- List of employees with salary above US$ 5.000,00 ---")
above5000 = [f['name'] for f in employees if f['salary'] > 5000] # Cria a lista above5000 contendo os nomes dos funcionários cujo salário é maior que 5.000.
if above5000:
    for name in above5000:
        print(name)
else:
    print("No employee with salary above 5.000,00")


