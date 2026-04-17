# Defining a function
def process_lab_batch(unprocessed_samples, completed_tests):
    while unprocessed_samples:
        current_sample = unprocessed_samples.pop()
        print(f">Analyzing sample: {current_sample}...")
        completed_tests.append(current_sample)
    print("[SYSTEM] Tray empty. Batch processing complete.")

unprocessed_samples = ["A_001(MRDT)", "A_002(HepB)", "A_003(HIV)", "A_004(Sickle_cell)", "A_005(Syphilis)"]
completed_tests = []
print(f"Completed tests: {completed_tests}")

process_lab_batch(unprocessed_samples, completed_tests)
print(f"Completed tests: {completed_tests}")
print(f"Unprocessed samples: {unprocessed_samples}")