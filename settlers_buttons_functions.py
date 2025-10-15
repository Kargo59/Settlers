import math
import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from pathlib import Path
from collections import Counter
from tkinter import messagebox
import random
from math import floor
import numpy as np


import settlers_graph_drawing
import settlers_20_10_21
import settlers_graph_properties


#import modules to graph and to display the graph properly in Tkinter
from matplotlib import pyplot as plt
import networkx as nx
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as patches
from matplotlib.backend_bases import MouseButton

#####################################################                          functions of the buttons         ############################################################



#Clears the canvas and plots a new graph - in order for it to work normally 'start_graph' has to be changed
#to something more general
def change_view_settlement():
    settlers_graph_drawing.start_graph.clearPlotPage()
    settlers_graph_drawing.settlement_graph.create_graph()

def change_view_city():
    settlers_graph_drawing.start_graph.clearPlotPage()
    settlers_graph_drawing.city_graph.create_graph()

#confirms selection based on the type of action performed. Later to also update the player's score, resources etc.
def confirm_selection():
    if settlers_graph_drawing.x == ['settlement']:
        #dict_properties.update({1:'settlement'})
        settlers_graph_drawing.settlement_graph.clearPlotPage()
        settlers_graph_drawing.start_graph.create_graph()
    elif settlers_graph_drawing.x == ['confirm_settlement']:
        settlers_graph_drawing.confirm_settlement_graph.clearPlotPage()
        settlers_graph_drawing.updated_nodes.assign_settlement_value()
        # print(updated_nodes.dict_prop)
        # for r in updated_nodes.dict_prop:
        #     if r == key_settlement:
        #         print(updated_nodes[r].dict_prop)
        #updated_nodes.dict_prop.update({1:'settlement'})
        #print(updated_nodes.dict_prop)
        settlers_graph_drawing.Player_2.score += 1
        #print(Player_2.score)
        settlers_graph_drawing.start_graph.create_graph()
    elif settlers_graph_drawing.x == ['confirm_city']:
        settlers_graph_drawing.confirm_city_graph.clearPlotPage()
        settlers_graph_drawing.updated_nodes.assign_city_value()
        # print(updated_nodes.dict_prop)
        # for r in updated_nodes.dict_prop:
        #     if r == key_settlement:
        #         print(updated_nodes[r].dict_prop)
        # updated_nodes.dict_prop.update({1:'settlement'})
        # print(updated_nodes.dict_prop)
        settlers_graph_drawing.Player_2.score += 1
        #print(Player_2.score)
        settlers_graph_drawing.start_graph.create_graph()
    elif settlers_graph_drawing.x == ['road']:
        settlers_graph_drawing.road_graph.clearPlotPage()
        settlers_graph_drawing.start_graph.create_graph()
    elif settlers_graph_drawing.x == ['confirm_road']:
        settlers_graph_drawing.confirm_road_graph.clearPlotPage()
        settlers_graph_drawing.updated_nodes.assign_road_value()
        settlers_graph_drawing.start_graph.create_graph()

    elif settlers_graph_drawing.x == ['confirm_knight_card']:
        settlers_graph_drawing.confirm_knight_card_graph.clearPlotPage()
        settlers_graph_properties.updated_nodes.assign_robber()
        settlers_20_10_21.player1_trade["state"] = "normal"
        settlers_20_10_21.player1_use_dev_card["state"] = "normal"
        settlers_20_10_21.player1_build["state"] = "normal"
        settlers_20_10_21.player1_end_turn["state"] = "normal"
        settlers_20_10_21.player1_roll_dice["state"] = "disabled"
        settlers_20_10_21.player1_cancel['state'] = 'disabled'
        settlers_20_10_21.player1_confirm['state'] = 'disabled'
        settlers_graph_properties.start_graph.create_graph()

#cancels the action and goes back to the normal view
def cancel_selection():
    if x == ['settlement']:
        settlement_graph.clearPlotPage()
        start_graph.create_graph()
    elif x == ['confirm_settlement']:
        confirm_settlement_graph.clearPlotPage()
        start_graph.create_graph()
    elif x == ['confirm_city']:
        confirm_city_graph.clearPlotPage()
        start_graph.create_graph()
    elif x == ['road']:
        road_graph.clearPlotPage()
        start_graph.create_graph()
    elif x == ['confirm_road']:
        confirm_road_graph.clearPlotPage()
        start_graph.create_graph()
    elif x == ['city']:
        city_graph.clearPlotPage()
        start_graph.create_graph()
    elif x == ['confirm_knight_card']:
        confirm_knight_card_graph.clearPlotPage()
        player1_trade["state"] = "normal"
        player1_use_dev_card["state"] = "normal"
        player1_build["state"] = "normal"
        player1_end_turn["state"] = "normal"
        player1_roll_dice["state"] = "disabled"
        player1_cancel['state'] = 'disabled'
        player1_confirm['state'] = 'disabled'

        start_graph.create_graph()


