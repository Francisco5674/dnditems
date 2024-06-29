from game import Game
from createplayer_menu import creatplayer_menu
from addexperience_menu import addexperience_menu
from addministrateplayers_menu import adminplayers_menu
from managecsv import csv_reader,csv_writer
from lootcrates_menu import lootcrates_menu

def main_menu():
    accesvar = 1
    dndsesion = Game()
    while accesvar == 1:
        print("******************** Welcome Dungeon Master ********************")
        print("What do you want to do?")
        print("[1] Create new player")
        print("[2] Add party experience points")
        print("[3] Loot crates")
        print("[4] Check players and/or update them")
        print("[5] Load")
        print("[6] Save")
        print("[7] Save and exit")

        option = input("Option: ")
        print("****************************************************************")

        if option.isdigit():
            option = int(option)
            if option == 1:
                creatplayer_menu(dndsesion)
            elif option == 2:
                addexperience_menu(dndsesion)
            elif option == 3:
                lootcrates_menu()
            elif option == 4:
                adminplayers_menu(dndsesion)
            elif option == 5:
                csv_reader("save.csv", dndsesion)
                input("loaded!")
            elif option == 6:
                csv_writer("save.csv", dndsesion)
                input("saved!")
            elif option == 7:
                csv_writer("save.csv", dndsesion)
                accesvar = 0
            else:
                print("Please type a valid option")
                input("press enter to continue")
        else:
            print("Please type a valid option")
            input("press enter to continue")
