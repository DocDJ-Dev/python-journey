patient_notes = None

print(patient_notes and patient_notes.upper())

# Since patient_notes is falsy, Python never even attempts .upper() — that's short-circuiting doing real protective work, not just a performance trick.