def build_road():
    start_graph.clearPlotPage()
    road_graph.create_graph()


def end_turn():
    updated_nodes.turn += 1
    #print(updated_nodes.turn)

counter = False
counter_dev_card = False
counter_trade = False
roll_counter = 0

#######################################     function to roll the dice, twice. before the two rolls, all other buttons are disabled      #################################################
def roll_dice():
    global rock
    global sheep
    global hay
    global brick
    global lumber
    global roll_counter

    if roll_counter < 2:
        roll_1 = int(random.randint(1, 6))
        roll_2 = int(random.randint(1, 6))

        sum_both_rolls = roll_1 + roll_2
        if sum_both_rolls == 7:
            hand_player_1 = []
            for i in range(int(Player_1.lumber)):
                hand_player_1.append('lumber')
            for i in range(int(Player_1.sheep)):
                hand_player_1.append('sheep')
            for i in range(int(Player_1.brick)):
                hand_player_1.append('brick')
            for i in range(int(Player_1.rock)):
                hand_player_1.append('rock')
            for i in range(int(Player_1.hay)):
                hand_player_1.append('hay')

            sum_hand_player_1 = len(hand_player_1)
            half_deck_player_1 = int(0.5 * int(sum_hand_player_1))
            #print(sum_hand_player_1)
            #print(half_deck_player_1)
            #print(hand_player_1)
            random.shuffle(hand_player_1)
            del hand_player_1[0:half_deck_player_1]
            #print(hand_player_1)
            #print(Counter(hand_player_1))
            Player_1.lumber = Counter(hand_player_1)['lumber']
            Player_1.brick = Counter(hand_player_1)['brick']
            Player_1.sheep = Counter(hand_player_1)['sheep']
            Player_1.rock = Counter(hand_player_1)['rock']
            Player_1.hay = Counter(hand_player_1)['hay']



        #print(sum_both_rolls)
        #print(updated_nodes.dict_prop)
        #print(dict_labels)
        #print(pos)

        nodes_rolled = []
        neighbors_middle_node = []
        #print(edges_only_middle_nodes)

        for key, record in dict_labels.items():
            if dict_labels[key] == sum_both_rolls:
                nodes_rolled.append(key)
                for element in edges_only_middle_nodes:
                    if str(key) in element:
                        neighbors_middle_node.append(element)

        #print(nodes_rolled)

        #print(neighbors_middle_node)

        #print(edges_only_middle_nodes)
        mid_nodes = []
        for edge in edges_only_middle_nodes:
            mid_nodes.append(edge[1])
        mid_nodes = set(mid_nodes)
        mid_nodes = sorted(list(mid_nodes))
        mid_nodes_enumerated = list(enumerate(mid_nodes,1))

        #print(mid_nodes_enumerated)
        #print(updated_nodes.dict_hex_colors)
        #print(Player_1.sheep)


        for element in neighbors_middle_node:
            if updated_nodes.dict_prop[element[0]] == 'settlement_player_2' or updated_nodes.dict_prop[element[0]] == 'city_player_2':
                price = element[1]
                for a in mid_nodes_enumerated:
                    if price in a:
                        color_index = a[0]
                        if updated_nodes.dict_hex_colors[color_index] == 'dimgrey':
                            print('rock')
                            Player_1.rock += 1
                        if updated_nodes.dict_hex_colors[color_index] == 'yellow':
                            print('hay')
                            Player_1.hay += 1
                        if updated_nodes.dict_hex_colors[color_index] == 'lime':
                            print('sheep')
                            Player_1.sheep += 1
                        if updated_nodes.dict_hex_colors[color_index] == 'red':
                            print('brick')
                            Player_1.brick += 1
                        if updated_nodes.dict_hex_colors[color_index] == 'forestgreen':
                            print('lumber')
                            Player_1.lumber += 1

        #print(Player_1.lumber, Player_1.sheep, Player_1.hay, Player_1.brick, Player_1.rock)

        # lumber = StringVar()
        lumber.set(Player_1.lumber)
        rock.set(Player_1.rock)
        brick.set(Player_1.brick)
        sheep.set(Player_1.sheep)
        hay.set(Player_1.hay)
        #updates the score by removing and placing a label
        # player1_rock_score.place_forget()
        # player1_rock_score.place(x=250, y=125)
        # player1_lumber_score.place_forget()
        # player1_lumber_score.place(x=120, y=125)
        # player1_hay_score.place_forget()
        # player1_hay_score.place(x=80, y=172)
        # player1_brick_score.place_forget()
        # player1_brick_score.place(x=195, y=172)
        # player1_sheep_score.place_forget()
        # player1_sheep_score.place(x=310, y=172)

        #         print('player 1 gets a resource')
            # if updated_nodes.dict_prop[node] == 'settlement_player_2' or updated_nodes.dict_prop[node] == 'city_player_2':
            #     print('player 2 gets a resource')












        # for record in updated_nodes.dict_prop:
        #     if updated_nodes.dict_prop[record] == 'settlement_player_1' or updated_nodes.dict_prop[record] == \
        #             'city_player_1':


        # player 1 - displays the result of the first roll
        player1_roll_1 = Label(root, width=3, height=1, bg='white', text=roll_1, font=('Times New Roman', 30))
        player1_roll_1.place(x=10, y=570)

        # player 1 - displays the result of the other roll
        player1_roll_2 = Label(root, width=3, height=1, bg='white', text=roll_2, font=('Times New Roman', 30), state='normal')
        player1_roll_2.place(x=100, y=570)


        roll_counter += 1

    if roll_counter == 2:
        player1_roll_dice['state'] = 'disable'
        player1_trade['state'] = 'normal'
        player1_use_dev_card['state'] = 'normal'
        player1_build['state'] = 'normal'
        player1_end_turn['state'] = 'normal'
        player1_confirm['state'] = 'disable'
        player1_cancel['state'] = 'disable'




