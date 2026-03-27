# lab status (flagging)
lab_active = False
pending_samples = ["001", "002", "003"]
processed_samples = []

while lab_active:
    if pending_samples:
        current_sample = pending_samples.pop()
        print(f"Processing: {current_sample.upper()}---[Done]")
        processed_samples.append(current_sample)
    else:
        print("All samples processed")
        lab_active = False
print(f"Processed {len(processed_samples)} samples")
