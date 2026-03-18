# Stock management rules
TABLETS_PER_DOSE = 6
LOW_STOCK_ALERT = 30

# Starting inventory
current_stock = 120
print(f"Morning report: We have {current_stock} tablets in stock.")

# Patient admission
patient_temp = 38.6
print(f"[Action] Patient arrived. Vital sign: Temp - {patient_temp}°C. Dispensing {TABLETS_PER_DOSE} tablets...")

current_stock = current_stock - TABLETS_PER_DOSE
print(f"Remaining stock: {current_stock} tablets.")

# Stock replenishment
shipment_received = 50
print(f"[Action] New shipment received: {shipment_received} tablets")
current_stock = current_stock + shipment_received
print(f"Evening Report: Total stock is now {current_stock} tablets.")

# Check stock level
if current_stock < LOW_STOCK_ALERT:
    print(f"Alert: Stock low ({current_stock} tablets remaining)")