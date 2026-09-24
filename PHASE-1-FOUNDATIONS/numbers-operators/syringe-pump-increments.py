# Serial thoracoscentesis
# In tension pneumothorax
# gas or fluid serially measured and added
# pressure is monitored until whole lung re-expands


first_recording = 51.3
second_recording = 31.3
third_recording = 22.7
fourth_recording = 12.4
targeted_total = 117.0
tolerance_threshold = 0.001

total_fluid_collected = (
    first_recording + second_recording + third_recording + fourth_recording
)

difference = abs(total_fluid_collected - targeted_total)

is_close = difference < tolerance_threshold

print(total_fluid_collected)
print(difference)
print(is_close)
