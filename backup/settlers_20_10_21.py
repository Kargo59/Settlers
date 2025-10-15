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


import settlers_buttons_functions


#import modules to graph and to display the graph properly in Tkinter
from matplotlib import pyplot as plt
import networkx as nx
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as patches
from matplotlib.backend_bases import MouseButton





#creates a class 'Graph' as a blueprint for all the graphs that will be created
class Graph:
    global values_labels
    # values created here will be assigned to the nodes in the middle of hexagons and printed on the screen
    three_with_dots = 3
    values_labels = [11, 12, 9, 4, 6, 5, 10, 3, 11, 4, 8, 8, 10, 9, three_with_dots, 5, 2, 6, ' ']
    random.shuffle(values_labels)

    def __init__(self, option):
        self.option = option

    def create_graph(self):
        global x
        global f
        global dict_labels
        global pos
        global edges_only_middle_nodes

        coordinates = []
        f = plt.figure(figsize=(12, 9.9), facecolor='lightskyblue')
        a = f.add_subplot(1, 1, 1, facecolor='lightskyblue', frame_on=True,zorder=0)
        plt.axis('off')
        plt.gca().set_position([0, 0, 1, 1])

        G = nx.Graph()

        #first idea on how to change the node color based on the inner function 'onclick(event)
        #if len(coordinates) == 0:
        #    G.add_edge(1,3)


        # bottom row, first from the left tile
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_edge(3, 4)
        G.add_edge(4, 5)
        G.add_edge(5, 6)
        G.add_edge(1, 6)

        # bottom row, second from the left tile

        G.add_edge(5, 7)
        G.add_edge(7, 8)
        G.add_edge(8, 9)
        G.add_edge(9, 10)
        G.add_edge(10, 6)

        # bottom row, second from the left tile

        G.add_edge(8, 11)
        G.add_edge(11, 12)
        G.add_edge(12, 13)
        G.add_edge(13, 14)
        G.add_edge(9, 14)

        #second row from the bottom, starting from the left
        G.add_edge(3, 15)
        G.add_edge(15, 16)
        G.add_edge(16,17)
        G.add_edge(17,18)
        G.add_edge(4,18)

        G.add_edge(18,19)
        G.add_edge(19,20)
        G.add_edge(7,20)

        G.add_edge(20, 21)
        G.add_edge(21,22)
        G.add_edge(11,22)

        G.add_edge(22,23)
        G.add_edge(23,24)
        G.add_edge(24,25)
        G.add_edge(12,25)

        G.add_edge(16,26)
        G.add_edge(26,27)
        G.add_edge(27,28)
        G.add_edge(28,29)
        G.add_edge(17,29)

        G.add_edge(29,30)
        G.add_edge(30,31)
        G.add_edge(31,32)
        G.add_edge(19,31)

        G.add_edge(31,32)
        G.add_edge(32,33)
        G.add_edge(21,33)

        G.add_edge(33,34)
        G.add_edge(34,35)
        G.add_edge(23,35)

        G.add_edge(35,36)
        G.add_edge(36,37)
        G.add_edge(37,38)
        G.add_edge(24,38)

        G.add_edge(28,39)
        G.add_edge(39,40)
        G.add_edge(40,41)
        G.add_edge(30,41)

        G.add_edge(41,42)
        G.add_edge(42,43)
        G.add_edge(32,43)

        G.add_edge(43,44)
        G.add_edge(44,45)
        G.add_edge(34,45)

        G.add_edge(45,46)
        G.add_edge(46,47)
        G.add_edge(36,47)

        G.add_edge(40,48)
        G.add_edge(48,49)
        G.add_edge(49,50)
        G.add_edge(42,50)

        G.add_edge(50,51)
        G.add_edge(51,52)
        G.add_edge(44,52)

        G.add_edge(52,53)
        G.add_edge(53,54)
        G.add_edge(46,54)

        #edges between nodes in the middle of the graph and their direct neighbors
        #bottom row, first left
        for s in range(1, 7):
            G.add_edge('A', s)
        #bottom row, second left
        for s in range(5, 11):
            G.add_edge('B', s)
        #bottom row, third left
        for s in range(8, 10):
            G.add_edge('C', s)
        for s in range(11, 15):
            G.add_edge('C', s)
        # second from the bottom row, first left
        for s in range(3, 5):
            G.add_edge('D', s)
        for s in range(15, 19):
            G.add_edge('D', s)
        # second from the bottom row, second from the left
        e_edges = [4,5,7,18,19,20]
        for s in e_edges:
            G.add_edge('E', s)
        # second from the bottom row, third from the left
        f_edges = [7,8,11,20,21,22]
        for s in f_edges:
            G.add_edge('F', s)
        # second from the bottom row, fourth from the left
        g_edges = [11,12,22,23,24,25]
        for s in g_edges:
            G.add_edge('G', s)
        # middle row, first from the left
        h_edges = [16,17,26,27,28,29]
        for s in h_edges:
            G.add_edge('H', s)
        # middle row, second from the left
        i_edges = [17,18,19,29,30,31]
        for s in i_edges:
            G.add_edge('I', s)
        # middle row, third from the left
        j_edges = [19,20,21,31,32,33]
        for s in j_edges:
            G.add_edge('J', s)
        # middle row, fourth from the left
        k_edges = [21,22,23,33,34,35]
        for s in k_edges:
            G.add_edge('K', s)
        # middle row, fifth from the left
        l_edges = [23,24,35,36,37,38]
        for s in l_edges:
            G.add_edge('L', s)
        # second from the top row, first from the left
        m_edges = [28,29,30,39,40,41]
        for s in m_edges:
            G.add_edge('M', s)
        # second from the top row, second from the left
        n_edges = [30,31,32,41,42,43]
        for s in n_edges:
            G.add_edge('N', s)
        # second from the top row, third from the left
        o_edges = [32,33,34,43,44,45]
        for s in o_edges:
            G.add_edge('O', s)
        # second from the top row, fourth from the left
        p_edges = [34,35,36,45,46,47]
        for s in p_edges:
            G.add_edge('P', s)
        # first from the top row, first from the left
        q_edges = [40,41,42,48,49,50]
        for s in q_edges:
            G.add_edge('Q', s)
        # first from the top row, second from the left
        r_edges = [42,43,44,50,51,52]
        for s in r_edges:
            G.add_edge('R', s)
        # first from the top row, third from the left
        s_edges = [44,45,46,52,53,54]
        for s in s_edges:
            G.add_edge('S', s)

        #nodes in the middle of hexes
        G.add_node('A')
        G.add_node('B')
        G.add_node('C')
        G.add_node('D')
        G.add_node('E')
        G.add_node('F')
        G.add_node('G')
        G.add_node('H')
        G.add_node('I')
        G.add_node('J')
        G.add_node('K')
        G.add_node('L')
        G.add_node('M')
        G.add_node('N')
        G.add_node('O')
        G.add_node('P')
        G.add_node('Q')
        G.add_node('R')
        G.add_node('S')
        #harbors
        G.add_node('A1')
        G.add_node('A2')
        G.add_node('A3')
        G.add_node('A4')
        G.add_node('A5')
        G.add_node('A6')
        G.add_node('A7')
        G.add_node('A8')
        G.add_node('A9')






        # explicitly set positions
        pos = {
            # bottom row, first from the left
            1: (0, 0), 2: (-0.7, 0.7), 3: (-0.7, 1.7), 4: (0, 2.4), 5: (0.7, 1.7), 6: (0.7, 0.7),\
            # bottom row, second from the left
            7: (1.4, 2.4), 8: (2.1, 1.7), 9: (2.1, 0.7), 10: (1.4, 0),\
            # bottom row, third from the left
            11: (2.8, 2.4), 12: (3.5, 1.7), 13: (3.5, 0.7), 14: (2.8, 0), \
            # row second from the bottom, first from the left
            15: (-1.4, 2.4), 16: (-1.4, 3.4), 17: (-0.7, 4.1), 18: (0, 3.4),
            # row second from the bottom, second from the left
            19: (0.7, 4.1), 20: (1.4, 3.4),
            # row second from the bottom, third from the left
            21:(2.1, 4.1), 22:(2.8, 3.4),
            # row second from the bottom, fourth from the left
            23:(3.5,4.1), 24:(4.2,3.4), 25: (4.2, 2.4),\
            #middle row, first from the left
            26:(-2.1, 4.1), 27:(-2.1,5.1), 28:(-1.4,5.8), 29:(-0.7,5.1),
            # middle row, second from the left
            30:(0, 5.8), 31:(0.7,5.1),
            # middle row, third from the left
            32:(1.4,5.8), 33: (2.1,5.1),
            # middle row, fourth from the left
            34:(2.8,5.8), 35:(3.5,5.1),
            # middle row, fifth from the left
            36:(4.2,5.8), 37:(4.9,5.1), 38:(4.9,4.1),\
            # second row from the top, first from the left
            39:(-1.4,6.8), 40:(-0.7,7.5), 41:(0,6.8),
            # second row from the top, second from the left
            42:(0.7,7.5), 43:(1.4,6.8),
            # second row from the top, third from the left
            44:(2.1,7.5), 45:(2.8,6.8),
            # second row from the top, fourth from the left
            46:(3.5,7.5), 47:(4.2,6.8),\
            # first row from the top, first from the left
            48:(-0.7,8.5),49:(0,9.2),50:(0.7,8.5),
            # first row from the top, second from the left
            51:(1.4,9.2), 52:(2.1,8.5),
            # first row from the top, third from the left
            53:(2.8,9.2), 54:(3.5,8.5),\
            #nodes in the middle of hexagons
            'A': (0, 1.2), 'B': (1.4, 1.2), 'C': (2.8, 1.2),\
            'D': (-0.7, 2.9), 'E': (0.7, 2.9), 'F': (2.1, 2.9), 'G': (3.5, 2.9),\
            'H': (-1.4, 4.6), 'I': (0, 4.6), 'J': (1.4, 4.6), 'K': (2.8, 4.6), 'L': (4.2, 4.6), \
            'M': (-0.7, 6.3), 'N': (0.7, 6.3), 'O': (2.1, 6.3), 'P': (3.5, 6.3), \
            'Q': (0, 8), 'R': (1.4, 8), 'S': (2.8, 8),\
            #harbors
            'A1': (-0.6, 0),'A2': (-1.75, 2.95),'A3': (-1.75, 6.3),'A4': (-0.55, 9.2),'A5': (2, 9.2),\
            'A6': (4, 7.55),'A7': (5.2, 4.65),'A8': (4.05, 1.65),'A9': (1.95, 0)
        }


        #creates two lists with x and y coordinates for each node - it will be used to build polygons in
        #hexagons_polygons dictionary below
        #these lists can probably be thrown away
        positions_list_x = []
        for x in range(1,55):
            positions_list_x.append(pos[x][0])
        positions_list_y = []
        for x in range(1,55):
            positions_list_y.append(pos[x][1])


        #builds hexagons based on x,y coordinates of nodes
        hexagons_polygons = {
            1: {"1": positions_list_x[0:6],
                       "2": positions_list_y[0:6]},
            2: {"1": [0.7, 0.7, 1.4, 2.1, 2.1, 1.4],
                       "2": [0.7, 1.7, 2.4, 1.7, 0.7, 0]},
            3: {"1": [2.1,2.1,2.8,3.5,3.5,2.8],
                      "2": [0.7,1.7,2.4,1.7,0.7,0]},
            4: {"1": [-0.7,-1.4,-1.4,-0.7,0,0],
                "2": [1.7,2.4,3.4,4.1,3.4,2.4]},
            5: {"1": [0.7,0,0,0.7,1.4,1.4],
                 "2": [1.7,2.4,3.4,4.1,3.4,2.4]},
            6: {"1": [2.1,1.4,1.4,2.1,2.8,2.8],
                 "2": [1.7,2.4,3.4,4.1,3.4,2.4]},
            7: {"1": [3.5,2.8,2.8,3.5,4.2,4.2],
                 "2": [1.7,2.4,3.4,4.1,3.4,2.4]},
            8: {"1": [-1.4,-2.1,-2.1,-1.4,-0.7,-0.7],
                 "2": [3.4,4.1,5.1,5.8,5.1,4.1]},
            9: {"1": [0,-0.7,-0.7,0,0.7,0.7],
                "2": [3.4,4.1,5.1,5.8,5.1,4.1]},
            10: {"1": [1.4,0.7,0.7,1.4,2.1,2.1],
                "2": [3.4,4.1,5.1,5.8,5.1,4.1]},
            11: {"1": [2.8,2.1,2.1,2.8,3.5,3.5],
                 "2": [3.4,4.1,5.1,5.8,5.1,4.1]},
            12: {"1": [4.2,3.5,3.5,4.2,4.9,4.9],
                 "2": [3.4,4.1,5.1,5.8,5.1,4.1]},
            13: {"1": [-0.7,-1.4,-1.4,-0.7,0,0],
                 "2": [5.1, 5.8,6.8,7.5,6.8,5.8]},
            14: {"1": [0.7,0,0,0.7,1.4,1.4],
                 "2": [5.1,5.8,6.8,7.5,6.8,5.8]},
            15: {"1": [2.1,1.4,1.4,2.1,2.8,2.8],
                 "2": [5.1,5.8,6.8,7.5,6.8,5.8]},
            16: {"1": [3.5,2.8,2.8,3.5,4.2,4.2],
                 "2": [5.1,5.8,6.8,7.5,6.8,5.8]},
            17: {"1": [0,-0.7,-0.7,0,0.7,0.7],
                "2": [6.8,7.5,8.5,9.2,8.5,7.5]},
            18: {"1": [1.4,0.7,0.7,1.4,2.1,2.1],
                "2": [6.8,7.5,8.5,9.2,8.5,7.5]},
            19: {"1": [2.8,2.1,2.1,2.8,3.5,3.5],
                "2": [6.8,7.5,8.5,9.2,8.5,7.5]}

                             }


        #fills the polygons with color based on updated_nodes.dict_hex_colors dictionary
        for x in hexagons_polygons:
            plt.fill("1", "2", updated_nodes.dict_hex_colors[x], alpha=0.7, edgecolor= None, lw=2, ls= 'solid', zorder=0, data=hexagons_polygons[x])

        #fills up the hexagons with colors according to the resources assigned to them based on 'updated_dict-resources'
        #x = np.arange(-0.75, 1.75, 1)
        #y = np.arange(1, 2, 1)
        #plt.fill_between(x, y, color='blue')


        #list to store the settings to display the right colors of the nodes depending on the situation
        color_map = []




        # draws the bordes of the nodes that are NOT in the middle of hexagons
        linewidths_list = []

        for count, node in list(enumerate(G)):
            if type(node) == int:
                linewidths_list.append(0)
            elif type(node) != int:
                linewidths_list.append(0)
            else:
                linewidths_list.append(0)

        list(enumerate(G))




        # adjusts the borders - draws the bordes of the nodes that have cities or settlements on them
        for z in updated_nodes.dict_prop:
            if updated_nodes.dict_prop[z] == 'settlement_player_1' or \
                    updated_nodes.dict_prop[z] == 'settlement_player_2' or \
                    updated_nodes.dict_prop[z] == 'city_player_1' or \
                    updated_nodes.dict_prop[z] == 'city_player_2':
                linewidths_list[z - 1] = 2
            else:
                linewidths_list[z - 1] = 0


        ################################################        options for displaying the graph        ##################################################

          #########################################################             normal graph        ##############################################################
        if self.__dict__['option'] == 'normal':

            #draws the nodes in the middle - most of them are gold, if 7 was rolled or knight card was played then
            #one of them is gray


            mids = [a for a in list(G.nodes)]
            mids = [b for b in mids if type(b) == str and len(b) == 1]
            middle_nodes = []
            for enum, h in list(enumerate(mids)):
                if updated_nodes.dict_mid_nodes_for_robber[h] == 'None' and updated_nodes.dict_hex_colors[enum+1] != 'navajowhite':
                    middle_nodes.append('gold')
                elif updated_nodes.dict_hex_colors[enum+1] == 'navajowhite':
                    middle_nodes.append('None')
                    middle_nodes.remove('None')
                    # del middle_nodes[enum]

                else:
                    middle_nodes.append('gray')

            # specifying different colors for the nodes that are not in the middle
            for node in G:
                if type(node) == int:
                    if updated_nodes.dict_prop[node] == 'settlement_player_1':
                        color_map.append('blue')
                    elif updated_nodes.dict_prop[node] == 'settlement_player_2':
                        color_map.append('violet')
                    elif updated_nodes.dict_prop[node] == 'city_player_1':
                        color_map.append('blue')
                    elif updated_nodes.dict_prop[node] == 'city_player_2':
                        color_map.append('violet')
                    else:
                        color_map.append('None')
                else:
                    color_map.append('None')






            options = {
                "font_size": 0,
                "node_size": 1900,
                #"node_color": "white",
                "edgecolors": "black",
                "linewidths": linewidths_list,
                "width": 5,
                'node_shape': 'o'
            }
            edge_color_map = []
            for edge in updated_nodes.dict_prop_roads:
                if updated_nodes.dict_prop_roads[edge] == 'road_player_1':
                    edge_color_map.append('blue')
                elif updated_nodes.dict_prop_roads[edge] == 'road_player_2':
                    edge_color_map.append('violet')
                else:
                    edge_color_map.append('black')


            #'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
            x = ['normal']




        #graph drawing options for the case when a settlement is to be built
        if updated_nodes.turn % 2 != 0 or updated_nodes.turn % 2 == 0:

            if self.__dict__['option'] == 'settlement':


                edges_for_graphing = list(G.edges)

                # specifying different colors for the nodes that have letters assigned to them
                if updated_nodes.turn != 0:
                    for node in G:
                        if type(node) == int:
                            if updated_nodes.dict_prop[node] == 'settlement_player_1':
                                #print(node)
                                color_map.append('blue')
                                # print(list(G.neighbors(node)))
                            elif updated_nodes.dict_prop[node] == 'settlement_player_2':
                                color_map.append('violet')
                            elif updated_nodes.dict_prop[node] == 'city_player_1':
                                color_map.append('blue')
                            elif updated_nodes.dict_prop[node] == 'city_player_2':
                                color_map.append('violet')
                            else:
                                color_map.append('None')
                        else:
                            color_map.append('None')


                    # for node in G:
                    #     if type(node) == int:
                    #         print(tuple(G.neighbors(node)))

                    #print(list(enumerate(color_map)))
                    #print(updated_nodes.dict_prop)

                    #print(updated_nodes.dict_prop)
                    for edge in G.edges:
                        if updated_nodes.dict_prop_roads[edge] == 'road_player_1':
                            #print(edge)
                            for element in edge:
                                if updated_nodes.dict_prop[element] != 'settlement_player_1' and updated_nodes.dict_prop[element] != 'city_player_1'\
                                and updated_nodes.dict_prop[element] != 'settlement_player_2' and updated_nodes.dict_prop[element] != 'city_player_2':
                                    neighbors_to_build_settlements = tuple(G.neighbors(element))
                                    #print(neighbors_to_build_settlements)

                                    if len(neighbors_to_build_settlements) == 2:
                                        if updated_nodes.dict_prop[neighbors_to_build_settlements[0]] != 'settlement_player_1' and\
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[1]] != 'settlement_player_1' and\
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[0]] != 'city_player_1' and\
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[1]] != 'city_player_1' and\
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[0]] != 'settlement_player_2' and\
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[1]] != 'settlement_player_2' and\
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[0]] != 'city_player_2' and\
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[1]] != 'city_player_2':

                                            color_map[element - 1] = ('yellow')

                                    elif len(neighbors_to_build_settlements) == 3:
                                        if updated_nodes.dict_prop[neighbors_to_build_settlements[0]] != 'settlement_player_1' and\
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[1]] != 'settlement_player_1' and \
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[2]] != 'settlement_player_1' and \
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[0]] != 'settlement_player_2' and \
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[1]] != 'settlement_player_2' and \
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[2]] != 'settlement_player_2' and \
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[0]] != 'city_player_1' and \
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[1]] != 'city_player_1' and \
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[2]] != 'city_player_1' and \
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[0]] != 'city_player_2' and \
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[1]] != 'city_player_2' and \
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[2]] != 'city_player_2':

                                            # print(element)
                                            color_map[element-1] = ('yellow')



                            #print(list(enumerate(color_map)))

                            # if updated_nodes.dict_prop[node] == 'settlement_player_1':
                            #     neighbors_edges = []
                            #     neighbors_edges_main = []
                            #     #for element in list(G.neighbors(node)):
                            #     #    neighbors_edges.append([node, element])
                            #     neighbors_edges = [[node, element] for element in list(G.neighbors(node))]
                            #     for edge in neighbors_edges:
                            #          edge.sort()
                            #     #print(neighbors_edges)
                            #
                            #
                            #     for element_2 in neighbors_edges:
                            #          if updated_nodes.dict_prop_roads[(tuple(element_2))] == 'road_player_1':
                            #              color_map[element_2[1] - 1] = ('lightskyblue')

                    # print(color_map)

                    # print(updated_nodes.dict_prop_roads.keys())
                    # print(updated_nodes.dict_prop_roads)


                #adjust the border width of the node that is available to build settlement on
                for index, color in list(enumerate(color_map)):
                    if color_map[index] == 'yellow':
                        linewidths_list[index] = 2

                options = {
                    "font_size": 0,
                    "node_size": 1900,
                    #"node_color": "blue",
                    "edgecolors": "black",
                    "linewidths": linewidths_list,
                    "width": 5,
                }
                edge_color_map = []
                for edge in updated_nodes.dict_prop_roads:
                    if updated_nodes.dict_prop_roads[edge] == 'road_player_1':
                        edge_color_map.append('blue')
                    elif updated_nodes.dict_prop_roads[edge] == 'road_player_2':
                        edge_color_map.append('violet')
                    else:
                        edge_color_map.append('black')                #'x' is a parameter needed for the for the 'cancel selection' fun)ction outside of this class to work
                x = ['settlement']

            elif self.__dict__['option'] == 'confirm_settlement':
                color_map = color_map_red

                #adjust the border width of the node that was chosen to build settlement on
                for index, color in list(enumerate(color_map)):
                    if color_map[index] == 'red':
                        linewidths_list[index] = 2

                options = {
                    "font_size": 0,
                    "node_size": 1900,
                    # "node_color": "blue",
                    "edgecolors": "black",
                    "linewidths": linewidths_list,
                    "width": 5,
                }
                edge_color_map = []
                for edge in updated_nodes.dict_prop_roads:
                    if updated_nodes.dict_prop_roads[edge] == 'road_player_1':
                        edge_color_map.append('blue')
                    elif updated_nodes.dict_prop_roads[edge] == 'road_player_2':
                        edge_color_map.append('violet')
                    else:
                        edge_color_map.append('black')

                #'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
                x = ['confirm_settlement']


            # graph drawing options for the case when a city is to be built
            elif self.__dict__['option'] == 'city':
                if updated_nodes.turn % 2 != 0:                             #situation for player number 1

                    # specifying different colors for the nodes that have letters assigned to them
                    for node in G:
                        if type(node) == int:
                            if updated_nodes.dict_prop[node] == 'settlement_player_1':
                                # print(node)
                                color_map.append('yellow')
                                # print(list(G.neighbors(node)))
                            elif updated_nodes.dict_prop[node] == 'settlement_player_2':
                                color_map.append('violet')
                            elif updated_nodes.dict_prop[node] == 'city_player_1':
                                color_map.append('blue')
                            elif updated_nodes.dict_prop[node] == 'city_player_2':
                                color_map.append('violet')
                            else:
                                color_map.append('None')
                        else:
                            color_map.append('None')

                    options = {
                        "font_size": 0,
                        "node_size": 1900,
                        # "node_color": "blue",
                        "edgecolors": "black",
                        "linewidths": linewidths_list,
                        "width": 5,
                    }
                    edge_color_map = []
                    for edge in updated_nodes.dict_prop_roads:
                        if updated_nodes.dict_prop_roads[edge] == 'road_player_1':
                            edge_color_map.append('blue')
                        elif updated_nodes.dict_prop_roads[edge] == 'road_player_2':
                            edge_color_map.append('violet')
                        else:
                            edge_color_map.append('black')

                    # 'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
                    x = ['city']

                if updated_nodes.turn % 2 == 0:

                    # specifying different colors for the nodes that have letters assigned to them
                    for node in G:
                        if node in updated_nodes.dict_prop:
                            if updated_nodes.dict_prop[node] == 'settlement_player_2':
                                color_map.append('green')
                            else:
                                color_map.append('white')
                        else:
                            color_map.append('yellow')

                    options = {
                        "font_size": 0,
                        "node_size": 1900,
                        # "node_color": "blue",
                        "edgecolors": "black",
                        "linewidths": linewidths_list,
                        "width": 5,
                    }
                    edge_color_map = ['black']
                    # 'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
                    x = ['city']


            elif self.__dict__['option'] == 'confirm_city':
                color_map = color_map_red
                options = {
                    "font_size": 0,
                    "node_size": 1900,
                    # "node_color": "blue",
                    "edgecolors": "black",
                    "linewidths": linewidths_list,
                    "width": 5,
                }
                edge_color_map = []
                for edge in updated_nodes.dict_prop_roads:
                    if updated_nodes.dict_prop_roads[edge] == 'road_player_1':
                        edge_color_map.append('blue')
                    elif updated_nodes.dict_prop_roads[edge] == 'road_player_2':
                        edge_color_map.append('violet')
                    else:
                        edge_color_map.append('black')
                # 'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
                x = ['confirm_city']


            elif self.__dict__['option'] == 'road':

                for node in G:
                    if type(node) == int:
                        if updated_nodes.dict_prop[node] == 'settlement_player_1':
                            color_map.append('blue')
                        elif updated_nodes.dict_prop[node] == 'settlement_player_2':
                            color_map.append('violet')
                        elif updated_nodes.dict_prop[node] == 'city_player_1':
                            color_map.append('blue')
                        elif updated_nodes.dict_prop[node] == 'city_player_2':
                            color_map.append('violet')
                        else:
                            color_map.append('None')
                    else:
                        color_map.append('None')

                options = {
                    "font_size": 0,
                    "node_size": 1900,
                    # "node_color": "blue",
                    "edgecolors": "black",
                    "linewidths": linewidths_list,
                    "width": 5,
                }
                edge_color_map = []
                edges_list = (list(G.edges))
                #print(edges_list)
                for x in edges_list:
                    # print(x[1])
                    if updated_nodes.turn % 2 != 0:
                        if updated_nodes.dict_prop_roads[x] == 'road_player_1':
                            edge_color_map.append('blue')

                            # for x[1] in edges_list:
                            #     if x[1] in updated_nodes.dict_prop_roads[x]:
                            #         print(updated_nodes.dict_prop_roads[x])

                            # neighbors_edges = [[x, element] for element in list(G.neighbors(x))]
                            # for edge in neighbors_edges:
                            #     edge.sort()
                            # print(neighbors_edges)



                        elif updated_nodes.dict_prop_roads[x] == 'road_player_2':
                            edge_color_map.append('violet')

                        elif updated_nodes.dict_prop[x[0]] == 'settlement_player_1' or updated_nodes.dict_prop[x[1]] == 'settlement_player_1'\
                        or updated_nodes.dict_prop[x[0]] == 'city_player_1' or updated_nodes.dict_prop[x[1]] == 'city_player_1':
                            edge_color_map.append('yellow')
                        else:
                            edge_color_map.append('black')
                    else:
                        if updated_nodes.dict_prop[x[0]] == 'settlement_player_2' or updated_nodes.dict_prop[
                            x[1]] == 'settlement_player_2' \
                                or updated_nodes.dict_prop[x[0]] == 'city_player_2' or updated_nodes.dict_prop[
                            x[1]] == 'city_player_2':
                            edge_color_map.append('yellow')
                        else:
                            edge_color_map.append('black')

                for r in edges_list:
                    # print(x[1])
                    if updated_nodes.turn % 2 != 0:
                        if updated_nodes.dict_prop_roads[r] == 'road_player_1':

                            #print(r)
                            #print(r[1])
                            list_enumerate = list(G.edges)
                            enumerate_prime = enumerate(list_enumerate)
                            list_enumerate_prime = list(enumerate_prime)
                            #print(list(G.nodes))
                            # print(updated_nodes.dict_prop_roads)
                            available_roads_init = list(G.edges([r[1]]))
                            for j in G.edges([r[0]]):
                                available_roads_init.append(j)
                            #print(available_roads_init)
                            available_roads_init_sorted = []
                            for u in available_roads_init:
                                new_u = sorted(u)
                                available_roads_init_sorted.append(new_u)
                            available_roads_init = []
                            for i in available_roads_init_sorted:
                                available_roads_init.append(tuple(i))
                                #print(available_roads_init)
                                #print(updated_nodes.dict_prop_roads.keys())
                            for d in available_roads_init:
                                if updated_nodes.dict_prop_roads[d] != 'road_player_1' and updated_nodes.dict_prop_roads[d] != 'road_player_2':
                                    for item in list_enumerate_prime:
                                        if d == item[1]:
                                            #print(item[0])
                                            #print(d)
                                            edge_color_map[item[0]] = 'yellow'
                                    #print(updated_nodes.dict_prop_roads)

                            #print(available_roads_init)
                            #print(edge_color_map)
                            #print(list_enumerate_prime)









                #'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
                x = ['road']


            elif self.__dict__['option'] == 'confirm_road':
                for node in G:
                    if type(node) == int:
                        if updated_nodes.dict_prop[node] == 'settlement_player_1':
                            color_map.append('blue')
                        elif updated_nodes.dict_prop[node] == 'settlement_player_2':
                            color_map.append('violet')
                        elif updated_nodes.dict_prop[node] == 'city_player_1':
                            color_map.append('blue')
                        elif updated_nodes.dict_prop[node] == 'city_player_2':
                            color_map.append('violet')
                        else:
                            color_map.append('None')
                    else:
                        color_map.append('None')

                options = {
                    "font_size": 0,
                    "node_size": 1900,
                    # "node_color": "blue",
                    "edgecolors": "black",
                    "linewidths": linewidths_list,
                    "width": 5,
                }

                edge_color_map = edge_color_map_road
                #'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
                x = ['confirm_road']