# #function that expand the menu "Play a development card"
def dev_card():
    global counter_dev_card
    global counter
    global counter_trade

    if counter_dev_card == False:
        player1_trade_bank.place_forget()
        player1_trade_merchant.place_forget()
        player1_build_road.place_forget()
        player1_build_settlement.place_forget()
        player1_build_city.place_forget()
        player1_buy_dev_card.place_forget()
        player1_knight_card.place(x=270, y=270)
        player1_year_of_plenty_card.place(x=270, y=320)
        player1_road_building_card.place(x=270, y=370)
        player1_monopoly_card.place(x=270, y=420)
        counter_dev_card = True
        counter_trade = False

    elif counter_dev_card == True:
        player1_knight_card.place_forget()
        player1_year_of_plenty_card.place_forget()
        player1_road_building_card.place_forget()
        player1_monopoly_card.place_forget()
        counter_dev_card = False

    #function that expand the menu "Trade"
def trade():
    global counter_dev_card
    global counter_trade
    global counter

    if counter_trade == False:
        player1_build_road.place_forget()
        player1_build_settlement.place_forget()
        player1_build_city.place_forget()
        player1_buy_dev_card.place_forget()
        player1_knight_card.place_forget()
        player1_year_of_plenty_card.place_forget()
        player1_road_building_card.place_forget()
        player1_monopoly_card.place_forget()
        player1_trade_bank.place(x=270, y=270)
        player1_trade_merchant.place(x=270, y=220)
        counter_trade = True
        counter = False
        counter_dev_card = False

    elif counter_trade == True:
        player1_knight_card.place_forget()
        player1_year_of_plenty_card.place_forget()
        player1_road_building_card.place_forget()
        player1_monopoly_card.place_forget()
        player1_trade_bank.place_forget()
        player1_trade_merchant.place_forget()
        counter_trade = False

########################################            function that creates a new window to trade with the merchant       #######################################################

def trade_merchant():
    pass




