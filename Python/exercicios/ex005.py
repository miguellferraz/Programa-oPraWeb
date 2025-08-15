name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
city = str(input("Enter your city: "))

data = {
    "name": name,
    "age": age,
    "city": city
}

print(f"Hello {name}, you have {age} years old and lives in {city}")