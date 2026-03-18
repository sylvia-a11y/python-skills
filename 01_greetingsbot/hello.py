print("Hello world!")

#gathering user data
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

#creating a full name
full_name = f"{first_name} {last_name}"

#printing the final badge message with .title() clearing
print(f"welcome, {full_name.title()}!")
print("Your security badge is now active.")