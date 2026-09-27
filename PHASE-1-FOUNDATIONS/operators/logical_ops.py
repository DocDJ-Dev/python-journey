age = 20
has_allergy = False
eligible = age >= 18 and not has_allergy
print(eligible)


allergies = []
print(bool(allergies))
allergies.append("penicillin")
print(bool(allergies))
