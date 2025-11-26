students = [
    {"name": "An", "gender": "Female", "email": "an@em.com"},
    {"name": "Bình", "gender": "Male", "email": "binh@em.com"},
    {"name": "Cường", "gender": "Male", "email": "cuong@em.com"},
    {"name": "Giang", "gender": "Female", "email": "giang@em.com"},
    {"name": "Hương", "gender": "Female", "email": "huong@em.com"},
    {"name": "Kiên", "gender": "Male", "email": "kien@em.com"},
    {"name": "Lan", "gender": "Female", "email": "lan@em.com"},
    {"name": "Mai", "gender": "Female", "email": "mai@em.com"}
]

emails = []

for student in students:
    if student["name"] == "Cường":
        continue
    if student["gender"] == "Male":
        emails.append(student["email"])
    if len(emails) == 2:
        break

print(emails)
