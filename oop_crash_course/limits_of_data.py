print("=" * 50)
print("Patient as a list")
print("=" * 50)

patient = ["Apio", 34, "Gulu", "Malaria"]
print(f"Name: {patient[0]}")
print(f"Age: {patient[1]}")
print(f"District: {patient[2]}")
print(f"Diagnosis: {patient[3]}")

print()
print("=" * 50)
print("Patient as a Dictionary")
print("=" * 50)


patient_dict = {
    "name": "Apio", 
    "age": 34, 
    "district": "Gulu", 
    "diagnosis": "Malaria"
}   
print(f"Name: {patient_dict['name']}")
print(f"Age: {patient_dict['age']}")
print(f"District: {patient_dict['district']}")
print(f"Diagnosis: {patient_dict['diagnosis']}")

patient_dict["diagnosis"] = "Anemia"
print(patient_dict)

print()
print("=" * 50)
print("The silent typo problem of dictionary")
print("=" * 50)

drug_inventory = {
    "paracetamol": 50,
    "amoxicillin": 30,
    "metronidazole": 100
}
print("Before update:", drug_inventory)
drug_inventory["paracetamol"] =  drug_inventory.get("paracetamol", 0) - 5

print("After update:", drug_inventory)

print()
print("=" * 50)
print("Patient as a tuple")
print("=" * 50)

patient_tuple = ("Apio", 34, "Gulu", "Malaria")
print(f"Name: {patient_tuple[0]}")
print(f"Age: {patient_tuple[1]}")
print(f"District: {patient_tuple[2]}")
print(f"Diagnosis: {patient_tuple[3]}")

#patient_tuple[0] = "Achieng"  # This will raise a TypeError because tuples are immutable
