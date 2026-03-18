days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
for day in days:
    print(day)
study_hours = [2, 3, 1, 4, 5, 2, 3]
for day, hour in zip(days, study_hours):
    print(f"{day}: {hour} hours")

print(f"Last three days: {days[-3:]}")
print(f"First two days: {days[:2]}")

print(f"Total hours studied: {sum(study_hours)}")
print(f"Maximum hours studied: {max(study_hours)}")
print(f"Minimum hours studied: {min(study_hours)}")
print(f"Number of days: {len(days)}")

if sum(study_hours) >= 25:
    print("Excellent study week")
elif sum(study_hours) >= 15:
    print("Good effort") 
else:
    print("You need to study more")

if max(study_hours) > 4:
    print("Very productive day")
else:
    print("Normal study day")

if max(study_hours) > 4 and sum(study_hours) > 20:
    print("Great consistency this week!")