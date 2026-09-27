age, has_allergy, is_pregnant = 14, False, True
print(age > 18 and is_pregnant and not has_allergy)  # False

age, has_allergy, is_pregnant = 30, False, True
print(age > 18 and is_pregnant and not has_allergy)  # True
