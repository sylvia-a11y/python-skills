# Concept: Functions, Arguments, and Return Values (PCC Chapter 8)
# TOOL 1: A SIMPLE ACTION (No raw materials needed)
# Syntax name: Function Definition

def trigger_emergency_alarm():
    """Prints a critical warning to the terminal."""
print("\n[SYSTEM ALERT] EMERRGENCY PROTOCOL INITIATED")
print("Please secure all lab samples immediately.")

# TOOL 2: ACCEPTING RAW MATERIAL(Parameters/Arguments)
# We pass data ("patient_id" and "test_type") into the parentheses.
# Syntax Name: Function Parameters

def log_lab_test(patient_id , test_type):
    """Simulates sending a test order to the lab."""
print(f"\n[LAB LOG] Order received for patient '{"patient_id"}'")
print(f"> Preparing analyzing equipment for: {"test_type".title()}")
print(f"Logging lab test: Patient ID {"patient_id"}, Test Type: {"test_type"}")

#TOOl 3: THE FACTORY PRODUCTION (Return Values)
#Printing just shows text on the screen 
# "return" actually hands the finished data back to the program
# So we can catch it with a variable and keep using it.

def calculate_bmi(weight_kg, height_meters):
    """Calculates Body Mass Index and returns the numerical float."""
# Syntax Name: Arithmetic Operators
    bmi = weight_kg / (height_meters**2)
# Syntax Name: Return statement (This is the finished product escaping the factory!)
    return round(bmi, 1) 

# TOOL 4: STILL UNDER CONSTRUCTION (The "pass" keyword)
# Sometimes, you know you need a tool, but you aren't ready to build it yet.
# If you leave a 'def' block entirely empty, Python will crush.
# Syntax Name: Tye "pass" keyword

def calculate_pediatric_dosage(weight_kg, age_months):
    """Placeholder for future pediatric dosage calculator."""
# "pass" tells Python: "I am still building this room, skip it for now"

# TOOL 5: MANAGING INVETORY (Lists - Session 04)
# Adding items to the Essential Medicines List (EML)

def update_medicine_inventory(inventory, new_medicine):
    """Adds a new medicine and sorts the list alphabetically.""" 
# Syntax Name: list method.append()
    inventory.append(new_medicine)
    inventory.sort()
    return inventory

# TOOL 6:CLINICAL TRIAGE (Conditionals - Session 06)
# Deciding urgency based on patient temperature

def get_triage_urgency(temperature):
    """Checks temperature and returns priority category."""
# Syntax Name: Conditional block (if_elif_else)
    if temperature >= 38.5:
        return "HIGH FEVER - URGENT"
    elif temperature >= 37.5:
        return "MILD FEVER - MONITOR"
    else:
        return "NORMAL - STABLE"
    
    # TOOL 7: PATIENT ARCHIVING (Dictionaries - 07)
    # Building an Electronic Health Record (EHR) entry

    def create_patient_record(name, age, blood_type):
        """Creates a dictionary for a new patient entry."""
    # Syntax Name: Dictionary Key-Value pairs
        record = {
            "patient_name": name,
            "age": age,
            "blood_type": blood_type,
            "status": "Admitted"
        }
        return record
    
    # TOOL 8: DASHBOARD PAGINATION (List Slicing - Session 10)
    # Slicing the master registry for controlled views

    def get_dashboard_page(registry, page_number, page_size = 3):
        """Returns a specific subset of patients using list slicing index logic."""
    # Syntax Name: Calculation for slicing 
        start_index = (page_number - 1) * page_size
        stop_index = start_index + page_size
    # Syntax Name: List Slice [start : stop]
        return registry[start_index : stop_index]
    
    # PART 9: USING OUR NEW TOOLS (Function Calls)
    print("=== HMIS TOOL LIBRARY INITIALIZED ===")
    # Syntax Name: Function Call (We are "pressing the button" to start the machine)
    trigger_emergency_alarm()

    # Syntax Name; passing Arguments into our tools
    log_lab_test("p-8821", "cpmplete blood count")
    log_lab_test("p-9904", "malaria rapid diagnostic")

    # Using a Return Value
    # The function hands back the number, and we use Variable Assignment to catch it!
    patient_weight = 70.5
    patient_height = 1.75
    # Syntax Name: Variable Assignment catching a Return Value
    calculated_result = calculate_bmi(patient_weight, patient_height)

    print(f"\n[CLINIC RECORD] Patient Vitals Processed.")
    print(f" > Record BMI: {calculated_result}")
    
    # Syntax Name: Calling a Placeholder Function
    # (It wil do absolutely nothing, but importantly, it won't crash!)
    calculate_pediatric_dosage(patient_weight, 48)

    # Now we can safely use the returned data in an if-statement!
    if calculated_result > 25.0:
        print(" > Note: Flag for dietary consultation. (Yellow Alert)")
    elif calculated_result < 18.5:
        print(" > Note: Flag for under weight protocol. (Red Alert)")
    else:
        print(" > Note: Normal range. (Green Status)")
    
    # --- Testing New Tools ---
    # Update_Medicine inventory (Session 04)
    eml = ["Paracetamol", "Amoxicillin"]
    updated_eml = update_medicine_inventory(eml, "Artemether")
    print(f"\n[PHARMACY] Updated EML: {updated_eml}")

    # Triage Urgency (session 06)
    triage-status = get_triage_urgency(39.1)
    print(f"[TRIAGE] Clinical Status: {triage_status}")

    # Patient Record Creation (Session 07)
    new_patient = create_patient_record("Joseph Okello", 28, "O+")
    print(f"[ARCHIVE] EHR Created: {new_patient}")
    
    # Dashboard View (Session 10)
    mock_registry = ["P-001", "p-002", "P-003", "P-004", "P-005", "P-006"]
    dashboard_view = get_dashboard_page(mock_registry, page_number = 2, page_size = 2)
    print(f"[DASHBOARD] Showing Page 2: {dashoard_view}")




        