########################################            function that creates a new window to trade with the bank       #######################################################
def trade_bank():

    #disable all buttons until you close the new window
    player1_trade_bank.place_forget()
    player1_trade_merchant.place_forget()
    player1_build["state"] = "disabled"
    player1_trade["state"] = "disabled"
    player1_use_dev_card["state"] = "disabled"
    player1_end_turn["state"] = "disabled"



    # Toplevel object which will
    # be treated as a new window
    bank_window = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    bank_window.title("Trade with the bank")

    # sets the geometry of toplevel
    bank_window.geometry("300x250")

    #puts the new window in the center
    width = root.winfo_x()
    height = root.winfo_y()
    bank_window.geometry("+%d+%d" % (width + 700, height + 400))

    # Make topLevelWindow remain on top until destroyed, or attribute changes.
    bank_window.attributes('-topmost', 1)

    # A Label widget to show in toplevel - this 'dummy' label is made to put two other columns in the middle on the window
    Label(bank_window, text="     ", font=("Times New Roman", 10), padx = 10, pady = 10).grid(row=0, column=0, columnspan=1)

    # A Label widget to show in toplevel
    Label(bank_window, text="Your 4 cards:", font=("Times New Roman", 10), padx = 10, pady = 10).grid(row=0, column=2, columnspan=1)

    # A Label widget to show in toplevel
    Label(bank_window, text="For bank's 1 card:", font=("Times New Roman", 10), padx = 30, pady = 10).grid(row=0, column=4, columnspan=1)


    #funtion that closes  the "trade bank" new window

    def close_window():
        bank_window.destroy()
        player1_roll_dice['state'] = 'disable'
        player1_trade['state'] = 'normal'
        player1_use_dev_card['state'] = 'normal'
        player1_build['state'] = 'normal'
        player1_end_turn['state'] = 'normal'
        player1_confirm['state'] = 'disable'
        player1_cancel['state'] = 'disable'

        #what happens after the 'confirm' button is clicked

    def confirm_bank():
        if v.get() == 'Brick' and Player_1.brick >= 4:
            if z.get() == 'Brick':
                Player_1.brick -= 3
                brick.set(Player_1.brick)
            elif z.get() == 'Lumber':
                Player_1.lumber += 1
                Player_1.brick -= 4
                brick.set(Player_1.brick)
                lumber.set(Player_1.lumber)
            elif z.get() == 'Sheep':
                Player_1.sheep += 1
                Player_1.brick -= 4
                brick.set(Player_1.brick)
                sheep.set(Player_1.sheep)
            elif z.get() == 'Wheat':
                Player_1.hay += 1
                Player_1.brick -= 4
                brick.set(Player_1.brick)
                hay.set(Player_1.hay)
            elif z.get() == 'Rock':
                Player_1.rock += 1
                Player_1.brick -= 4
                brick.set(Player_1.brick)
                rock.set(Player_1.rock)

            bank_window.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'

        elif v.get() == 'Lumber' and Player_1.lumber >= 4:
            if z.get() == 'Lumber':
                Player_1.lumber -= 3
                lumber.set(Player_1.lumber)
            elif z.get() == 'Brick':
                Player_1.lumber -= 4
                Player_1.brick += 1
                brick.set(Player_1.brick)
                lumber.set(Player_1.lumber)
            elif z.get() == 'Sheep':
                Player_1.sheep += 1
                Player_1.lumber -= 4
                lumber.set(Player_1.lumber)
                sheep.set(Player_1.sheep)
            elif z.get() == 'Wheat':
                Player_1.hay += 1
                Player_1.lumber -= 4
                lumber.set(Player_1.lumber)
                hay.set(Player_1.hay)
            elif z.get() == 'Rock':
                Player_1.rock += 1
                Player_1.lumber -= 4
                rock.set(Player_1.rock)
                lumber.set(Player_1.lumber)

            bank_window.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'


        elif v.get() == 'Sheep' and Player_1.sheep >= 4:
            if z.get() == 'Sheep':
                Player_1.sheep -= 3
                sheep.set(Player_1.sheep)
            elif z.get() == 'Brick':
                Player_1.sheep -= 4
                Player_1.brick += 1
                sheep.set(Player_1.sheep)
                brick.set(Player_1.brick)
            elif z.get() == 'Lumber':
                Player_1.sheep -= 4
                Player_1.lumber += 1
                sheep.set(Player_1.sheep)
                lumber.set(Player_1.lumber)
            elif z.get() == 'Wheat':
                Player_1.sheep -= 4
                Player_1.hay += 1
                sheep.set(Player_1.sheep)
                hay.set(Player_1.hay)
            elif z.get() == 'Rock':
                Player_1.sheep -= 4
                Player_1.rock += 1
                sheep.set(Player_1.sheep)
                rock.set(Player_1.rock)

            bank_window.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'

        elif v.get() == 'Wheat' and Player_1.hay >= 4:
            if z.get() == 'Wheat':
                Player_1.hay -= 3
                hay.set(Player_1.hay)
            elif z.get() == 'Brick':
                Player_1.hay -= 4
                Player_1.brick += 1
                hay.set(Player_1.hay)
                brick.set(Player_1.brick)
            elif z.get() == 'Lumber':
                Player_1.hay -= 4
                Player_1.lumber += 1
                hay.set(Player_1.hay)
                lumber.set(Player_1.lumber)
            elif z.get() == 'Sheep':
                Player_1.hay -= 4
                Player_1.sheep += 1
                sheep.set(Player_1.sheep)
                hay.set(Player_1.hay)
            elif z.get() == 'Rock':
                Player_1.hay -= 4
                Player_1.rock += 1
                hay.set(Player_1.hay)
                rock.set(Player_1.rock)

            bank_window.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'


        elif v.get() == 'Rock' and Player_1.rock >= 4:
            if z.get() == 'Rock':
                Player_1.rock -= 3
                rock.set(Player_1.rock)
            elif z.get() == 'Brick':
                Player_1.rock -= 4
                Player_1.brick += 1
                rock.set(Player_1.rock)
                brick.set(Player_1.brick)
            elif z.get() == 'Lumber':
                Player_1.rock -= 4
                Player_1.lumber += 1
                rock.set(Player_1.rock)
                lumber.set(Player_1.lumber)
            elif z.get() == 'Sheep':
                Player_1.rock -= 4
                Player_1.sheep += 1
                sheep.set(Player_1.sheep)
                rock.set(Player_1.rock)
            elif z.get() == 'Wheat':
                Player_1.rock -= 4
                Player_1.hay += 1
                hay.set(Player_1.hay)
                rock.set(Player_1.rock)

            bank_window.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'



        else:
            bank_window.attributes('-topmost', 0)
            messagebox.showinfo("", "At least 4 cards of this kind required")
            bank_window.attributes('-topmost', 1)


                                        #########################            ####################

    # Tkinter string variable
    # able to store any string value
    v = StringVar(bank_window, "None")


    # Tkinter string variable
    # able to store any string value
    z = StringVar(bank_window, "None")



    # Dictionary to create multiple buttons
    values_1 = {"Brick": "Brick",
              "Lumber": "Lumber",
              "Sheep": "Sheep",
              "Wheat": "Wheat",
              "Rock": "Rock"}


    # Dictionary to create multiple buttons
    values_2 = {"Brick": "Brick",
              "Lumber": "Lumber",
              "Sheep": "Sheep",
              "Wheat": "Wheat",
              "Rock": "Rock"}


    y = 1

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for (text, value) in values_1.items():
        Radiobutton(bank_window, width=10, text=text, variable=v,
                    value=value, indicator=0,
                    background="lightskyblue").grid(row=y, column=2, columnspan=2)
        y +=1


    b = 1

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for (text_2, value_2) in values_2.items():
        Radiobutton(bank_window, width=10, text=text_2, variable=z,
                    value=value_2, indicator=0,
                    background="lightskyblue").grid(row=b, column=4, columnspan=2)
        b +=1

    #'cancel' button inside this window
    cancel_bank = Button(bank_window, width=3, height=1, bg='white', text=chr(10008), fg='red',\
                        font=('Times New Roman', 20), \
                        command=close_window).grid(row=6, column=2, columnspan=1, padx=10, pady=20)

    #'confirm' button inside this window
    confirm_bank = Button(bank_window, width = 3, height=1, bg='white', text=chr(10003), fg='green',\
                          font=('Times New Roman', 20), \
                          command=confirm_bank).grid(row=6, column=4, columnspan=2, padx=10, pady=20)


