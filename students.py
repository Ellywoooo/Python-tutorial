names = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        name = {"name":name, "house":house}
        names.append(name)

def get_name(student):
    return student["name"]

for name in sorted(names, key=get_name, reverse = True):
    print(f"{name['name']} is in {name['house']}")