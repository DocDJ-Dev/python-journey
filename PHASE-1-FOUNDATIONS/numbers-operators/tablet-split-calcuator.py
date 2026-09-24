# required total dose (mg)
# fixed tablet strength (mg per tablet)
# calculate how many whole tablets are needed and what fractional mg remainder is left over

required_dose = 400
tablet_strength = 15

tablets_required = required_dose // tablet_strength

remaining_dose_required = required_dose % tablet_strength

print(tablets_required)
print(remaining_dose_required)