#####################################################         ###################    graph after knight card is played #######################################################

            # the graph created when the'knight card' button is clicked
            if self.__dict__['option'] == 'knight_card':

                # specifying different colors for the nodes that are not in the middle...
                for node in G:
                    if type(node) == int:
                        if updated_nodes.dict_prop[node] == 'settlement_player_1':
                            color_map.append('blue')
                        elif updated_nodes.dict_prop[node] == 'settlement_player_2':
                            color_map.append('violet')
                        elif updated_nodes.dict_prop[node] == 'city_player_1':
                            color_map.append('blue')
                        elif updated_nodes.dict_prop[node] == 'city_player_2':
                            color_map.append('violet')
                        else:
                            color_map.append('None')
                    else:
                        color_map.append('None')


                middle_node_colors_knight_card = ['gold' for x in range(19)]

                print(updated_nodes.dict_mid_nodes_for_robber)
                print(list(enumerate(updated_nodes.dict_mid_nodes_for_robber)))
                print('fixing the robber')

                #finds nodes attached to the opponent and makes them available to be blocked (assigns black color to them)
                for enum, node in list(enumerate(G, start=-54)):
                    index = 0
                    if type(node) == str and len(node) == 1:
                        print(enum, node)
                        #print(list(G.neighbors(node)))
                        for c in list(G.neighbors(node)):
                            if (updated_nodes.dict_prop[c] == 'settlement_player_2' or updated_nodes.dict_prop[c] == 'city_player_2')\
                                and updated_nodes.dict_mid_nodes_for_robber[node] != 'robber':
                                middle_node_colors_knight_card[enum] = 'gray'



                #removes the color from the node containing the desert
                for enum, node in list(enumerate(G, start=-53)):
                    index = 0
                    if type(node) == str and len(node) == 1:
                        #print(enum, node)
                        if updated_nodes.dict_hex_colors[enum] == 'navajowhite':
                            #print('here')
                            middle_node_colors_knight_card[enum-1] = 'None'
                            # del middle_node_colors_knight_card[enum-1]

                print(middle_node_colors_knight_card)
                print('jajajajala')




                options = {
                    "font_size": 0,
                    "node_size": 1900,
                    # "node_color": "white",
                    "edgecolors": "black",
                    "linewidths": linewidths_list,
                    "width": 5,
                    'node_shape': 'o'
                }
                edge_color_map = []
                for edge in updated_nodes.dict_prop_roads:
                    if updated_nodes.dict_prop_roads[edge] == 'road_player_1':
                        edge_color_map.append('blue')
                    elif updated_nodes.dict_prop_roads[edge] == 'road_player_2':
                        edge_color_map.append('violet')
                    else:
                        edge_color_map.append('black')

                # 'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
                x = ['normal']


                player1_trade["state"] = "disabled"
                player1_use_dev_card["state"] = "disabled"
                player1_build["state"] = "disabled"
                player1_end_turn["state"] = "disabled"
                player1_roll_dice["state"] = "disabled"
                player1_cancel['state'] = 'disabled'
                player1_confirm['state'] = 'disabled'