########################################            function that creates a new window to trade with the merchant       #######################################################
def trade_merchant():

    #disable all buttons until you close the new window
    player1_trade_bank.place_forget()
    player1_trade_merchant.place_forget()
    player1_build["state"] = "disabled"
    player1_trade["state"] = "disabled"
    player1_use_dev_card["state"] = "disabled"
    player1_end_turn["state"] = "disabled"



    # Toplevel object which will
    # be treated as a new window
    merchant_window = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    merchant_window.title("Trade with the merchant")

    # sets the geometry of toplevel
    merchant_window.geometry("300x250")

    #puts the new window in the center
    width = root.winfo_x()
    height = root.winfo_y()
    merchant_window.geometry("+%d+%d" % (width + 700, height + 400))

    # Make topLevelWindow remain on top until destroyed, or attribute changes.
    merchant_window.attributes('-topmost', 'true')

    # A Label widget to show in toplevel - this 'dummy' label is made to put two other columns in the middle on the window
    Label(merchant_window, text="     ", font=("Times New Roman", 12), padx = 10, pady = 10).grid(row=0, column=0, columnspan=1)

    # A Label widget to show in toplevel
    Label(merchant_window, text="Your offer:", font=("Times New Roman", 12), padx = 10, pady = 10).grid(row=0, column=2, columnspan=1)

    # A Label widget to show in toplevel
    Label(merchant_window, text="For 1 card:", font=("Times New Roman", 12), padx = 30, pady = 10).grid(row=0, column=4, columnspan=1)


    ##funtion that closes  the "trade merchant" new window

    def close_window():
        merchant_window.destroy()
        player1_roll_dice['state'] = 'disable'
        player1_trade['state'] = 'normal'
        player1_use_dev_card['state'] = 'normal'
        player1_build['state'] = 'normal'
        player1_end_turn['state'] = 'normal'
        player1_confirm['state'] = 'disable'
        player1_cancel['state'] = 'disable'


                                        #########################            ####################

    # Tkinter string variable
    # able to store any string value
    v = StringVar(merchant_window, "1")


    # Tkinter string variable
    # able to store any string value
    z = StringVar(merchant_window, "1")



    # Dictionary to create multiple buttons
    values_1 = {"2:1 Lumber": "2",
              "2:1 Sheep": "3",
              "2 x Wheat": "4",
              "2 x Rock": "5"}


    # Dictionary to create multiple buttons
    values_2 = {"Brick": "6",
              "Lumber": "7",
              "Sheep": "8",
              "Wheat": "9",
              "Rock": "10"}


    y = 2

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for (text, value) in values_1.items():
        Radiobutton(merchant_window, width=10, text=text, variable=v,
                    value=value, indicator=0,
                    background="lightskyblue").grid(row=y, column=2, columnspan=2)
        y +=1


    b = 1

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for (text_2, value_2) in values_2.items():
        Radiobutton(merchant_window, width=10, text=text_2, variable=z,
                    value=value_2, indicator=0,
                    background="lightskyblue").grid(row=b, column=4, columnspan=2)
        b +=1

    #'cancel' button inside this window
    cancel_merchant = Button(merchant_window, width=3, height=1, bg='white', text=chr(10008), fg='red',\
                        font=('Times New Roman', 20), \
                        command=close_window).grid(row=6, column=2, columnspan=1, padx=10, pady=20)

    #'confirm' button inside this window
    confirm_merchant = Button(merchant_window, width = 3, height=1, bg='white', text=chr(10003), fg='green',\
                          font=('Times New Roman', 20), \
                          command=confirm_selection).grid(row=6, column=4, columnspan=2, padx=10, pady=20)

    def any_3_cards():
        Radiobutton.forget()


    merchant_any_card_button = Button(merchant_window, text="3:1 (Any Card)", background="lightskyblue", command=any_3_cards).grid(row=1, column=2, columnspan=2)



