
import random
from random import shuffle
from tkinter import messagebox


class Buy_development_card:
    def __init__(self, knight, victory_point, monopoly, year_of_plenty, road_building):
        self.knight = knight
        self.victory_point = victory_point
        self.monopoly = monopoly
        self.year_of_plenty = year_of_plenty
        self.road_building = road_building

    deck = ['Knight', 'Knight','Knight','Knight','Knight','Knight','Knight','Knight','Knight','Knight','Knight',\
            'Knight','Knight','Knight','Year of Plenty', 'Year of Plenty', 'Victory Point', 'Road Building','Road Building', \
            'Monopoly','Monopoly', 'Victory Point','Victory Point','Victory Point','Victory Point',]
    random.shuffle(deck)


    def pick_card(self):
        print(self.deck)
        card_picked = self.deck.pop(0)
        print(self.deck)

        if card_picked == 'Knight':
            messagebox.showinfo("", ('You got a ' + str(card_picked)) + ' Card!')
            self.knight += 1
        elif card_picked == 'Victory Point':
            messagebox.showinfo("", ('You got a ' + str(card_picked)) + ' !')
            self.victory_point += 1

        elif card_picked == 'Monopoly':
            messagebox.showinfo("", ('You got a ' + str(card_picked)) + ' card!')
            self.monopoly += 1
        elif card_picked == 'Year of Plenty':
            messagebox.showinfo("", ('You got a ' + str(card_picked)) + ' card!')
            self.year_of_plenty += 1
        elif card_picked == 'Road Building':
            messagebox.showinfo("", ('You got a ' + str(card_picked)) + ' card!')
            self.road_building += 1


cards_player_1 = Buy_development_card(4, 0, 0, 0, 0)

cards_player_2 = Buy_development_card(4, 0, 0, 0, 0)