###############################        "confirm knight card graph" - graph after chosing a node after playing the knight card         ##################################3

            # the graph created when the'knight card' button is clicked
            if self.__dict__['option'] == 'confirm_knight_card':

                # specifying different colors for the nodes that are not in the middle...
                for node in G:
                    if type(node) == int:
                        if updated_nodes.dict_prop[node] == 'settlement_player_1':
                            color_map.append('blue')
                        elif updated_nodes.dict_prop[node] == 'settlement_player_2':
                            color_map.append('violet')
                        elif updated_nodes.dict_prop[node] == 'city_player_1':
                            color_map.append('blue')
                        elif updated_nodes.dict_prop[node] == 'city_player_2':
                            color_map.append('violet')
                        else:
                            color_map.append('None')
                    else:
                        color_map.append('None')

                #
                # middle_node_colors_knight_card = ['gold' for x in range(19)]
                # print('lalala')
                # print(updated_nodes.dict_hex_colors)
                # for key in updated_nodes.dict_hex_colors:
                #     if updated_nodes.dict_hex_colors[key] == 'navajowhite':
                #         middle_node_colors_knight_card[key-1] = 'None'
                #
                #
                #
                # print(middle_node_colors_knight_card)



                middle_node_colors_knight_card_red = middle_node_knight_card_red
                print('sss')
                print(middle_node_colors_knight_card_red)
                print('sth')
                print(list(enumerate(G, start=-53)))

                #removes the color from the node containing the desert
                for enum, node in list(enumerate(G, start=-53)):
                    index = 0
                    if type(node) == str and len(node) == 1:
                        print(enum, node)
                        if updated_nodes.dict_hex_colors[enum] == 'navajowhite':
                            print(updated_nodes.dict_hex_colors[enum])
                            middle_node_colors_knight_card_red[enum-1] = 'None'

                print(updated_nodes.dict_hex_colors)
                print('sfsfesd')
                print(middle_node_colors_knight_card_red)


                #finds nodes attached to the opponent and makes them available to be blocked (assigns black color to them)
                for enum, node in list(enumerate(G, start=-54)):
                    index = 0
                    if type(node) == str and len(node) == 1:
                        #print(enum, node)
                        #print(list(G.neighbors(node)))
                        for c in list(G.neighbors(node)):
                            if (updated_nodes.dict_prop[c] == 'settlement_player_2' or updated_nodes.dict_prop[c] == 'city_player_2') \
                                    and middle_node_colors_knight_card_red[enum] != 'red' and  middle_node_colors_knight_card_red[enum] != 'None':
                                #print(enum, node)
                                middle_node_colors_knight_card_red[enum] = 'gold'

                print(middle_node_colors_knight_card_red)


                options = {
                    "font_size": 0,
                    "node_size": 1900,
                    # "node_color": "white",
                    "edgecolors": "black",
                    "linewidths": linewidths_list,
                    "width": 5,
                    'node_shape': 'o'
                }
                edge_color_map = []
                for edge in updated_nodes.dict_prop_roads:
                    if updated_nodes.dict_prop_roads[edge] == 'road_player_1':
                        edge_color_map.append('blue')
                    elif updated_nodes.dict_prop_roads[edge] == 'road_player_2':
                        edge_color_map.append('violet')
                    else:
                        edge_color_map.append('black')


                # 'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
                x = ['confirm_knight_card']


                player1_trade["state"] = "disabled"
                player1_use_dev_card["state"] = "disabled"
                player1_build["state"] = "disabled"
                player1_end_turn["state"] = "disabled"
                player1_roll_dice["state"] = "disabled"
                player1_cancel['state'] = 'normal'
                player1_confirm['state'] = 'normal'





