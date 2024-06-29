from player import Player

def creatplayer_menu(sesion):
    accesvar = 1
    while accesvar == 1:
        print("******************** Creating new player ********************")
        print("Type 'cancel' if you want to cancel")

        name = str(input("name of the new player: "))
        print("****************************************************************")
        if name == "cancel":
            accesvar = 0
        else:
            if sesion.available_name(name):
                print("******************** Creating new player ********************")
                print(f"You sure you want this player to be called {name}?")
                print(f"Type 'yes' to confirm it and anything else to cancel it")

                regret = str(input( ))
                print("****************************************************************")
                if regret == "yes":
                    sesion.players[name] = Player(name)
                    print("You've created a new player!")
                    print("press enter to continue")
                    input()
                    accesvar = 0
                else:
                    pass
            else:
                print("The name is already used by other player")
                print("press enter to create another name")
                input()
            

