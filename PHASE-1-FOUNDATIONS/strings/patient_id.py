patient_id = "PT-2026-00457"

prefix = patient_id[:2]
year = patient_id[3:7]
sequence = patient_id[8:]

print(prefix, year, sequence)