########################################       general rules for displaying the graphs              ##############################################


        #creates labels for the nodes that have letters assigned to them, gives them a random integer value
        keys_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']

        # creates a dictionary for the harbor nodes - will be used to draw these selected nodes separately with labels
        keys_labels_harbors = ['A1', 'A2','A3', 'A4','A5', 'A6','A7', 'A8','A9']
        values_labels_harbors = ['3:1', 'Wheat\n2:1', 'Rock\n2:1','3:1','Sheep\n2:1','3:1','3:1', 'Brick\n2:1','Wood\n2:1']

        harbors = dict(zip(keys_labels_harbors,values_labels_harbors))



        #list updated every time a new settlement is created - will be used to display nodes having settlements on them
        keys_settlements_cities = [x for x in updated_nodes.dict_prop if updated_nodes.dict_prop[x] == 'settlement_player_1' \
                            or updated_nodes.dict_prop[x] == 'city_player_1'\
                            or updated_nodes.dict_prop[x] == 'settlement_player_2'\
                            or updated_nodes.dict_prop[x] == 'city_player_2']

        colors_settlements_cities = []
        for elem in keys_settlements_cities:
            if updated_nodes.dict_prop[elem] == 'settlement_player_1':
                colors_settlements_cities.append('blue')
            elif updated_nodes.dict_prop[elem] == 'settlement_player_2':
                colors_settlements_cities.append('violet')





        dict_labels = dict(zip(keys_labels, values_labels))

        #assigns the 'desert' (or really an empty value) value to the desert hexagon,\
        # if 'desert' taken away from other hex -> swaps values
        desert_update = list(dict_labels)
        for e in updated_nodes.dict_hex_colors:
            if updated_nodes.dict_hex_colors[e] == 'navajowhite':
                if dict_labels[desert_update[e-1]] != ' ':
                    swap = dict_labels[desert_update[e-1]]
                    dict_labels[desert_update[e-1]] = ' '
                    for y in dict_labels:
                        if dict_labels[y] == ' ' and y != desert_update[e-1]:
                            dict_labels[y] = swap

        #cancels drawing of the 'desert' node
        for e in dict_labels:
            if dict_labels[e] == ' ':
                y = desert_update.index(e)
                keys_labels.remove(keys_labels[y])

        #draws only the edges connecting nodes on the vertices of the hexagons withour drawing the ones in the middle of hexes
        edges_no_middle_nodes = [v for v in list(G.edges) if isinstance(v[0], int) and isinstance(v[1], int)]

        # edges_no_middle_nodes = []
        # for v in list(G.edges):
        #     if isinstance(v[0], int) and isinstance(v[1], int):
        #         edges_no_middle_nodes.append(v)

        #lists only the edges in the middle of hexes
        edges_only_middle_nodes = [v for v in list(G.edges) if isinstance(v[0], str) or isinstance(v[1], str)]
        #print(edges_only_middle_nodes)

