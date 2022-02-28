import InsectClass as ic


def main():
    wings = int(input("How many wings does the insect have? "))
    legs = int(input("How many legs does the insect have? "))

    mosquito = ic.InsectObject(2, 4)
    housefly = ic.InsectObject(3, 6)

    mosquito.flight

    print("This insect can fly ", mosquito.get_miles(), "miles")


main()
