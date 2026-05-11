# __init__, self.
class Patient:
    def __init__(self, name, age, district):
       
         # Validate data
        if age < 0:
            raise ValueError ("Age cannot be negative")
        
        if not district.strip():
            raise ValueError ("District cannot be empty")

        self.name = name
        self.age = age
        self.district = district
        self.diagnosis = None
        self.is_admitted = False

    def __str__(self):
        diagnosis_display = self.diagnosis or "Not yet diagnosed" 
        return (
            f"Patient: {self.name} | "
            f"Age: {self.age} | "
            f"District: {self.district} | "
            f"Diagnosis: {diagnosis_display}"
        )
    
    def diagnose(self, disease):
        self.diagnosis = disease
        print(f"{self.name} has been diagnosed with {disease}.")

p1 = Patient("Apio", 34, "Gulu")
print(p1)
print(f"Created: {p1.name}, {p1.age}, {p1.district}")

p1.diagnose("Malaria")
print(p1)

patients = [
    Patient("Apio", 34, "Gulu"),
    Patient("Ocen", 28, "Gulu"),
    Patient("Nakato", 25, "Gulu")
]
patients[0].diagnosis = "Malaria"
patients[2].diagnosis = "Tuberculosis"
patients[1].diagnose("Typhoid")
for p in patients:
    print(f"{p}")

try:
    p_bad = Patient("Ocen", -5, "Gulu")
except ValueError as e:
    print(f"Error: {e}")

try:
    p_bad2 = Patient("Nakato", 25, " ")
except ValueError as t:
   print(f"Error: {t}")

class Clinic:
    def __init__(self, clinic_name, location, maxbed):
        
        # Validate data
        if maxbed < 0:
            raise ValueError ("maximum beds cannot be negative")
        
        if not location.strip():
            raise ValueError ("Location cannot be empty")

        self.clinic_name = clinic_name
        self.location = location
        self.maxbed = maxbed
        self.patients_admitted = 0

    def __str__(self):
        available_beds = self.maxbed - self.patients_admitted
        return (
            f"Clinic: {self.clinic_name} | "
            f"Location: {self.location} | "
            f"Max Beds: {self.maxbed} | "
            f"Patients Admitted: {self.patients_admitted} |"
            f"Available Beds: {available_beds}"
        )   
clinic1 = Clinic("Lancent", "Mbarara", 50)
clinic2 = Clinic("Vieny", "Entebbe", 70)
#print(clinic1)
#print(clinic2)

clinics = [
    Clinic("Lancent", "Mbarara", 50),
    Clinic("Vieny", "Entebbe", 70),
    Clinic("MBN", "Mbarara ", 30)
]
for c in clinics:
    print(c)

#print(clinic1. __dict__)
#print(clinic2. __dict__)
#print(f"Created: {clinic1.clinic_name}, {clinic1.location}, {clinic1.maxbed}")
#print(f"Created: {clinic1.clinic_name}, {clinic1.location}, {clinic1.maxbed}")

try:
    clinic_mbra = Clinic("MBN", "Mbarara ", -10)
except ValueError as e:
    print(f"Error: {e}")

try:
    clinic_ent = Clinic("Maestero", " ", 70)
except ValueError as e:
    print(f"Error: {e}")

