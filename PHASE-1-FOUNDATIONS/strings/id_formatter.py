# differently-formatted ID string
student_id = "2026-802008664x12-Desire-James"

year = student_id[0:4]
national_id_head = student_id[5:14]
national_id_letter = student_id[14].upper()
national_id_tail = student_id[15:17]
name = student_id[18:]
names = name.split("-")
full_name = " ".join(names).upper()

formatted = (
    f"{year:<5}{national_id_head}-{national_id_letter}-{national_id_tail:<3}{full_name}"
)
print(formatted)
