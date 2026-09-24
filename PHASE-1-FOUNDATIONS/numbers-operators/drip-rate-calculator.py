# volume to infuse (mL)
# infusion time (hours)
# drop factor (drops per mL)
# calculate the drip rate in drops per minute

number_of_hours = 8
total_volume = 1000
drop_factor = 20


drip_rate = round(((total_volume * drop_factor) / (number_of_hours * 60)))
print(drip_rate)