################################### #                function that expands the menu "Build"         #########################################
def click_build():
    global counter
    global counter_dev_card
    global counter_trade

    if counter == True:
        player1_build_road.place_forget()
        player1_build_settlement.place_forget()
        player1_build_city.place_forget()
        player1_buy_dev_card.place_forget()
        counter = False

    elif counter == False:
        player1_trade_bank.place_forget()
        player1_trade_merchant.place_forget()
        player1_knight_card.place_forget()
        player1_year_of_plenty_card.place_forget()
        player1_road_building_card.place_forget()
        player1_monopoly_card.place_forget()
        player1_build_road.place(x=270, y=320)
        player1_build_settlement.place(x=270, y=370)
        player1_build_city.place(x=270, y=420)
        player1_buy_dev_card.place(x=270, y=470)
        counter = True
        counter_dev_card = False
        counter_trade = False


#####################################################         functions to define the development cards buttons        ###########################################


def knight_card():
    start_graph.clearPlotPage()
    knight_card_graph.create_graph()
    player1_knight_card.place_forget()
    player1_year_of_plenty_card.place_forget()
    player1_build_road.place_forget()
    player1_build_settlement.place_forget()
    player1_build_city.place_forget()
    player1_buy_dev_card.place_forget()
    player1_road_building_card.place_forget()
    player1_monopoly_card.place_forget()


