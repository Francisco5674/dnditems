
def addexperience_menu(sesion):
    accesvar = 1
    while accesvar == 1:
        if len(sesion.players.keys()) != 0:
            print("************ How many experience do you want to add?")
            print("just add 0 if you want to cancel")
            print("use negative numbers to extract")

            delta = input("delta experience: ")
            if delta.isdigit():
                delta = int(delta)
                for player in sesion.players.keys():
                    sesion.players[player].experience += delta
                    sesion.players[player].update_lvl()
                print("************ Player current status **************")
                for player in sesion.players.keys():
                    sesion.players[player].status()
                print("*************************************************")
                input("press enter to go on")
                accesvar = 0
            else:
                print("Please type a valid option")
                input("press enter to continue")
        else:
            print("There are no players")
            input("press enter to go on")
            accesvar = 0
        