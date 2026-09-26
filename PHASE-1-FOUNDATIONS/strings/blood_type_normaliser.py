record_1 = " O Positive"
record_2 = "o+"
record_3 = "O POS"

record_1_cleaned = record_1.strip().upper().replace("POSITIVE", "+").replace(" ", "")
record_2_cleaned = record_2.upper()
record_3_cleaned = record_3.replace(" ", "").replace("POS", "+")


print(record_1_cleaned)
print(record_2_cleaned)
print(record_3_cleaned)
