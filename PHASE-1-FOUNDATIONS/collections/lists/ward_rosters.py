ward_a = ["Dr James", "Dr Kelly", "Nurse Shallom", "Prof Ndleve"]
ward_b = ward_a  # same references

ward_b.append("Dr Farai")
print(ward_a)
print(ward_a is ward_b)

ward_c = ward_a.copy()
print(ward_c == ward_a)  # True: same contents
print(ward_c is ward_a)  # False: different references
