

class Player:
    def __init__(self,name):
        self.name = name
        self.__experience = 0
        self.level = 1
    
    def update_lvl(self):
        if self.experience < 300:
            self.level = 1
        elif 300 <= self.experience < 900:
            self.level = 2
        elif 900 <= self.experience < 2700:
            self.level = 3
        elif 2700 <= self.experience < 6500:
            self.level = 4
        elif 6500 <= self.experience < 14000:
            self.level = 5
        elif 14000 <= self.experience < 23000:
            self.level = 6
        elif 23000 <= self.experience < 34000:
            self.level = 7
        elif 34000 <= self.experience < 48000:
            self.level = 8
        elif 48000 <= self.experience < 64000:
            self.level = 9
        elif 64000 <= self.experience < 85000:
            self.level = 10
        elif 85000 <= self.experience < 100000:
            self.level = 11
        elif 100000 <= self.experience < 120000:
            self.level = 12
        elif 120000 <= self.experience < 140000:
            self.level = 13
        elif 140000 <= self.experience < 165000:
            self.level = 14
        elif 165000 <= self.experience < 195000:
            self.level = 15
        elif 195000 <= self.experience < 225000:
            self.level = 16
        elif 225000 <= self.experience < 265000:
            self.level = 17
        elif 265000 <= self.experience < 305000:
            self.level = 18
        elif 305000 <= self.experience < 355000:
            self.level = 19
        elif self.experience >= 355000:
            self.level = 20

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self,valor):
        if valor < 0:
            self.__experience = 0
        else:
            self.__experience = valor
    
    def status(self):
        print(f"[{self.name}], level: {self.level}, experience: {self.experience}")

    
    
