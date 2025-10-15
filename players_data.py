#create a 'player' class (maybe store score, resources and so on in it later?)
class Player:
    def __init__(self, score, hay, lumber, rock, brick,sheep):
        self.score = score
        self.hay = hay
        self.lumber = lumber
        self.rock = rock
        self.brick = brick
        self.sheep = sheep

Player_1 = Player(0, 2, 3, 4, 5, 6)
Player_2 = Player(0, 0, 0, 0, 0, 0)
