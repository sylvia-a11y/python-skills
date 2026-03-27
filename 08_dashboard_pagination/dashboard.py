patient_registry = [
    "A001 - Maria",
    "A002 - Desiree",
    "A003 - Nasir",
    "A004 - Patrick",
    "A005 - Godfrey",
    "A006 - John",
    "A007 - Emily",
    "A008 - Michael",
    "A009 - Sarah",
    "A010 - David",
    "A011 - Lisa",
    "A012 - Nakato",
]

total_patients = len(patient_registry)
print(f"Total patients: {total_patients}")
PAGE_SIZE = 6
page_1 = patient_registry[:PAGE_SIZE]
print(f"\n---PAGE 1(Records 1 - {PAGE_SIZE})---")
for patient in page_1:
    print(f"- {patient}")

#page 2 patient 6 - 10
#start - PAGE_SIZE
#stop - PAGE_SIZE * 2
page_2 = patient_registry[PAGE_SIZE:PAGE_SIZE * 2]
print(f"\n---PAGE 2(Records {PAGE_SIZE + 1} - {PAGE_SIZE * 2})---")
for patient in page_2:
    print(f"- {patient}")

#page 3 patient 11 - 12
#start - PAGE_SIZE * 2
page_3 = patient_registry[PAGE_SIZE * 2: ]
print(f"\n---PAGE 3(Remaining Records)---")
for patient in page_3:
    print(f"- {patient}")