###################################################           drawing of the graph         #########################################################################3

        edgelist = edges_no_middle_nodes

        # plots the nodes and edges on the graph
        nx.draw_networkx(G, pos, edge_color=edge_color_map, edgelist=edgelist, node_color=color_map, **options, ax=a)
        #draws the labels for the nodes that have letters assigned to them - shows the numerical value assigned to them randomly
        nx.draw_networkx_labels(G, pos, labels=dict_labels, font_size=16)
        #displays the golden nodes in the middle of hexes
        if self.__dict__['option'] != 'knight_card' and self.__dict__['option'] != 'confirm_knight_card':
            nx.draw_networkx_nodes(G, pos, nodelist=keys_labels, node_size=2000, node_color= middle_nodes, edgecolors='black')
        elif self.__dict__['option'] == 'knight_card':
            middle_node_colors_knight_card.remove('None')
            nx.draw_networkx_nodes(G, pos, nodelist=keys_labels, node_size=2000, node_color=middle_node_colors_knight_card, edgecolors='black')
        elif self.__dict__['option'] == 'confirm_knight_card':
            middle_node_colors_knight_card_red.remove(middle_node_colors_knight_card_red[y])
            nx.draw_networkx_nodes(G, pos, nodelist=keys_labels, node_size=2000, node_color=middle_node_colors_knight_card_red, edgecolors='black')
        #draws harbors
        nx.draw_networkx_nodes(G, pos, nodelist=keys_labels_harbors, node_size=2000, node_shape='h', node_color='white', edgecolors='black')
        #draws the labels for the harbor nodes
        nx.draw_networkx_labels(G, pos, labels=harbors, font_size=11)

        #displays nodes that have settlements or cities on them
        #nx.draw_networkx_nodes(G, pos, nodelist=keys_settlements_cities, node_size=2000, node_color=colors_settlements_cities, edgecolors='black')







        # Set margins for the axes so that nodes aren't clipped
        # ax = plt.gca()
        # ax.margins(0.20)
        # plt.axis("off")



        # create matplotlib canvas using figure f / graph `G`  and assign to widget `board frame`
        self.canvas = FigureCanvasTkAgg(f, master=board_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column=1, row=0)
        #self.canvas.get_tk_widget().place(relx=0.2, rely=0)



