name = input("Whay's your name? ")

match name:
    case "Harry" | "Hermiont" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")