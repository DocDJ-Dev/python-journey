patient_a_symptoms = {"fever", "cough", "fatigue"}
patient_b_symptoms = {"cough", "headache", "fatigue"}

# shared symptoms
print(f"Symptoms in both patients:{patient_a_symptoms & patient_b_symptoms}")

# combined symptoms
print(f"All symptoms combined:{ patient_a_symptoms | patient_b_symptoms}")

# unique to each one individually
print(f"Symptoms in patient a not b:{patient_a_symptoms - patient_b_symptoms}")
print(f"Symptoms in patient b not a:{patient_b_symptoms - patient_a_symptoms}")
