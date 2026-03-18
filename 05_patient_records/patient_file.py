patient_001 = {
    "name": "annet",
    "age": 20,
    "blood_type": "O+",
    "status": "pending"
    }
print(f"opening file: {patient_001["name"].title()}") 

insurance_status = patient_001.get("insurance", "No insurance")
print(f"Billing: {insurance_status}")

patient_001["diagnosis"] = "anemia"
print(patient_001)

patient_001.update({
    "status": "reviewed",
    "last_vist": "12-03-2026"
    })

patient_001.pop("status")

for key, value in patient_001.items():
    clean_label = key.replace("_", " ").upper()
    print(f"{clean_label} : {value}")