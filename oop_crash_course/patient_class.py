# Class
class Patient:
    pass

p1 = Patient()
print(p1)
print(type(p1))

p1.name = "Apio"
p1.age = 34
p1.district = "Gulu"
p1.diagnosis = "None"

print(p1.name)
print(p1.age)
print(p1.district)
print(p1.diagnosis)

p2 = Patient()
p2.name = "Achieng"
p2.age = 28
p2.district = "Lira"
p2.diagnosis = "Malaria"
print(p2.name)
print(p2.age)
print(p2.district)
print(p2.diagnosis)

p2.age = 29
print(p2.age)
print(p1.age)

p3 = Patient()
p3.name = "Nakato"

# print(p3.district)  # This will raise an AttributeError because p3 does not have a district attribute yet

# __init__, self.
class Patient:
    def __init__(self, name, age, district, none)
        self.name = name
        self.age = age
        self.district = district
        self.diagnosis = none
        pass
