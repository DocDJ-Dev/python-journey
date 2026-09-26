ages = [45, 12, 67, 34]
younger_first = sorted(ages)

print(ages)  # untouched
print(younger_first)  # new list

ages.sort()
print(ages)  # <- now mutated in place
