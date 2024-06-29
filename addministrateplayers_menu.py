from players_menu import players_menu

def adminplayers_menu(sesion):
    accesvar = 1
    while accesvar == 1:
        if len(sesion.players.keys()) != 0:
            print("************ Players: ***************")
            for player in sesion.players.keys():
                sesion.players[player].status()
            print("*************************************")
            print("type cancel to cancel the operation")
            option = input("option: ")
            if option != "cancel":
                if sesion.available_name(option):
                    print("There is no player with that name")
                    input("press enter to go on")
                else:
                    players_menu(sesion, option)
            else:
                accesvar = 0
        else:
            print("There are no players")
            input("press enter to go on")
            accesvar = 0
    