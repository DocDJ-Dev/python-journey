patient_records = {"name": "Someone"}

print("allegies" in patient_records and "penicillin" in patient_records["allegies"])
# -> False, no crash

# swapped order — same logic, different sequence:
print("penicillin" in patient_records["allegies"] and "allegies" in patient_records)
# -> KeyError: 'allegies'
# Short-circuiting can't protect you from a check that happens too early; it only protects the operand that comes after the safe one.
