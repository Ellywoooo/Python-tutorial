import csv
name = input("What's your name? ")
house = input("Where is your house? ")

with open ("names.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","house"])
    writer.writerow({"name":name, "house":house})