###########################################################       this section defines actions that happen when graph is clicked
        #                                                           (on playing the knight card or building stuff)          #####################################################



        #function to get the coordinates when clicked on the graph
        def on_click(event):
            global color_map_red_old
            global color_map_red
            global middle_node_knight_card_red
            if event.button is MouseButton.LEFT and self.__dict__['option'] == 'settlement':
                global key_settlement
                x, y = event.x, event.y
                ax = event.inaxes  # the axes instance;
                #print('Coordinates: %f %f' % (event.xdata, event.ydata))
                #add a function here later that clears the list 'coordinates' if it is not empty
                coordinates.append(event.xdata)
                coordinates.append(event.ydata)
                #print(coordinates)
                #print(color_map)
                self.clearPlotPage()
                # prints the list of nodes - I can use it later to select the node to be colored red - should it be highlighted here?

                # highlights the node that was clicked by the player
                coordinates_tuple = tuple(coordinates)
                #print(coordinates_tuple)
                #print(pos.values())
                # finding the dictionary 'pos' values that are closest to the coordinates clicked by the player
                positions = []
                positions_first_element = []
                positions_second_element = []
                for value in iter(pos.values()):
                    positions.append(value)
                #print(list(enumerate(positions)))
                # breaking down the 'position' list of list into two lists: one with first elements of 'positions',
                # the other one with second elements of that list
                for x in positions:
                    positions_first_element.append(x[0])
                for x in positions:
                    positions_second_element.append(x[1])

                #print(positions_first_element)
                #print(positions_second_element)
                #find the nodes (in the dictionary 'pos') that are closest to the elements that were just clicked
                if coordinates[0] != None and coordinates[1] != None:
                    a = (min(positions_first_element, key=lambda x: abs(x - coordinates[0])))
                    b = (min(positions_second_element, key=lambda x: abs(x - coordinates[1])))
                else:
                    a = 0               #later write a function to disable the confirm button if clicked at the wrong spot
                    b = 0

                coordinates_tuple = (a, b)
                #print(coordinates_tuple)
                #print(updated_nodes.dict_prop)
                #creates a list needed to update the values for 'settlement' or 'city' within the 'Graph_Properties' class
                #later will create function that will turn the confirm button off if clicked in the spot that was not allowed
                key_settlement = [w for w in pos if pos[w] == coordinates_tuple]

                #create a list to contain information about which node was clicked
                color_map_red = []

                # assigns the value 'red' in the color_map (which is used to color the nodes in the graph)
                # and leaves other values as they were
                try:
                    for i in pos:
                        if pos[i] == coordinates_tuple and color_map[i-1] == 'yellow' and coordinates[0] != None\
                                and updated_nodes.dict_prop[i] != 'settlement_player_2' and updated_nodes.dict_prop[i] !='city_player_2':
                            color_map_red.append('red')
                        elif pos[i] == coordinates_tuple and color_map[i-1] != 'yellow'and coordinates[0] == None:
                            color_map_red.append('None')
                        elif pos[i] == coordinates_tuple and color_map[i-1] != 'yellow'and coordinates[0] != None:
                            color_map_red.append('None')
                        elif pos[i] != coordinates_tuple and type(i) == int:
                            color_map_red.append('None')
                        elif pos[i] != coordinates_tuple and type(i) == str:
                            color_map_red.append('None')
                except TypeError or ValueError or AttributeError:
                    settlement_graph.create_graph()


                #print(color_map_red)

                # color_map_red = ['red' if pos[i] == coordinates_tuple and updated_nodes.dict_prop[i] == 'settlement_player_1'\
                #                      else 'white' if type(i) == int else 'yellow' for i in pos]

                #check which settlements and cities were already built by both players and adjust the 'color_map_red' accordingly
                for node in G:
                    if type(node) == int:
                        if updated_nodes.dict_prop[node] == 'settlement_player_1':
                            color_map_red[node-1] = ('blue')
                        elif updated_nodes.dict_prop[node] == 'settlement_player_2':
                            color_map_red[node-1] = ('violet')
                        elif updated_nodes.dict_prop[node] == 'city_player_1':
                            color_map_red[node - 1] = ('blue')
                        elif updated_nodes.dict_prop[node] == 'city_player_2':
                            color_map_red[node - 1] = ('violet')



                # create a list'color map red old' to compare it with the newly created color map red list - if they are not the same,
                # the player hasn't clicked the red node and the program will not allow it
                #will be used later for the case when the player builds a city
                color_map_red_old = color_map_red

                if 'red' in color_map_red:
                    confirm_settlement_graph.create_graph()
                else:
                    settlement_graph.create_graph()

            if event.button is MouseButton.LEFT and self.__dict__['option'] == 'city':
                global key_city
                x, y = event.x, event.y
                ax = event.inaxes  # the axes instance; is this expression necessary?
                # print('Coordinates: %f %f' % (event.xdata, event.ydata))
                # add a function here later that clears the list 'coordinates' if it is not empty
                coordinates.append(event.xdata)
                coordinates.append(event.ydata)
                self.clearPlotPage()
                # prints the list of nodes - I can use it later to select the node to be colored red - should it be highlighted here?
                # print(list(G.nodes))
                # print(pos)
                # highlights the node that was clicked by the player
                coordinates_tuple = tuple(coordinates)
                # print(coordinates_tuple)
                # print(pos.values())
                # finding the dictionary 'pos' values that are closest to the coordinates clicked by the player
                positions = []
                positions_first_element = []
                positions_second_element = []
                for value in iter(pos.values()):
                    positions.append(value)
                # breaking down the 'position' list of list into two lists: one with first elements of 'positions',
                # the other one with second elements of that list
                for x in positions:
                    positions_first_element.append(x[0])
                for x in positions:
                    positions_second_element.append(x[1])

                # print(positions_first_element)
                # print(positions_second_element)
                #find the nodes (in the dictionary 'pos') that are closest to the elements that were just clicked
                if coordinates[0] != None and coordinates[1] != None:
                    a = (min(positions_first_element, key=lambda x: abs(x - coordinates[0])))
                    b = (min(positions_second_element, key=lambda x: abs(x - coordinates[1])))
                else:
                    a = 0               #later write a function to disable the confirm button if clicked at the wrong spot
                    b = 0

                coordinates_tuple = (a, b)

                # print(pos)
                # print(positions)
                # print(coordinates_tuple)
                # positions_index = positions.index(coordinates_tuple)
                # print(positions_index)

                # creates a list needed to update the values for 'settlement' or 'city' within the 'Graph_Properties' class
                key_city = [w for w in pos if pos[w] == coordinates_tuple]

                # assigns the value 'red' in the color_map (which is used to color the nodes in the graph)
                # and leaves other values as they were
                color_map_red = []

                try:
                    for i in pos:
                        if pos[i] == coordinates_tuple and color_map[i-1] == 'yellow' and coordinates[0] != None:
                            color_map_red.append('red')
                        elif pos[i] == coordinates_tuple and color_map[i - 1] != 'yellow' and coordinates[0] == None:
                            color_map_red.append('None')
                        elif pos[i] == coordinates_tuple and color_map[i - 1] != 'yellow' and coordinates[0] != None:
                            color_map_red.append('None')
                        elif pos[i] != coordinates_tuple and type(i) == int:
                            color_map_red.append('None')
                        elif pos[i] != coordinates_tuple and type(i) == str:
                            color_map_red.append('None')
                except TypeError or ValueError or AttributeError:
                    color_map_red = ['None' for multiplicator in range(73)]

                #print(color_map_red)
                #print(len(color_map_red))
                #print(len(pos))

                #color_map_red = ['red' if pos[i] == coordinates_tuple else 'white' if type(i) == int else 'yellow' for i in pos]

                #check which settlements and cities were already built by both players and adjust the 'color_map_red' accordingly
                for node in G:
                    if type(node) == int:
                        if updated_nodes.dict_prop[node] == 'settlement_player_1' and color_map_red[node-1] != 'red':
                            color_map_red[node-1] = ('blue')
                        elif updated_nodes.dict_prop[node] == 'settlement_player_2':
                            color_map_red[node-1] = ('violet')
                        elif updated_nodes.dict_prop[node] == 'city_player_1':
                            color_map_red[node - 1] = ('blue')
                        elif updated_nodes.dict_prop[node] == 'city_player_2':
                            color_map_red[node - 1] = ('violet')


                # print(color_map_red)
                #if color_map_red_old[positions_index] == 'red':
                if 'red' in color_map_red:
                    confirm_city_graph.create_graph()
                else:
                    city_graph.create_graph()



            if event.button is MouseButton.LEFT and self.__dict__['option'] == 'road':
                global edge_color_map_road
                global key_edges
                x, y = event.x, event.y
                ax = event.inaxes
                #print('Coordinates: %f %f' % (event.xdata, event.ydata))
                # add a function here later that clears the list 'coordinates' if it is not empty
                coordinates.append(event.xdata)
                coordinates.append(event.ydata)
                self.clearPlotPage()
                # for each edge it takes the respective values in the dictionary 'pos' and makes an average out of them.
                # will be used later to click the edges that a player wants to build a road on
                edges = list(G.edges)

                list_pos = [[pos[y] for y in x] for x in edges]

                list_pos_first_element = [[y[0] for y in x] for x in list_pos]
                list_pos_second_element = [[y[1] for y in x] for x in list_pos]

                avg_first_element = [sum(x) / len(x) for x in list_pos_first_element]
                avg_second_element = [sum(x) / len(x) for x in list_pos_second_element]
                if coordinates[0] != None and coordinates[1] != None:
                    a = (min(avg_first_element, key=lambda x: abs(x - coordinates[0])))
                    b = (min(avg_second_element, key=lambda x: abs(x - coordinates[1])))
                else:
                    a = 999               #later write a function to disable the confirm button if clicked at the wrong spot
                    b = 999


                coordinates_tuple = (a, b)

                # for x in list_pos_first_element:
                #     if sum(x)/len(x) == coordinates_tuple[0]:
                #         print('True')
                #     else:
                #         print('False')
                #
                #
                # for x in list_pos_second_element:
                #     if sum(x) / len(x) == coordinates_tuple[1]:
                #         print('True')
                #     else:
                #         print('False')
                #
                list_pos_first_element_matching = ['True' if sum(x)/len(x) == coordinates_tuple[0] else 'False' for x in list_pos_first_element]
                list_pos_second_element_matching = ['True' if sum(x)/len(x) == coordinates_tuple[1] else 'False' for x in list_pos_second_element]

                final_list=[]
                for x, y in zip(list_pos_first_element_matching, list_pos_second_element_matching):
                    if x == 'True':
                        if y == 'True':
                            final_list.append('True')
                        else:
                            final_list.append('False')
                    else:
                            final_list.append('False')

                #print(final_list)

                index_edges = []

                for index, item in enumerate(final_list):
                    if item == 'True':
                        index_edges.append(index)

                #print(index_edges)
                if len(index_edges) > 0:
                    key_edges = edges[index_edges[0]] # defines a variable used later to update dictionary with 'road' property
                    #print(key_edges)

                edge_color_map_road = []

                if len(index_edges) == 0:
                    coord_edges = ['None']
                elif len(index_edges) > 0:
                    coord_edges = edges[index_edges[0]]

                #print(edges)
                #print(list(enumerate(edge_color_map)))
                edge_color_map_enumerated = list(enumerate(edge_color_map))
                #print(list(enumerate(edges)))
                print(coord_edges)
                #print(updated_nodes.dict_prop_roads)

                #final step to compare the list with all edges to the edge clicked. when the edge is found it is marked red
                for x in edges:
                    if x == coord_edges:
                        for a, b in list(enumerate(edges)):
                            if b == coord_edges and edge_color_map[a] == 'yellow':
                                #print(a)
                                edge_color_map_road.append('red')
                            elif b == coord_edges and edge_color_map[a] == 'violet':
                                edge_color_map_road.append('violet')
                            elif b == coord_edges and edge_color_map[a] != 'yellow':
                                edge_color_map_road.append('black')
                    elif b ==coord_edges and edge_color_map[a] == 'road_player_2':
                        edge_color_map.append('violet')
                    elif updated_nodes.dict_prop_roads[x] == 'road_player_1':
                        edge_color_map_road.append('blue')
                    elif updated_nodes.dict_prop_roads[x] == 'road_player_2':
                        edge_color_map_road.append('violet')
                    else:
                        edge_color_map_road.append('black')

                if coord_edges == ['None'] or 'red' not in edge_color_map_road:
                    edge_color_map_road = edge_color_map

                print(edge_color_map_road)


                # in case a player clicked somewhere outside of graph - later make a pop up message saying 'didn't catch it, try again'
                #print(edge_color_map_road)
                confirm_road_graph.create_graph()


                # nx.draw_networkx(G, pos, node_color=color_map_red, **options, ax=a)
                #
                # self.canvas = FigureCanvasTkAgg(f, master=board_frame)
                # self.canvas.draw()
                # self.canvas.get_tk_widget().pack()


