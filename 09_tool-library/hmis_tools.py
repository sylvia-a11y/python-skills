def trigger_emergency_alert():
    """print a warning to the terminal"""
    print("EMERGENCY ALERT")
    print("secure samples and lead to the emergency exit")
    """Sending tests to the lab"""

def log_lab_test(patient_id, test_type):
    """Logs a lab test for a patient, Returns a string"""
    log_entry = f"Patient ID: {patient_id}, Test Type: {test_type}"
    print(log_entry)
   

def calculate_bmi(weight_kg, height_meters):
    """Calculates BMI, Returns float"""
    bmi = weight_kg / (height_meters ** 2)
    return round(bmi, 1)
    
def paediatric_dose_calculator(weight_kg, age_years):
    """placeholder function for future pead dosage calculator"""
    pass
        
                    