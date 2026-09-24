# Operators (+,-,/,*)
# ** — exponentiation (power)
# // — floor division (bracket: divide, then round down to the nearest whole number, discarding any remainder)
# % — modulus (bracket: the remainder left over after division)
# / always returns a float( 10/2 = 5.0)

# Operator precedence- BMI calculator
weight_kg = 68.0
height_m = 1.72

bmi = weight_kg / height_m**2
print(f"BMI: {bmi:.2f}")

# floor division and modulus- dosing schedule
total_minutes = 24 * 60
interval_minutes = 50

doses = total_minutes // interval_minutes
leftover_minutes = total_minutes % interval_minutes

print(f"Full doses deliverable: {doses}")
print(f"Minutes remaining after the last dose: {leftover_minutes}")

# round() -Python uses round-half-to-even ("banker's rounding"). Round grade-school-style over a large dataset and your average creeps upward with a systematic bias; round-half-to-even cancels that out.

# The floating point trap
dose_a = 0.1
dose_b = 0.2
total = dose_a + dose_b

print(total)  # 0.30000000000000004
# =>it stores numbers in binary fractions not decimals
print(total == 0.3)  # False

print(round(37.5))  # 38
print(round(38.5))  # 38  <- also 38, not 39
print(round(39.5))  # 40
print(round(40.5))  # 40
