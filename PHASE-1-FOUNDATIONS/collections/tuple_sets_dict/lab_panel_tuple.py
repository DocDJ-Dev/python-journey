# fixed format (test_name, value, unit)

lab_result = ("HBA1C", 6, "%")

test_name, value, unit = lab_result

print(f"""Patient results:
Test: {test_name}
Result Value: {value}{unit}""")
