import CellPhoneClass as cp


def main():
    man = "Apple"
    mod = "iPhone 13"
    retail = 999

    phone = cp.CellPhone(man, mod, retail)

    print(phone.get_manufact())
    print(phone.get_model())
    print(phone.get_retail_price())


main()