############################    function that defines what happens after clicking the 'year of plenty' button     ##################################################################
def year_of_plenty():
    player1_knight_card.place_forget()
    player1_year_of_plenty_card.place_forget()
    player1_build_road.place_forget()
    player1_build_settlement.place_forget()
    player1_build_city.place_forget()
    player1_buy_dev_card.place_forget()
    player1_road_building_card.place_forget()
    player1_monopoly_card.place_forget()

    player1_roll_dice['state'] = 'disable'
    player1_trade['state'] = 'disable'
    player1_use_dev_card['state'] = 'disable'
    player1_build['state'] = 'disable'
    player1_end_turn['state'] = 'disable'
    player1_confirm['state'] = 'disable'
    player1_cancel['state'] = 'disable'

    # Toplevel object which will
    # be treated as a new window
    year_of_plenty = Toplevel(root)

    #what happens when 'X' on the top bar is clicked
    def on_exit():
        player1_roll_dice['state'] = 'disable'
        player1_trade['state'] = 'normal'
        player1_use_dev_card['state'] = 'normal'
        player1_build['state'] = 'normal'
        player1_end_turn['state'] = 'normal'
        player1_confirm['state'] = 'disable'
        player1_cancel['state'] = 'disable'
        year_of_plenty.destroy()

    year_of_plenty.protocol("WM_DELETE_WINDOW", on_exit)


    # sets the title of the Toplevel widget
    year_of_plenty.title("Year of plenty")

    # sets the geometry of toplevel
    year_of_plenty.geometry("300x250")

    # puts the new window in the center
    width = root.winfo_x()
    height = root.winfo_y()
    year_of_plenty.geometry("+%d+%d" % (width + 700, height + 400))

    # Make topLevelWindow remain on top until destroyed, or attribute changes.
    year_of_plenty.attributes('-topmost', 1)

    # A Label widget to show in toplevel - this 'dummy' label is made to put two other columns in the middle on the window
    Label(year_of_plenty, text="            ", font=("Times New Roman", 10), padx=10, pady=10).grid(row=0, column=0, columnspan=1)

    # A Label widget to show in toplevel
    Label(year_of_plenty, text="Draw 2 cards from the bank", font=("Times New Roman", 10), padx=10, pady=10).grid(row=0, column=1,
                                                                                                  columnspan=1)

    # funtion that closes  the "trade bank" new window

    def close_window():
        year_of_plenty.destroy()
        player1_roll_dice['state'] = 'disable'
        player1_trade['state'] = 'normal'
        player1_use_dev_card['state'] = 'normal'
        player1_build['state'] = 'normal'
        player1_end_turn['state'] = 'normal'
        player1_confirm['state'] = 'disable'
        player1_cancel['state'] = 'disable'

        # what happens after the 'confirm' button is clicked

    def confirm_bank():
        if v.get() == 'Brick':
            Player_1.brick +=2
            brick.set(Player_1.brick)
            year_of_plenty.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'

        elif v.get() == 'Lumber':
            Player_1.lumber += 2
            lumber.set(Player_1.lumber)
            year_of_plenty.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'

        elif v.get() == 'Wheat':
            Player_1.hay += 2
            hay.set(Player_1.hay)
            year_of_plenty.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'

        elif v.get() == 'Sheep':
            Player_1.sheep += 2
            sheep.set(Player_1.sheep)
        elif v.get() == 'Rock':
            Player_1.rock += 2
            rock.set(Player_1.rock)
            year_of_plenty.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'



        else:
            year_of_plenty.attributes('-topmost', 0)
            messagebox.showinfo("", "Choose a resource!")
            year_of_plenty.attributes('-topmost', 1)







    # Tkinter string variable
    # able to store any string value
    v = StringVar(year_of_plenty, "None")



    # Dictionary to create multiple buttons
    values_1 = {"Brick": "Brick",
                "Lumber": "Lumber",
                "Sheep": "Sheep",
                "Wheat": "Wheat",
                "Rock": "Rock"}

    y = 1

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for (text, value) in values_1.items():
        Radiobutton(year_of_plenty, width=10, text=text, variable=v,
                    value=value, indicator=0,
                    background="lightskyblue").grid(row=y, column=1, columnspan=1)
        y += 1


    # 'cancel' button inside this window
    cancel_bank = Button(year_of_plenty, width=3, height=1, bg='white', text=chr(10008), fg='red', \
                         font=('Times New Roman', 20), \
                         command=close_window).grid(row=6, column=1, columnspan=1, padx=10, pady=20, sticky=W)

    # 'confirm' button inside this window
    confirm_bank = Button(year_of_plenty, width=3, height=1, bg='white', text=chr(10003), fg='green', \
                          font=('Times New Roman', 20), \
                          command=confirm_bank).grid(row=6, column=1, columnspan=1, padx=10, pady=20, sticky=E)


#####################################################      function on clicking the "monopoly" development card                    ###########################################
                                                #          needs to have the buttons adjusted (confirm, cancel, radio buttons),
                                                #       after other player is made                                  ###################################################
