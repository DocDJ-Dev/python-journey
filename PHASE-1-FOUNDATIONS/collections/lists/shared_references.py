ward_a = ["Moyo", "Ncube", "Banda"]
ward_b = ward_a  # NOT a copy — same object, two names

ward_b.append("Dube")
print(ward_a)
print(ward_a is ward_b)

ward_c = ward_a.copy()  # a real, independent copy
ward_c.append("Sibanda")
print(ward_a)
print(ward_a is ward_c)
