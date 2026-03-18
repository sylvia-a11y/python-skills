name = "clepa"
print(f"Hello, {name}")
print(f"Welcome {name.title()}!, Lets organize your daily study planner: ")

#---study tasks---
tasks = []
task1 = input("Enter your first task: ")
tasks.append(task1)

task2 = input("Enter your second task: ")
tasks.append(task2)

task3 = input("Enter your third task: ")
tasks.append(task3)

urgent = input("Enter your urgent task: ")
tasks.insert(0,urgent)
print(tasks)
print(f"Daily study planner: {len(tasks)}")

completed = input("Enter the task you have completed: ")
tasks.remove(completed)
print(tasks)

tasks.sort()
print(tasks)

tasks.reverse()
print(tasks)
print(tasks[0])
print(tasks[-1])

days = ("SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY")
print(days)
print(len(days))
print(f"First three days: {days[3]}")
