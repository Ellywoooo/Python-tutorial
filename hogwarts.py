students = [
    {"name":"Hermione", "house": "Griffindor", "patronus": "Otter"},
    {"name":"Harry", "house": "Griffindor", "patronus": "Stag"},
    {"name":"Ron", "house": "Griffindor", "patronus": "Jack Russell terrier"},
    {"name":"Draco", "house": "slytherin", "patronus": None},
    
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", " )