#######################################  draws the graph with red node highlighted, to be blocked by a knight card      ###################################################

            if event.button is MouseButton.LEFT and self.__dict__['option'] == 'knight_card':
                global key_knight_card
                x, y = event.x, event.y
                ax = event.inaxes  # the axes instance;
                # print('Coordinates: %f %f' % (event.xdata, event.ydata))
                # add a function here later that clears the list 'coordinates' if it is not empty
                coordinates.append(event.xdata)
                coordinates.append(event.ydata)
                print(coordinates)
                self.clearPlotPage()

                # highlights the node that was clicked by the player

                coordinates_tuple = tuple(coordinates)
                # print(coordinates_tuple)
                # finding the dictionary 'pos' values that are closest to the coordinates clicked by the player
                positions = []
                for key in pos:
                    if type(key) == str and len(key) == 1:
                        positions.append(pos[key])

                positions_first_element = []
                positions_second_element = []

                # breaking down the 'position' list of list into two lists: one with first elements of 'positions',
                # the other one with second elements of that list
                for x in positions:
                    positions_first_element.append(x[0])
                for x in positions:
                    positions_second_element.append(x[1])

                # print(positions_first_element)
                # print(positions_second_element)
                # find the nodes (in the dictionary 'pos') that are closest to the elements that were just clicked
                if coordinates[0] != None and coordinates[1] != None:
                    a = (min(positions_first_element, key=lambda x: abs(x - coordinates[0])))
                    b = (min(positions_second_element, key=lambda x: abs(x - coordinates[1])))
                else:
                    a = 0  # later write a function to disable the confirm button if clicked at the wrong spot
                    b = 0

                coordinates_tuple = (a, b)
                print(coordinates_tuple)
                for h in coordinates_tuple:
                    if len(str(h)) > 2:
                        if str(h)[2] == 9:
                            print('nein')
                        else:
                            round(h,1)
                    else:
                        round(h, 1)

                # creates a list needed to update the values for 'settlement' or 'city' within the 'Graph_Properties' class
                # later will create function that will turn the confirm button off if clicked in the spot that was not allowed
                key_knight_card = [w for w in pos if pos[w] == coordinates_tuple]
                print(key_knight_card)
                # create a list to contain information about which node was clicked
                color_map_red = []

                edges_only_middle_nodes_letter_only = list(set([l for g,l in edges_only_middle_nodes]))
                edges_only_middle_nodes_letter_only = list(enumerate(sorted(edges_only_middle_nodes_letter_only)))

                print('were here')
                print(middle_node_colors_knight_card)

                for u in edges_only_middle_nodes_letter_only:
                    if updated_nodes.dict_hex_colors[(u[0]) + 1] == 'navajowhite':
                        middle_node_colors_knight_card.insert(int(u[0]), 'None')

                print(middle_node_colors_knight_card)
                print(edges_only_middle_nodes_letter_only)
                print(updated_nodes.dict_hex_colors)


                try:
                    middle_node_knight_card_red = []

                    for u in edges_only_middle_nodes_letter_only:
                        print(updated_nodes.dict_hex_colors[(u[0])+1])
                        if updated_nodes.dict_hex_colors[(u[0])+1] == 'navajowhite':
                            middle_node_knight_card_red.append('None')
                        elif updated_nodes.dict_hex_colors[(u[0])+1] != 'navajowhite' and key_knight_card == (list(u[1])) and middle_node_colors_knight_card[int(u[0])] == 'gray':
                            print('yay')
                            middle_node_knight_card_red.append('red')
                        else:
                            middle_node_knight_card_red.append('gold')

                    # middle_node_knight_card_red.remove('None')

                    print(middle_node_knight_card_red)
                    print('and now here')
                    # if updated_nodes.dict_hex_colors[enum] == 'navajowhite':
                    #     print(updated_nodes.dict_hex_colors[enum])
                    #     middle_node_colors_knight_card_red[enum - 1] = 'None'



                    confirm_knight_card_graph.create_graph()

                except IndexError or TypeError or ValueError or AttributeError:
                    start_graph.create_graph()



                # color_map_red = ['red' if pos[i] == coordinates_tuple and updated_nodes.dict_prop[i] == 'settlement_player_1'\
                #                      else 'white' if type(i) == int else 'yellow' for i in pos]

                # check which settlements and cities were already built by both players and adjust the 'color_map_red' accordingly
                # for node in G:
                #     if type(node) == int:
                #         if updated_nodes.dict_prop[node] == 'settlement_player_1':
                #             color_map_red[node - 1] = ('blue')
                #         elif updated_nodes.dict_prop[node] == 'settlement_player_2':
                #             color_map_red[node - 1] = ('violet')
                #         elif updated_nodes.dict_prop[node] == 'city_player_1':
                #             color_map_red[node - 1] = ('blue')
                #         elif updated_nodes.dict_prop[node] == 'city_player_2':
                #             color_map_red[node - 1] = ('violet')

                # create a list'color map red old' to compare it with the newly created color map red list - if they are not the same,
                # the player hasn't clicked the red node and the program will not allow it
                # will be used later for the case when the pl``ayer builds a city
                # color_map_red_old = color_map_red

                # if 'red' in middle_node_knight_card_red:
                #     confirm_knight_card_graph.create_graph()
                #     print('confirm_knight_graph')
                # else:
                #     start_graph.create_graph()

        #connect 'button press event' with on_click function, can later be disconnected with:
        #plt.disconnect(cid)
        cid = plt.connect('button_press_event', on_click)


    #clear the canvas to prepare for the next version of the graph
    def clearPlotPage(self):
        self.canvas.get_tk_widget().pack_forget()

    # cancels
    # the action and goes back to the normal view
    def cancel_selection(self):
        self.clearPlotPage()
        start_graph.create_graph()


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





#########################################################          prepare the main window              #####################################################


root = Tk()
root.geometry('500x400')
root.title('Settlers of Catan')
root.state('zoomed')
root.configure(bg='lightskyblue')


#frame for the board
board_frame = Frame(root, width=1200, height=1000, bg='lightskyblue', highlightbackground=None, borderwidth=0, highlightcolor=None, highlightthickness=0)
#board_frame.grid(column=1, columnspan=3, row=0, rowspan=3, padx=0, pady=13)
board_frame.place(x=300, y=0)


#frame for player 1
# player1_frame = Frame(root, width=650, height=485, bg='sienna4', highlightbackground='black', borderwidth=0, highlightcolor='blue', highlightthickness=2)
# #player1_frame.grid(column=1, row=0, padx=100, pady=10, sticky='sw')
# # player1_frame = Frame(board_frame, width=650, height=485, bg='brown', highlightbackground='black', borderwidth=0, highlightcolor='blue', highlightthickness=2)
# player1_frame.pack()
# player1_frame.place(x=60, y=50)


#name of player 1
player1_name = Label(root, width = 20, height=2, bg='lightskyblue', text='Player 1', font=('Times New Roman', 20, 'italic', 'bold'))
player1_name.place(x=100, y=20)

#player 1 - resources label
player1_resource = Label(root, width = 9, height=2, bg='lightskyblue', text='Resources:', font=('Times New Roman', 17, 'italic'))
player1_resource.place(x=10, y=70)


#player 1 - hay
player1_hay = Label(root, width = 5, height=2, bg='lightskyblue', text='Wheat', font=('Times New Roman', 15, 'italic'))
player1_hay.place(x=10, y=160)

hay = StringVar()
hay.set(Player_1.hay)
#player 1 - displays the current number of hay cards
player1_hay_score = Label(root, width = 3, height=1, bg='white', textvariable= hay, font=('Times New Roman', 15, 'italic'))
player1_hay_score.place(x=80, y=172)

#player 1 - brick
player1_brick = Label(root, width = 5, height=2, bg='lightskyblue', text='Brick', font=('Times New Roman', 15, 'italic'))
player1_brick.place(x=130, y=160)

brick = StringVar()
brick.set(Player_1.brick)
#player 1 - displays the current number of brick cards
player1_brick_score = Label(root, width = 3, height=1, bg='white', textvariable= brick, font=('Times New Roman', 15, 'italic'))
player1_brick_score.place(x=195, y=172)

#player 1 - sheep
player1_sheep = Label(root, width = 5, height=2, bg='lightskyblue', text='Sheep:', font=('Times New Roman', 15, 'italic'))
player1_sheep.place(x=250, y=160)

sheep = StringVar()
sheep.set(Player_1.sheep)
#player 1 - displays the current number of sheep cards
player1_sheep_score = Label(root, width = 3, height=1, bg='white', textvariable= sheep, font=('Times New Roman', 15, 'italic'))
player1_sheep_score.place(x=310, y=172)

#player 1 - rock
player1_rock = Label(root, width = 5, height=2, bg='lightskyblue', text='Rock:', font=('Times New Roman', 15, 'italic'))
player1_rock.place(x=180, y=115)

