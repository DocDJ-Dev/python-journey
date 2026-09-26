# An X-ray's fixed width × height dimensions
# - use tuple-used for ordered immutable list with fixed row format
x_ray_dimentions = (24, 26)
width = x_ray_dimentions[0]
height = x_ray_dimentions[1]
print(f"witdth:{width} height:{height}")

# The set of distinct drug allergies a patient has reported across several visits (no duplicates wanted, order doesn't matter)
# - use set for unordered list and cannot accept duplicates
patient_allergies = {"eczema", "conjuctivitis", "blood type A rejection", "eczema"}
print(f"Patient allegies list. No repetition: {patient_allergies}")

# A patient's full profile with named fields (name, age, blood type, etc.)
# -use dict as it contains named keys and their values
patient_details = {
    "name": "Desire",
    "age": 40,
    "blood_type": "A+",
    "diagnosis": "Anaemia due to CKD",
    "plan": "Transfusion",
}
