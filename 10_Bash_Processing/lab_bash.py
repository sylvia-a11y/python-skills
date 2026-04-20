# Defining a function
def process_lab_batch(unprocessed_samples, completed_tests):
    while unprocessed_samples:
        current_sample = unprocessed_samples.pop()
        print(f">Analyzing sample: {current_sample}...")
        completed_tests.append(current_sample)
    print("[SYSTEM] Tray empty. Batch processing complete.")

def finalize_record(patient_list):
    for record in patient_list:
        record["status"] = "Finalized"
        record["verified_by"] = "Dr. Sylvia"
        print(f"Patient {record["id"]} updated & verified.")
        

unprocessed_samples = ["A_001(MRDT)", "A_002(HepB)", "A_003(HIV)", "A_004(Sickle_cell)", "A_005(Syphilis)"]
completed_tests = []
print(f"Completed tests: {completed_tests}")

process_lab_batch(unprocessed_samples, completed_tests)
print(f"Completed tests: {completed_tests}")
print(f"Unprocessed samples: {unprocessed_samples}")

hmis_database = [
    {"id": "P_001", "name": "John Doe", "status": "Pending"},
    {"id": "P_002", "name": "Jane Smith", "status": "Pending"},
    {"id": "P_003", "name": "Emily Davis", "status": "Pending"}
]
finalize_record(hmis_database)
print(hmis_database)