rock = StringVar()
rock.set(Player_1.rock)
#player 1 - displays the current number of rock cards
player1_rock_score = Label(root, width = 3, height=1, bg='white', textvariable= rock, font=('Times New Roman', 15, 'italic'))
player1_rock_score.place(x=250, y=125)

#player 1 - lumber
player1_lumber = Label(root, width = 6, height=2, bg='lightskyblue', text='Lumber:', font=('Times New Roman', 15, 'italic'))
player1_lumber.place(x=24, y=115)

lumber = StringVar()
lumber.set(Player_1.lumber)

#player 1 - displays the current number of lumber cards
player1_lumber_score = Label(root, width = 3, height=1, bg='white', textvariable= lumber, font=('Times New Roman', 15, 'italic'))
player1_lumber_score.place(x=120, y=125)


#player 1 - trade button
player1_trade = Button(root, width = 20, height=1, bg='white', text= 'Trade', font=('Times New Roman', 15, 'italic'), command=settlers_buttons_functions.trade, state = 'disable')
player1_trade.place(x=10, y=220)

#trade with merchant button - submenu of "Trade" button!
player1_trade_merchant = Button(root, width=20, height=1, bg='white', text='Merchant', font=('Times New Roman', 15, 'italic'), command=settlers_buttons_functions.trade_merchant)

#trade with bank button - submenu of "Trade" button!
player1_trade_bank = Button(root, width=20, height=1, bg='white', text='Bank', font=('Times New Roman', 15, 'italic'), command=settlers_buttons_functions.trade_bank)


#player 1 - use development card button
player1_use_dev_card = Button(root, width = 20, height=1, bg='white', text= 'Play Development Card', font=('Times New Roman', 15, 'italic'),\
                              command=settlers_buttons_functions.dev_card, state = 'disable')
player1_use_dev_card.place(x=10, y=270)

#player 1 - build button
player1_build = Button(root, width = 20, height=1, bg='white', text= 'Build / Buy', font=('Times New Roman', 15, 'italic'),\
                       command=settlers_buttons_functions.click_build, state = 'disable')
player1_build.place(x=10, y=320)

#button for building settlement - submenu of "build" button!
player1_build_settlement = Button(root, width=20, height=1, bg='white', text='Settlement', font=('Times New Roman', 15, 'italic'))

#build a city button - submenu of "build" button!
player1_build_city = Button(root, width=20, height=1, bg='white', text='Upgrade To a City', font=('Times New Roman', 15, 'italic'))

#build a road button - submenu of "build" button!
player1_build_road = Button(root, width=20, height=1, bg='white', text='Road', font=('Times New Roman', 15, 'italic'), command=settlers_buttons_functions.build_road)

#buy a dev card button - submenu of "build" button!

player1_buy_dev_card = Button(root, width=20, height=1, bg='white', text='Buy a Development Card', font=('Times New Roman', 15, 'italic'))

#use a knight card button - submenu of "Play dev card" button! - replace the text with StrVar like in resources
player1_knight_card = Button(root, width=20, height=1, bg='white', text='Knight Card', font=('Times New Roman', 15, 'italic'), command=settlers_buttons_functions.knight_card)

#use a 'year of plenty' card button - submenu of "Play dev card" button!
player1_year_of_plenty_card = Button(root, width=20, height=1, bg='white', text='Year of Plenty', font=('Times New Roman', 15, 'italic'), command=settlers_buttons_functions.year_of_plenty)

#use a 'Road building' card button - submenu of "Play dev card" button!
player1_road_building_card = Button(root, width=20, height=1, bg='white', text='Road building', font=('Times New Roman', 15, 'italic'))

#use a 'Road building' card button - submenu of "Play dev card" button!
player1_road_building_card = Button(root, width=20, height=1, bg='white', text='Road building', font=('Times New Roman', 15, 'italic'))

#use a 'Monopoly' card button - submenu of "Play dev card" button!
player1_monopoly_card = Button(root, width=20, height=1, bg='white', text='Monopoly', font=('Times New Roman', 15, 'italic'), command=settlers_buttons_functions.monopoly)


#player 1 - End Turn button
player1_end_turn = Button(root, width = 20, height=1, bg='white', text= 'End Turn', font=('Times New Roman', 15, 'italic'), command=settlers_buttons_functions.end_turn, state = 'disable')
player1_end_turn.place(x=10, y=370)

#player 1 - Cancel button
player1_cancel = Button(root, width = 3, height=1, bg='white', text=chr(10008), fg='red', font=('Times New Roman', 30),\
                        command = settlers_buttons_functions.cancel_selection, state = 'disable')
player1_cancel.place(x=10, y=420)

#player 1 - Confirm button
player1_confirm = Button(root, width = 3, height=1, bg='white', text=chr(10003), fg='green', font=('Times New Roman', 30), state='disable', command=settlers_buttons_functions.confirm_selection)
player1_confirm.place(x=100, y=420)

#player 1 - Roll dice button
player1_roll_dice = Button(root, width = 20, height=1, bg='white', text= 'Roll dice', font=('Times New Roman', 15, 'italic'), command = settlers_buttons_functions.roll_dice, state='normal')
player1_roll_dice.place(x=10, y=520)
# player1_roll_dice.bind('<Button-1>', roll_dice)

# player 1 - 'dummy' (empty) result of the first roll
player1_roll_1_empty = Label(root, width=3, height=1, bg='white', text=' ', font=('Times New Roman', 30))
player1_roll_1_empty.place(x=10, y=570)

# player 1 - displays the result of the other roll
player1_roll_2_empty = Label(root, width=3, height=1, bg='white', text=' ', font=('Times New Roman', 30), state='normal')
player1_roll_2_empty.place(x=100, y=570)





##########################################          frame for player 2            ######################################################################


player2_frame = Frame(root, width=650, height=585, bg='burlywood4', highlightbackground='black', borderwidth=1, highlightcolor='black', highlightthickness=2)
#player2_frame.grid(column=2, row=0, padx=10, pady=10, ipady=0, sticky=NW)
player2_frame.place(x=1450, y=500)
#player2_frame.lift()

#name of player 2
player2_name = Label(player2_frame, width = 43, bg='white', text='Player 2 name')
player2_name.grid(row=0, column=0, padx=10, pady=10)

#Player's 2 resources
player2_resources = Label(player2_frame, width=30, bg='white', text='Resources')
player2_resources.grid(row=1, column=0, padx=10, pady=10)

#Player's 2 Development Cards
player2_devcards = Label(player2_frame, width=30, bg='white', text='Development Cards')
player2_devcards.grid(row=2, column=0, padx=10, pady=10)

#Player's 2 Actions - change to a separate frame later!
player2_actions = Label(player2_frame, width=30, bg='white', text='Actions this turn')
player2_actions.grid(row=3, column=0, padx=10, pady=10)

#Player's 2 Button 'Build a settlement'
player2_build_settlement = Button(player2_frame, width=30, bg='white', text='Build settlement', command=settlers_buttons_functions.change_view_settlement)
player2_build_settlement.grid(row=4, column=0, padx=10, pady=10)

#Player's 2 Button 'Upgrade to a city'
player2_build_settlement = Button(player2_frame, width=30, bg='white', text='Upgrade to a city', command=settlers_buttons_functions.change_view_city)
player2_build_settlement.grid(row=5, column=0, padx=10, pady=10)

#Player's 2 Button 'Build a a Road'
player2_build_settlement = Button(player2_frame, width=30, bg='white', text='Build a road', command=settlers_buttons_functions.build_road)
player2_build_settlement.grid(row=6, column=0, padx=10, pady=10)

#Player's 2 'Confirm Action' Button
player2_confirm_button = Button(player2_frame, width=30, bg='white', text='Confirm Action', command=settlers_buttons_functions.confirm_selection)
player2_confirm_button.grid(row=7, column=0, padx=10, pady=10)

#Player's 2 'Cancel Action' Button
player2_confirm_button = Button(player2_frame, width=30, bg='white', text='Cancel Action', command=settlers_buttons_functions.cancel_selection)
player2_confirm_button.grid(row=8, column=0, padx=10, pady=10)

#Player's 2 'End Turn' Button
player2_end_turn = Button(player2_frame, width=30, bg='white', text='End Turn', command=settlers_buttons_functions.end_turn)
player2_end_turn.grid(row=9, column=0, padx=10, pady=10)

#creating instances of the Class 'Graph' with different settings in brackets to display different views
start_graph = Graph('normal')
settlement_graph = Graph('settlement')
city_graph = Graph('city')
confirm_settlement_graph = Graph('confirm_settlement')
confirm_city_graph = Graph('confirm_city')
road_graph = Graph('road')
confirm_road_graph = Graph('confirm_road')
#draws the board where options to block opponent with knight card are shown
knight_card_graph = Graph('knight_card')
#graph with one node colored red (chosen by player who played the 'knight card')
confirm_knight_card_graph = Graph('confirm_knight_card')
#confirm_knight_card = Graph('confirm_knight_card')


#initializing the game by creating the 'start_graph'
start_graph.create_graph()

#list to keep the coordinates when nodes on the graph are clicked
coordinates = []


root.mainloop()