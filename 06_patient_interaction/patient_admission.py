name = input("Enter patient name: \n")
# age_input = input("Enter patients age: ")
# age = int(age_input)

age = int(input("Enter patient's age: "))

print(f"Welcome: {name.title()}")

if age >= 18:
    print("Adult patient")
else:
    print("Minor")

