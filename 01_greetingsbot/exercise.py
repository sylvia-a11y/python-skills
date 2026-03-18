name = input("What is your name? ")
name = "seryn"
print(f"Hello, {name.title()}")

#---the to_do_list---
to_do_list = []

#---add initial task---
task1 = input("Enter your first task: ")
to_do_list.append(task1)
print(to_do_list)

task2 = input("Enter your second task: ")
to_do_list.append(task2)
task3 = input("Enter your third task: ")
to_do_list.append(task3)
print(to_do_list)

#---modifying---
to_do_list[1] = to_do_list[1].upper()
print(to_do_list)

#--- add priority task---
to_do_list.insert(0,"Urgent_Meeting")
print(to_do_list)

to_do_list.sort()
print(to_do_list)

to_do_list.reverse()
print(to_do_list)

to_do_list.remove("Urgent_Meeting")
print(to_do_list)

#---final list---
print(f"{name.title()}, here is your final to-do-list: ")
print(f"{task1.title()}, {task2.title()}, {task3.title()}")