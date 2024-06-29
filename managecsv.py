from player import Player

def csv_reader(path,sesion):
    res = []
    with open(path, 'r', encoding= "utf8") as file:
        for line in file.readlines():
            res.append(line.strip().split(","))

    for item in res:
        if len(item) > 0:
            sesion.players[item[0]] = Player(item[0])
            sesion.players[item[0]].experience += int(item[1])
            sesion.players[item[0]].update_lvl()
    

def csv_writer(path,sesion):
    file = open(path, 'w', encoding ="utf8")
    for name in sesion.players.keys():
        xp = sesion.players[name].experience
        file.write(name +","+ str(xp) + "\n")
    
    
    

