authorised_users = ["risan", "annet", "josephine"]
current_user = "gamusi"

if current_user in authorised_users:
    print(f"Welcome, {current_user.title()}")

    if current_user == "annet":
        print("ACCESS GRANTED")

else:
    print("ACCESS DENIED")

hb_level = input("Enter hemoglobin level: ")
print(f"Patient's Hb_level is: {hb_level}")

reagent = True
distilled_water = False
if reagent and distilled_water:
    print("Run test")
elif not reagent or not distilled_water:
    print("Cannot proceed")

if hb_level < 12.0:
    print("Patient is anemic")