def monopoly():
    player1_knight_card.place_forget()
    player1_year_of_plenty_card.place_forget()
    player1_build_road.place_forget()
    player1_build_settlement.place_forget()
    player1_build_city.place_forget()
    player1_buy_dev_card.place_forget()
    player1_road_building_card.place_forget()
    player1_monopoly_card.place_forget()

    player1_roll_dice['state'] = 'disable'
    player1_trade['state'] = 'disable'
    player1_use_dev_card['state'] = 'disable'
    player1_build['state'] = 'disable'
    player1_end_turn['state'] = 'disable'
    player1_confirm['state'] = 'disable'
    player1_cancel['state'] = 'disable'

    # Toplevel object which will
    # be treated as a new window
    year_of_plenty = Toplevel(root)

    #what happens when 'X' on the top bar is clicked
    def on_exit():
        player1_roll_dice['state'] = 'disable'
        player1_trade['state'] = 'normal'
        player1_use_dev_card['state'] = 'normal'
        player1_build['state'] = 'normal'
        player1_end_turn['state'] = 'normal'
        player1_confirm['state'] = 'disable'
        player1_cancel['state'] = 'disable'
        year_of_plenty.destroy()

    year_of_plenty.protocol("WM_DELETE_WINDOW", on_exit)


    # sets the title of the Toplevel widget
    year_of_plenty.title("Monopoly")

    # sets the geometry of toplevel
    year_of_plenty.geometry("300x300")

    # puts the new window in the center
    width = root.winfo_x()
    height = root.winfo_y()
    year_of_plenty.geometry("+%d+%d" % (width + 700, height + 400))

    # Make topLevelWindow remain on top until destroyed, or attribute changes.
    year_of_plenty.attributes('-topmost', 1)

    # A Label widget to show in toplevel - this 'dummy' label is made to put two other columns in the middle on the window
    Label(year_of_plenty, text="         ", font=("Times New Roman", 10), padx=10, pady=10).grid(row=0, column=0, columnspan=1)

    # A Label widget to show in toplevel
    Label(year_of_plenty, text="Take all of the selected resource\nfrom the opponent", font=("Times New Roman", 10), padx=10, pady=10).grid(row=0, column=1,
                                                                                                  columnspan=1)

    # funtion that closes  the "trade bank" new window

    def close_window():
        year_of_plenty.destroy()
        player1_roll_dice['state'] = 'disable'
        player1_trade['state'] = 'normal'
        player1_use_dev_card['state'] = 'normal'
        player1_build['state'] = 'normal'
        player1_end_turn['state'] = 'normal'
        player1_confirm['state'] = 'disable'
        player1_cancel['state'] = 'disable'

        # what happens after the 'confirm' button is clicked

    def confirm_bank():
        if v.get() == 'Brick':
            Player_1.brick +=2
            brick.set(Player_1.brick)
            year_of_plenty.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'

        elif v.get() == 'Lumber':
            Player_1.lumber += 2
            lumber.set(Player_1.lumber)
            year_of_plenty.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'

        elif v.get() == 'Wheat':
            Player_1.hay += 2
            hay.set(Player_1.hay)
            year_of_plenty.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'

        elif v.get() == 'Sheep':
            Player_1.sheep += 2
            sheep.set(Player_1.sheep)
        elif v.get() == 'Rock':
            Player_1.rock += 2
            rock.set(Player_1.rock)
            year_of_plenty.destroy()
            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'normal'
            player1_use_dev_card['state'] = 'normal'
            player1_build['state'] = 'normal'
            player1_end_turn['state'] = 'normal'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'



        else:
            year_of_plenty.attributes('-topmost', 0)
            messagebox.showinfo("", "Choose a resource!")
            year_of_plenty.attributes('-topmost', 1)







    # Tkinter string variable
    # able to store any string value
    v = StringVar(year_of_plenty, "None")



    # Dictionary to create multiple buttons
    values_1 = {"Brick": "Brick",
                "Lumber": "Lumber",
                "Sheep": "Sheep",
                "Wheat": "Wheat",
                "Rock": "Rock"}

    y = 1

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for (text, value) in values_1.items():
        Radiobutton(year_of_plenty, width=10, text=text, variable=v,
                    value=value, indicator=0,
                    background="lightskyblue").grid(row=y, column=1, columnspan=1)
        y += 1


    # 'cancel' button inside this window
    cancel_bank = Button(year_of_plenty, width=3, height=1, bg='white', text=chr(10008), fg='red', \
                         font=('Times New Roman', 20), \
                         command=close_window).grid(row=6, column=1, columnspan=1, padx=10, pady=20, sticky=W)

    # 'confirm' button inside this window
    confirm_bank = Button(year_of_plenty, width=3, height=1, bg='white', text=chr(10003), fg='green', \
                          font=('Times New Roman', 20), \
                          command=confirm_bank).grid(row=6, column=1, columnspan=1, padx=10, pady=20, sticky=E)




def end_turn():
    player1_knight_card.place_forget()
    player1_year_of_plenty_card.place_forget()
    player1_build_road.place_forget()
    player1_build_settlement.place_forget()
    player1_build_city.place_forget()
    player1_buy_dev_card.place_forget()
    player1_road_building_card.place_forget()
    player1_monopoly_card.place_forget()
    counter = False
    counter_dev_card = False

    player1_build["state"] = "disabled"

