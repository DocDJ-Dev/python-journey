record = {"name": "Desire", "age": 24, "Diagnosis": "T2DM"}


print(record)
print(record.get("lab_results", "Not yet done."))

record["age"] = 25  # update the already existing key
record["plan"] = "admit"  # add new key

print(record)
