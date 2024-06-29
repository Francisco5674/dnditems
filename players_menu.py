def players_menu(sesion, name):
    accesvar = 1
    while accesvar == 1:
        print(f"************ {name} ***************")
        print("[1] Change experience")
        print("[2] Delete character")
        print("[3] Cancel")
        option = input("Option: ")
        print("************************************")

        if option.isdigit():
            option = int(option)
            if option == 1:
                print("************ How many experience do you want to add?")
                print("just add 0 if you want to cancel")
                print("use negative numbers to extract")

                delta = input("delta experience: ")
                if delta.isdigit():
                    delta = int(delta)
                    sesion.players[name].experience += delta
                    sesion.players[name].update_lvl()
                    print("************ Player current status **************")
                    sesion.players[name].status()                  
                    print("*************************************************")
                    input("press enter to go on")
                    accesvar = 0
                else:
                    print("Please type a valid option")
                    input("press enter to continue")
            elif option == 2:
                print(f"You sure you want to delte {name}?")
                option = input("YES to confirm, anything else to cancel: ")
                if option == "YES":
                    sesion.players.pop(name, None)
                    accesvar = 0
                else:
                    pass
            elif option == 3:
                accesvar = 0
            else:
                print("Please type a valid option")
                input("press enter to continue")
        else:
            print("Please type a valid option")
            input("press enter to continue")
