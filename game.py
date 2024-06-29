

class Game:
    def __init__(self):
        self.players = {}

    def available_name(self, name):
        if name in self.players.keys():
            return False
        else:
            return True
    
    def status(self):
        for player in self.players.keys():
            self.players[player].status()
    


