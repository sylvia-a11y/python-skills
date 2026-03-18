patients = [
    "Maria", 
    "Shifra", 
    "Dorcus", 
    "Mary", 
    "Peter", 
    "John"
    ]

for patient in patients:
    print(f"Next in line: {patient}")
    print(f">assistant: please proceed to the next station, {patient}")

print("All patients have been briefed.")

results = [95, 110, 88, 120, 105, 92, 115, 89, 101, 108]
print(f"Total samples processed of results: {len(results)}")
print(f"Lowest result: {min(results)}")
print(f"Highest result: {max(results)}")
print(f"Batch Sum: {sum(results)}")

print(f"First 3 results: {results[:3]}")

NORMAL_RANGE = (46, 98)
if results < 46:
    print("Low")
elif results < 98:
    print("Normal")
else:
    print("High")
