from lootcrate_api import loot_crate

def lootcrates_menu():
    accesvar = 1
    while accesvar == 1:
        print("**************** Choose a loot crate *******************")
        print("[1] Uncommon")
        print("[2] Rare")
        print("[3] Very rare")
        print("[4] Legendary")
        print("[5] Cancel")

        option = input("Option: ")
        print("*********************************************************")

        if option.isdigit():
            option = int(option)
            if option == 1:
                loot_crate("uncommon")
                input("press enter to continue")
            elif option == 2:
                loot_crate("rare")
                input("press enter to continue")
            elif option == 3:
                loot_crate("veryrare")
                input("press enter to continue")
            elif option == 4:
                loot_crate("legendary")
                input("press enter to continue")
            elif option == 5:
                accesvar = 0          
            else:
                print("Please type a valid option")
                input("press enter to continue")
        else:
            print("Please type a valid option")
            input("press enter to continue")
