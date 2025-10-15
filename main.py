import math
import tkinter

from tkinter import messagebox
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from pathlib import Path
from collections import Counter

import random
from math import floor

import networkx
import numpy as np

# import modules to graph and to display the graph properly in Tkinter
from matplotlib import pyplot as plt
import networkx as nx
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as patches
from matplotlib.backend_bases import MouseButton

import buy_development_card


# creates a class 'Graph' as a blueprint for all the graphs that will be created
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
        f = plt.figure(figsize=(10.4, 8.9), facecolor='lightskyblue')
        a = f.add_subplot(1, 1, 1, facecolor='lightskyblue', frame_on=True, zorder=0)
        plt.axis('off')
        plt.gca().set_position([0, 0, 1, 1])

        G = nx.Graph()

        # first idea on how to change the node color based on the inner function 'onclick(event)
        # if len(coordinates) == 0:
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

        # second row from the bottom, starting from the left
        G.add_edge(3, 15)
        G.add_edge(15, 16)
        G.add_edge(16, 17)
        G.add_edge(17, 18)
        G.add_edge(4, 18)

        G.add_edge(18, 19)
        G.add_edge(19, 20)
        G.add_edge(7, 20)

        G.add_edge(20, 21)
        G.add_edge(21, 22)
        G.add_edge(11, 22)

        G.add_edge(22, 23)
        G.add_edge(23, 24)
        G.add_edge(24, 25)
        G.add_edge(12, 25)

        G.add_edge(16, 26)
        G.add_edge(26, 27)
        G.add_edge(27, 28)
        G.add_edge(28, 29)
        G.add_edge(17, 29)

        G.add_edge(29, 30)
        G.add_edge(30, 31)
        G.add_edge(31, 32)
        G.add_edge(19, 31)

        G.add_edge(31, 32)
        G.add_edge(32, 33)
        G.add_edge(21, 33)

        G.add_edge(33, 34)
        G.add_edge(34, 35)
        G.add_edge(23, 35)

        G.add_edge(35, 36)
        G.add_edge(36, 37)
        G.add_edge(37, 38)
        G.add_edge(24, 38)

        G.add_edge(28, 39)
        G.add_edge(39, 40)
        G.add_edge(40, 41)
        G.add_edge(30, 41)

        G.add_edge(41, 42)
        G.add_edge(42, 43)
        G.add_edge(32, 43)

        G.add_edge(43, 44)
        G.add_edge(44, 45)
        G.add_edge(34, 45)

        G.add_edge(45, 46)
        G.add_edge(46, 47)
        G.add_edge(36, 47)

        G.add_edge(40, 48)
        G.add_edge(48, 49)
        G.add_edge(49, 50)
        G.add_edge(42, 50)

        G.add_edge(50, 51)
        G.add_edge(51, 52)
        G.add_edge(44, 52)

        G.add_edge(52, 53)
        G.add_edge(53, 54)
        G.add_edge(46, 54)

        # edges between nodes in the middle of the graph and their direct neighbors
        # bottom row, first left
        for s in range(1, 7):
            G.add_edge('A', s)
        # bottom row, second left
        for s in range(5, 11):
            G.add_edge('B', s)
        # bottom row, third left
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
        e_edges = [4, 5, 7, 18, 19, 20]
        for s in e_edges:
            G.add_edge('E', s)
        # second from the bottom row, third from the left
        f_edges = [7, 8, 11, 20, 21, 22]
        for s in f_edges:
            G.add_edge('F', s)
        # second from the bottom row, fourth from the left
        g_edges = [11, 12, 22, 23, 24, 25]
        for s in g_edges:
            G.add_edge('G', s)
        # middle row, first from the left
        h_edges = [16, 17, 26, 27, 28, 29]
        for s in h_edges:
            G.add_edge('H', s)
        # middle row, second from the left
        i_edges = [17, 18, 19, 29, 30, 31]
        for s in i_edges:
            G.add_edge('I', s)
        # middle row, third from the left
        j_edges = [19, 20, 21, 31, 32, 33]
        for s in j_edges:
            G.add_edge('J', s)
        # middle row, fourth from the left
        k_edges = [21, 22, 23, 33, 34, 35]
        for s in k_edges:
            G.add_edge('K', s)
        # middle row, fifth from the left
        l_edges = [23, 24, 35, 36, 37, 38]
        for s in l_edges:
            G.add_edge('L', s)
        # second from the top row, first from the left
        m_edges = [28, 29, 30, 39, 40, 41]
        for s in m_edges:
            G.add_edge('M', s)
        # second from the top row, second from the left
        n_edges = [30, 31, 32, 41, 42, 43]
        for s in n_edges:
            G.add_edge('N', s)
        # second from the top row, third from the left
        o_edges = [32, 33, 34, 43, 44, 45]
        for s in o_edges:
            G.add_edge('O', s)
        # second from the top row, fourth from the left
        p_edges = [34, 35, 36, 45, 46, 47]
        for s in p_edges:
            G.add_edge('P', s)
        # first from the top row, first from the left
        q_edges = [40, 41, 42, 48, 49, 50]
        for s in q_edges:
            G.add_edge('Q', s)
        # first from the top row, second from the left
        r_edges = [42, 43, 44, 50, 51, 52]
        for s in r_edges:
            G.add_edge('R', s)
        # first from the top row, third from the left
        s_edges = [44, 45, 46, 52, 53, 54]
        for s in s_edges:
            G.add_edge('S', s)

        # nodes in the middle of hexes
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

        # harbors
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
            1: (0, 0), 2: (-0.7, 0.7), 3: (-0.7, 1.7), 4: (0, 2.4), 5: (0.7, 1.7), 6: (0.7, 0.7), \
            # bottom row, second from the left
            7: (1.4, 2.4), 8: (2.1, 1.7), 9: (2.1, 0.7), 10: (1.4, 0), \
            # bottom row, third from the left
            11: (2.8, 2.4), 12: (3.5, 1.7), 13: (3.5, 0.7), 14: (2.8, 0), \
            # row second from the bottom, first from the left
            15: (-1.4, 2.4), 16: (-1.4, 3.4), 17: (-0.7, 4.1), 18: (0, 3.4),
            # row second from the bottom, second from the left
            19: (0.7, 4.1), 20: (1.4, 3.4),
            # row second from the bottom, third from the left
            21: (2.1, 4.1), 22: (2.8, 3.4),
            # row second from the bottom, fourth from the left
            23: (3.5, 4.1), 24: (4.2, 3.4), 25: (4.2, 2.4), \
            # middle row, first from the left
            26: (-2.1, 4.1), 27: (-2.1, 5.1), 28: (-1.4, 5.8), 29: (-0.7, 5.1),
            # middle row, second from the left
            30: (0, 5.8), 31: (0.7, 5.1),
            # middle row, third from the left
            32: (1.4, 5.8), 33: (2.1, 5.1),
            # middle row, fourth from the left
            34: (2.8, 5.8), 35: (3.5, 5.1),
            # middle row, fifth from the left
            36: (4.2, 5.8), 37: (4.9, 5.1), 38: (4.9, 4.1), \
            # second row from the top, first from the left
            39: (-1.4, 6.8), 40: (-0.7, 7.5), 41: (0, 6.8),
            # second row from the top, second from the left
            42: (0.7, 7.5), 43: (1.4, 6.8),
            # second row from the top, third from the left
            44: (2.1, 7.5), 45: (2.8, 6.8),
            # second row from the top, fourth from the left
            46: (3.5, 7.5), 47: (4.2, 6.8), \
            # first row from the top, first from the left
            48: (-0.7, 8.5), 49: (0, 9.2), 50: (0.7, 8.5),
            # first row from the top, second from the left
            51: (1.4, 9.2), 52: (2.1, 8.5),
            # first row from the top, third from the left
            53: (2.8, 9.2), 54: (3.5, 8.5), \
            # nodes in the middle of hexagons
            'A': (0, 1.2), 'B': (1.4, 1.2), 'C': (2.8, 1.2), \
            'D': (-0.7, 2.9), 'E': (0.7, 2.9), 'F': (2.1, 2.9), 'G': (3.5, 2.9), \
            'H': (-1.4, 4.6), 'I': (0, 4.6), 'J': (1.4, 4.6), 'K': (2.8, 4.6), 'L': (4.2, 4.6), \
            'M': (-0.7, 6.3), 'N': (0.7, 6.3), 'O': (2.1, 6.3), 'P': (3.5, 6.3), \
            'Q': (0, 8), 'R': (1.4, 8), 'S': (2.8, 8), \
            # harbors
            'A1': (-0.6, 0), 'A2': (-1.75, 2.95), 'A3': (-1.75, 6.3), 'A4': (-0.6, 9.2), 'A5': (1.95, 9.2), \
            'A6': (4, 7.55), 'A7': (5.2, 4.65), 'A8': (4, 1.65), 'A9': (1.95, 0)
        }

        # print(G.edges)
        # dictionary_neighbors = {}
        # keys = range(54)
        # for k in G:
        #     if type(k) == int:
        #         dictionary_neighbors[k] = list(G.neighbors(k))
        #
        # print(dictionary_neighbors)

        # creates two lists with x and y coordinates for each node - it will be used to build polygons in
        # hexagons_polygons dictionary below
        # these lists can probably be thrown away
        positions_list_x = []
        for x in range(1, 55):
            positions_list_x.append(pos[x][0])
        positions_list_y = []
        for x in range(1, 55):
            positions_list_y.append(pos[x][1])

        # builds hexagons based on x,y coordinates of nodes
        hexagons_polygons = {
            1: {"1": positions_list_x[0:6],
                "2": positions_list_y[0:6]},
            2: {"1": [0.7, 0.7, 1.4, 2.1, 2.1, 1.4],
                "2": [0.7, 1.7, 2.4, 1.7, 0.7, 0]},
            3: {"1": [2.1, 2.1, 2.8, 3.5, 3.5, 2.8],
                "2": [0.7, 1.7, 2.4, 1.7, 0.7, 0]},
            4: {"1": [-0.7, -1.4, -1.4, -0.7, 0, 0],
                "2": [1.7, 2.4, 3.4, 4.1, 3.4, 2.4]},
            5: {"1": [0.7, 0, 0, 0.7, 1.4, 1.4],
                "2": [1.7, 2.4, 3.4, 4.1, 3.4, 2.4]},
            6: {"1": [2.1, 1.4, 1.4, 2.1, 2.8, 2.8],
                "2": [1.7, 2.4, 3.4, 4.1, 3.4, 2.4]},
            7: {"1": [3.5, 2.8, 2.8, 3.5, 4.2, 4.2],
                "2": [1.7, 2.4, 3.4, 4.1, 3.4, 2.4]},
            8: {"1": [-1.4, -2.1, -2.1, -1.4, -0.7, -0.7],
                "2": [3.4, 4.1, 5.1, 5.8, 5.1, 4.1]},
            9: {"1": [0, -0.7, -0.7, 0, 0.7, 0.7],
                "2": [3.4, 4.1, 5.1, 5.8, 5.1, 4.1]},
            10: {"1": [1.4, 0.7, 0.7, 1.4, 2.1, 2.1],
                 "2": [3.4, 4.1, 5.1, 5.8, 5.1, 4.1]},
            11: {"1": [2.8, 2.1, 2.1, 2.8, 3.5, 3.5],
                 "2": [3.4, 4.1, 5.1, 5.8, 5.1, 4.1]},
            12: {"1": [4.2, 3.5, 3.5, 4.2, 4.9, 4.9],
                 "2": [3.4, 4.1, 5.1, 5.8, 5.1, 4.1]},
            13: {"1": [-0.7, -1.4, -1.4, -0.7, 0, 0],
                 "2": [5.1, 5.8, 6.8, 7.5, 6.8, 5.8]},
            14: {"1": [0.7, 0, 0, 0.7, 1.4, 1.4],
                 "2": [5.1, 5.8, 6.8, 7.5, 6.8, 5.8]},
            15: {"1": [2.1, 1.4, 1.4, 2.1, 2.8, 2.8],
                 "2": [5.1, 5.8, 6.8, 7.5, 6.8, 5.8]},
            16: {"1": [3.5, 2.8, 2.8, 3.5, 4.2, 4.2],
                 "2": [5.1, 5.8, 6.8, 7.5, 6.8, 5.8]},
            17: {"1": [0, -0.7, -0.7, 0, 0.7, 0.7],
                 "2": [6.8, 7.5, 8.5, 9.2, 8.5, 7.5]},
            18: {"1": [1.4, 0.7, 0.7, 1.4, 2.1, 2.1],
                 "2": [6.8, 7.5, 8.5, 9.2, 8.5, 7.5]},
            19: {"1": [2.8, 2.1, 2.1, 2.8, 3.5, 3.5],
                 "2": [6.8, 7.5, 8.5, 9.2, 8.5, 7.5]}

        }

        # fills the polygons with color based on updated_nodes.dict_hex_colors dictionary
        for x in hexagons_polygons:
            plt.fill("1", "2", updated_nodes.dict_hex_colors[x], alpha=0.7, edgecolor=None, lw=2, ls='solid', zorder=0,
                     data=hexagons_polygons[x])

        # fills up the hexagons with colors according to the resources assigned to them based on 'updated_dict-resources'
        # x = np.arange(-0.75, 1.75, 1)
        # y = np.arange(1, 2, 1)
        # plt.fill_between(x, y, color='blue')

        # list to store the settings to display the right colors of the nodes depending on the situation
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

        # draws the nodes in the middle - most of them are gold, if 7 was rolled or knight card was played then
        # one of them is gray

        mids = [a for a in list(G.nodes)]
        mids = [b for b in mids if type(b) == str and len(b) == 1]
        middle_nodes = []
        for enum, h in list(enumerate(mids)):
            if updated_nodes.dict_mid_nodes_for_robber[h] == 'None' and updated_nodes.dict_hex_colors[
                enum + 1] != 'navajowhite':
                middle_nodes.append('gold')
            elif updated_nodes.dict_hex_colors[enum + 1] == 'navajowhite':
                middle_nodes.append('None')
                middle_nodes.remove('None')
                # del middle_nodes[enum]

            else:
                middle_nodes.append('gray')

        ################################################        options for displaying the graph        ##################################################

        #########################################################             normal graph        ##############################################################
        if self.__dict__['option'] == 'normal':

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
                "node_size": 00,
                # "node_color": "white",
                "edgecolors": "black",
                "linewidths": linewidths_list,
                "width": 5,
                # 'node_shape': 'p'
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

        #########################################################         draws the 'merchant' graph        ##############################################################
        if self.__dict__['option'] == 'merchant':

            # draws the nodes in the middle - most of them are gold, if 7 was rolled or knight card was played then
            # one of them is gray

            mids = [a for a in list(G.nodes)]
            mids = [b for b in mids if type(b) == str and len(b) == 1]
            middle_nodes = []
            for enum, h in list(enumerate(mids)):
                if updated_nodes.dict_mid_nodes_for_robber[h] == 'None' and updated_nodes.dict_hex_colors[
                    enum + 1] != 'navajowhite':
                    middle_nodes.append('gold')
                elif updated_nodes.dict_hex_colors[enum + 1] == 'navajowhite':
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
                "node_size": 00,
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

            # marks the available harbors yellow - change later so that it reflects the turn!!! also update for the city option!!1

            harbors_highlighted = ['white' for x in range(1, 10)]

            if updated_nodes.turn % 2 != 0:
                if updated_nodes.dict_prop[1] == 'settlement_player_1' or updated_nodes.dict_prop[1] == 'city_player_1' \
                        or updated_nodes.dict_prop[2] == 'settlement_player_1' or updated_nodes.dict_prop[
                    2] == 'city_player_1':
                    harbors_highlighted[0] = 'yellow'
                if updated_nodes.dict_prop[15] == 'settlement_player_1' or updated_nodes.dict_prop[
                    15] == 'city_player_1' \
                        or updated_nodes.dict_prop[16] == 'settlement_player_1' or updated_nodes.dict_prop[
                    16] == 'city_player_1':
                    harbors_highlighted[1] = 'yellow'
                if updated_nodes.dict_prop[28] == 'settlement_player_1' or updated_nodes.dict_prop[
                    28] == 'city_player_1' \
                        or updated_nodes.dict_prop[39] == 'settlement_player_1' or updated_nodes.dict_prop[
                    39] == 'city_player_1':
                    harbors_highlighted[2] = 'yellow'
                if updated_nodes.dict_prop[48] == 'settlement_player_1' or updated_nodes.dict_prop[
                    48] == 'city_player_1' \
                        or updated_nodes.dict_prop[49] == 'settlement_player_1' or updated_nodes.dict_prop[
                    49] == 'city_player_1':
                    harbors_highlighted[3] = 'yellow'
                if updated_nodes.dict_prop[51] == 'settlement_player_1' or updated_nodes.dict_prop[
                    51] == 'city_player_1' \
                        or updated_nodes.dict_prop[52] == 'settlement_player_1' or updated_nodes.dict_prop[
                    52] == 'city_player_1':
                    harbors_highlighted[4] = 'yellow'
                if updated_nodes.dict_prop[46] == 'settlement_player_1' or updated_nodes.dict_prop[
                    46] == 'city_player_1' \
                        or updated_nodes.dict_prop[47] == 'settlement_player_1' or updated_nodes.dict_prop[
                    47] == 'city_player_1':
                    harbors_highlighted[5] = 'yellow'
                if updated_nodes.dict_prop[37] == 'settlement_player_1' or updated_nodes.dict_prop[
                    37] == 'city_player_1' \
                        or updated_nodes.dict_prop[38] == 'settlement_player_1' or updated_nodes.dict_prop[
                    38] == 'city_player_1':
                    harbors_highlighted[6] = 'yellow'
                if updated_nodes.dict_prop[25] == 'settlement_player_1' or updated_nodes.dict_prop[
                    25] == 'city_player_1' \
                        or updated_nodes.dict_prop[12] == 'settlement_player_1' or updated_nodes.dict_prop[
                    12] == 'city_player_1':
                    harbors_highlighted[7] = 'yellow'
                if updated_nodes.dict_prop[9] == 'settlement_player_1' or updated_nodes.dict_prop[9] == 'city_player_1' \
                        or updated_nodes.dict_prop[10] == 'settlement_player_1' or updated_nodes.dict_prop[
                    10] == 'city_player_1':
                    harbors_highlighted[8] = 'yellow'
            if updated_nodes.turn % 2 == 0:
                if updated_nodes.dict_prop[1] == 'settlement_player_2' or updated_nodes.dict_prop[1] == 'city_player_2' \
                        or updated_nodes.dict_prop[2] == 'settlement_player_2' or updated_nodes.dict_prop[
                    2] == 'city_player_2':
                    harbors_highlighted[0] = 'yellow'
                if updated_nodes.dict_prop[15] == 'settlement_player_2' or updated_nodes.dict_prop[
                    15] == 'city_player_2' \
                        or updated_nodes.dict_prop[16] == 'settlement_player_2' or updated_nodes.dict_prop[
                    16] == 'city_player_2':
                    harbors_highlighted[1] = 'yellow'
                if updated_nodes.dict_prop[28] == 'settlement_player_2' or updated_nodes.dict_prop[
                    28] == 'city_player_2' \
                        or updated_nodes.dict_prop[39] == 'settlement_player_2' or updated_nodes.dict_prop[
                    39] == 'city_player_2':
                    harbors_highlighted[2] = 'yellow'
                if updated_nodes.dict_prop[48] == 'settlement_player_2' or updated_nodes.dict_prop[
                    48] == 'city_player_2' \
                        or updated_nodes.dict_prop[49] == 'settlement_player_2' or updated_nodes.dict_prop[
                    49] == 'city_player_2':
                    harbors_highlighted[3] = 'yellow'
                if updated_nodes.dict_prop[51] == 'settlement_player_2' or updated_nodes.dict_prop[
                    51] == 'city_player_2' \
                        or updated_nodes.dict_prop[52] == 'settlement_player_2' or updated_nodes.dict_prop[
                    52] == 'city_player_2':
                    harbors_highlighted[4] = 'yellow'
                if updated_nodes.dict_prop[46] == 'settlement_player_2' or updated_nodes.dict_prop[
                    46] == 'city_player_2' \
                        or updated_nodes.dict_prop[47] == 'settlement_player_2' or updated_nodes.dict_prop[
                    47] == 'city_player_2':
                    harbors_highlighted[5] = 'yellow'
                if updated_nodes.dict_prop[37] == 'settlement_player_2' or updated_nodes.dict_prop[
                    37] == 'city_player_2' \
                        or updated_nodes.dict_prop[38] == 'settlement_player_2' or updated_nodes.dict_prop[
                    38] == 'city_player_2':
                    harbors_highlighted[6] = 'yellow'
                if updated_nodes.dict_prop[25] == 'settlement_player_2' or updated_nodes.dict_prop[
                    25] == 'city_player_2' \
                        or updated_nodes.dict_prop[12] == 'settlement_player_2' or updated_nodes.dict_prop[
                    12] == 'city_player_2':
                    harbors_highlighted[7] = 'yellow'
                if updated_nodes.dict_prop[9] == 'settlement_player_2' or updated_nodes.dict_prop[9] == 'city_player_2' \
                        or updated_nodes.dict_prop[10] == 'settlement_player_2' or updated_nodes.dict_prop[
                    10] == 'city_player_2':
                    harbors_highlighted[8] = 'yellow'

                x = ['merchant']

            # 'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
            x = ['merchant']

        ###############################################################        settlement graph            ###############################################################################

        # graph drawing options for the case when a settlement is to be built
        if updated_nodes.turn % 2 != 0 or updated_nodes.turn % 2 == 0:

            if self.__dict__['option'] == 'settlement':

                edges_for_graphing = list(G.edges)

                # prints settlements ands cities on the map
                if updated_nodes.turn != 0:
                    for node in G:
                        if type(node) == int:
                            if updated_nodes.dict_prop[node] == 'settlement_player_1':
                                # print(node)
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

                    edges_only_numbers = [a for a in G.edges if type(a[1]) == int]

                    # starts looking for spots available for settlements - and highlights them yellow


                    if updated_nodes.turn == 1:
                        for l in list(G.nodes):
                            for l in range(0,54):
                                color_map[l] = 'yellow'


                    elif updated_nodes.turn == 2:


                        for edge in edges_only_numbers:
                                for element in edge:
                                    if updated_nodes.dict_prop[element] != 'settlement_player_2' and \
                                            updated_nodes.dict_prop[element] != 'city_player_2' \
                                            and updated_nodes.dict_prop[element] != 'settlement_player_1' and \
                                            updated_nodes.dict_prop[element] != 'city_player_1':

                                        neighbors_to_build_settlements = list(G.neighbors(element))

                                        for s in neighbors_to_build_settlements:
                                            if type(s) != int:
                                                neighbors_to_build_settlements.remove(s)
                                        if len(neighbors_to_build_settlements) == 2:
                                            if updated_nodes.dict_prop[
                                                neighbors_to_build_settlements[0]] != 'settlement_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'settlement_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'city_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'city_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'settlement_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'settlement_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'city_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'city_player_1':
                                                color_map[element - 1] = ('yellow')

                                        elif len(neighbors_to_build_settlements) >= 3:

                                            if updated_nodes.dict_prop[
                                                neighbors_to_build_settlements[0]] != 'settlement_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'settlement_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[2]] != 'settlement_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'settlement_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'settlement_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[2]] != 'settlement_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'city_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'city_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[2]] != 'city_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'city_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'city_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[2]] != 'city_player_1':
                                                color_map[element - 1] = ('yellow')

                    elif updated_nodes.turn == 3:

                        for edge in edges_only_numbers:
                            for element in edge:
                                if updated_nodes.dict_prop[element] != 'settlement_player_1' and \
                                        updated_nodes.dict_prop[element] != 'city_player_1' \
                                        and updated_nodes.dict_prop[element] != 'settlement_player_2' and \
                                        updated_nodes.dict_prop[element] != 'city_player_2':

                                    neighbors_to_build_settlements = list(G.neighbors(element))

                                    for s in neighbors_to_build_settlements:
                                        if type(s) != int:
                                            neighbors_to_build_settlements.remove(s)
                                    if len(neighbors_to_build_settlements) == 2:
                                        if updated_nodes.dict_prop[
                                            neighbors_to_build_settlements[0]] != 'settlement_player_1' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[1]] != 'settlement_player_1' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[0]] != 'city_player_1' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[1]] != 'city_player_1' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[0]] != 'settlement_player_2' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[1]] != 'settlement_player_2' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[0]] != 'city_player_2' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[1]] != 'city_player_2':
                                            color_map[element - 1] = ('yellow')

                                    elif len(neighbors_to_build_settlements) >= 3:

                                        if updated_nodes.dict_prop[
                                            neighbors_to_build_settlements[0]] != 'settlement_player_1' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[1]] != 'settlement_player_1' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[2]] != 'settlement_player_1' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[0]] != 'settlement_player_2' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[1]] != 'settlement_player_2' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[2]] != 'settlement_player_2' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[0]] != 'city_player_1' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[1]] != 'city_player_1' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[2]] != 'city_player_1' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[0]] != 'city_player_2' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[1]] != 'city_player_2' and \
                                                updated_nodes.dict_prop[
                                                    neighbors_to_build_settlements[2]] != 'city_player_2':
                                            color_map[element - 1] = ('yellow')

                        # for l in list(G.nodes):
                        #     for l in range(0,54):
                        #         if updated_nodes.dict_prop[l+1] != 'settlement_player_1':
                        #             for m in list(G.neighbors(l+1)):
                        #                 for m in range (1,54):
                        #                     if updated_nodes.dict_prop[m] != 'settlement_player_1':
                        #                         color_map[l+1] = 'yellow'



                    elif updated_nodes.turn % 2 != 0 and updated_nodes.turn != 1 and updated_nodes != 3:

                        for edge in edges_only_numbers:
                            if updated_nodes.dict_prop_roads[edge] == 'road_player_1':

                                for element in edge:
                                    if updated_nodes.dict_prop[element] != 'settlement_player_1' and \
                                            updated_nodes.dict_prop[element] != 'city_player_1' \
                                            and updated_nodes.dict_prop[element] != 'settlement_player_2' and \
                                            updated_nodes.dict_prop[element] != 'city_player_2':

                                        neighbors_to_build_settlements = list(G.neighbors(element))

                                        for s in neighbors_to_build_settlements:
                                            if type(s) != int:
                                                neighbors_to_build_settlements.remove(s)
                                        if len(neighbors_to_build_settlements) == 2:
                                            if updated_nodes.dict_prop[
                                                neighbors_to_build_settlements[0]] != 'settlement_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'settlement_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'city_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'city_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'settlement_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'settlement_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'city_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'city_player_2':
                                                color_map[element - 1] = ('yellow')

                                        elif len(neighbors_to_build_settlements) >= 3:

                                            if updated_nodes.dict_prop[
                                                neighbors_to_build_settlements[0]] != 'settlement_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'settlement_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[2]] != 'settlement_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'settlement_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'settlement_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[2]] != 'settlement_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'city_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'city_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[2]] != 'city_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'city_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'city_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[2]] != 'city_player_2':
                                                color_map[element - 1] = ('yellow')




                    elif updated_nodes.turn % 2 == 0 and updated_nodes.turn != 2:

                        for edge in edges_only_numbers:
                            if updated_nodes.dict_prop_roads[edge] == 'road_player_2':

                                for element in edge:
                                    if updated_nodes.dict_prop[element] != 'settlement_player_2' and \
                                            updated_nodes.dict_prop[element] != 'city_player_2' \
                                            and updated_nodes.dict_prop[element] != 'settlement_player_1' and \
                                            updated_nodes.dict_prop[element] != 'city_player_1':

                                        neighbors_to_build_settlements = list(G.neighbors(element))

                                        for s in neighbors_to_build_settlements:
                                            if type(s) != int:
                                                neighbors_to_build_settlements.remove(s)
                                        if len(neighbors_to_build_settlements) == 2:
                                            if updated_nodes.dict_prop[
                                                neighbors_to_build_settlements[0]] != 'settlement_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'settlement_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'city_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'city_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'settlement_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'settlement_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'city_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'city_player_1':
                                                color_map[element - 1] = ('yellow')

                                        elif len(neighbors_to_build_settlements) >= 3:

                                            if updated_nodes.dict_prop[
                                                neighbors_to_build_settlements[0]] != 'settlement_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'settlement_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[2]] != 'settlement_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'settlement_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'settlement_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[2]] != 'settlement_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'city_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'city_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[2]] != 'city_player_2' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[0]] != 'city_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[1]] != 'city_player_1' and \
                                                    updated_nodes.dict_prop[
                                                        neighbors_to_build_settlements[2]] != 'city_player_1':
                                                color_map[element - 1] = ('yellow')

                # adjust the border width of the node that is available to build settlement on
                for index, color in list(enumerate(color_map)):
                    if color_map[index] == 'yellow':
                        linewidths_list[index] = 2

                options = {
                    "font_size": 0,
                    "node_size": 1900,
                    # "node_color": "blue",
                    "edgecolors": "black",
                    "linewidths": linewidths_list,
                    "width": 5,
                }

                # draws the roads
                edge_color_map = []
                for edge in updated_nodes.dict_prop_roads:
                    if updated_nodes.dict_prop_roads[edge] == 'road_player_1':
                        edge_color_map.append('blue')
                    elif updated_nodes.dict_prop_roads[edge] == 'road_player_2':
                        edge_color_map.append('violet')
                    else:
                        edge_color_map.append('black')

                # 'x' is a parameter needed for the for the 'cancel selection' fun)ction outside of this class to work
                x = ['settlement']




            #################################################################3              confirm settlement              ##################################################################

            elif self.__dict__['option'] == 'confirm_settlement':
                color_map = color_map_red

                # adjust the border width of the node that was chosen to build settlement on
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

                # 'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
                x = ['confirm_settlement']

                if 'red' not in color_map:
                    player1_trade["state"] = "disabled"
                    player1_use_dev_card["state"] = "disabled"
                    player1_build["state"] = "disabled"
                    player1_end_turn["state"] = "disabled"
                    player1_roll_dice["state"] = "disabled"
                    player1_cancel['state'] = 'normal'
                    player1_confirm['state'] = 'disabled'
                else:
                    player1_trade["state"] = "disabled"
                    player1_use_dev_card["state"] = "disabled"
                    player1_build["state"] = "disabled"
                    player1_end_turn["state"] = "disabled"
                    player1_roll_dice["state"] = "disabled"
                    player1_cancel['state'] = 'normal'
                    player1_confirm['state'] = 'normal'



            ###############################################################################                 city graph              #########################################################################

            # graph drawing options for the case when a city is to be built
            elif self.__dict__['option'] == 'city':
                if updated_nodes.turn % 2 != 0:  # situation for player number 1

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

                elif updated_nodes.turn % 2 == 0:  # situation for player number 2

                    # specifying different colors for the nodes that have letters assigned to them
                    for node in G:
                        if type(node) == int:
                            if updated_nodes.dict_prop[node] == 'settlement_player_2':
                                # print(node)
                                color_map.append('yellow')
                                # print(list(G.neighbors(node)))
                            elif updated_nodes.dict_prop[node] == 'settlement_player_1':
                                color_map.append('blue')
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


            #############################################################################             confirm city graph          #####################################################

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


            ###########################################################################             road graph          #################################################################################

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
                edges_only_numbers = [a for a in G.edges if type(a[1]) == int]

                edges_list_no_middle = [(1, 2), (1, 6), (2, 3), (3, 4), (3, 15), (4, 5), (4, 18), (5, 6), (5, 7), \
                                        (6, 10), (7, 8), (7, 20), (8, 9), (8, 11), (9, 10), (9, 14), (11, 12), (11, 22), \
                                        (12, 13), (12, 25), (13, 14), (15, 16), (16, 17), (16, 26), (17, 18), (17, 29), \
                                        (18, 19), (19, 20), (19, 31), (20, 21), (21, 22), (21, 33), (22, 23), (23, 24), \
                                        (23, 35), (24, 25), (24, 38), (26, 27), (27, 28), (28, 29), (28, 39), (29, 30), \
                                        (30, 31), (30, 41), (31, 32), (32, 33), (32, 43), (33, 34), (34, 35), (34, 45), \
                                        (35, 36), (36, 37), (36, 47), (37, 38), (39, 40), (40, 41), (40, 48), (41, 42), \
                                        (42, 43), (42, 50), (43, 44), (44, 45), (44, 52), (45, 46), (46, 47), (46, 54), \
                                        (48, 49), (49, 50), (50, 51), (51, 52), (52, 53), (53, 54)]

                for c in edges_list_no_middle:
                    # print(x[1])
                    if updated_nodes.turn % 2 != 0 and updated_nodes.turn !=3:
                        if updated_nodes.dict_prop_roads[c] == 'road_player_1':
                            edge_color_map.append('blue')

                        elif updated_nodes.dict_prop_roads[c] == 'road_player_2':
                            edge_color_map.append('violet')

                        elif updated_nodes.dict_prop[c[0]] == 'settlement_player_1' or updated_nodes.dict_prop[
                            c[1]] == 'settlement_player_1' \
                                or updated_nodes.dict_prop[c[0]] == 'city_player_1' or updated_nodes.dict_prop[
                            c[1]] == 'city_player_1':
                            edge_color_map.append('yellow')
                        else:
                            edge_color_map.append('black')



                    elif updated_nodes.turn == 3:
                        print('roads turn 3')
                        print(second_settlement_player_1)
                        if updated_nodes.dict_prop_roads[c] == 'road_player_1':
                            edge_color_map.append('blue')

                        elif updated_nodes.dict_prop_roads[c] == 'road_player_2':
                            edge_color_map.append('violet')

                        elif updated_nodes.dict_prop[c[0]] == 'settlement_player_1' or updated_nodes.dict_prop[
                            c[1]] == 'settlement_player_1' \
                                or updated_nodes.dict_prop[c[0]] == 'city_player_1' or updated_nodes.dict_prop[
                            c[1]] == 'city_player_1':
                            edge_color_map.append('black')
                        else:
                            edge_color_map.append('black')


                            #
                        if len(second_settlement_player_1) > 0:
                            available_roads_player_1 = ((list(G.edges(second_settlement_player_1))))
                            print(available_roads_player_1)
                            available_roads_player_1 = [list(b) for b in available_roads_player_1]

                            print(available_roads_player_1)
                            print('trakaka')
                            available_roads_player_1 = [c for c in available_roads_player_1 if
                                                        type(c[0]) == int and type(c[1]) == int]

                            print(available_roads_player_1)
                            for d in available_roads_player_1:
                                d.sort()
                            available_roads_player_1 = [tuple(e) for e in available_roads_player_1]
                            print(available_roads_player_1)

                            print('now her we are')


                        print('last step')
                        print(available_roads_player_1)
                        print(list(enumerate(edge_color_map)))
                        print(list(enumerate(edges_list_no_middle)))

                        if len(available_roads_player_1) == 3:
                            indices_2 = [i for i, x in enumerate(edges_list_no_middle) if x == available_roads_player_1[0] or x == available_roads_player_1[1] or x == available_roads_player_1[2]]
                        elif len(available_roads_player_1) == 2:
                            indices_2 = [i for i, x in enumerate(edges_list_no_middle) if
                                         x == available_roads_player_1[0] or x == available_roads_player_1[1]]
                        elif len(available_roads_player_1) == 1:
                            indices_2 = [i for i, x in enumerate(edges_list_no_middle) if
                                         x == available_roads_player_1[0]]

                        print(indices_2)

                        if len((list(enumerate(edge_color_map)))) == 71:
                            for e in indices_2:
                                edge_color_map[e] = 'yellow'


                        # for t, y in list(enumerate(edges_list_no_middle)):
                        #     if y == available_roads_player_1[0] or y == available_roads_player_1[1] or y == available_roads_player_1[2]:
                        #         edge_color_map[t] = 'yellow'

                            # for t in edge_color_map:
                            #     if t == 'yellow':
                            #         print(edge_color_map.index(t))
                        #
                        # indices = [i for i, x in enumerate(edge_color_map) if x == "yellow"]
                        # print(indices)
                        # print(list(enumerate(edge_color_map)))
                        # print(list(enumerate(edges_list_no_middle)))
                        #
                        # # for y in indices:
                        # #     if edges_list_no_middle[y] not in available_roads_player_1:
                        # #         edge_color_map[y] = 'black'
                        #
                        # for number, piece in list(enumerate(edge_color_map)):
                        #     if piece in edge_color_map == 'yellow':
                        #         if edges_list_no_middle[number] not in available_roads_player_1:
                        #             edge_color_map[number] = 'black'
                        #
                        #











                    elif updated_nodes.turn % 2 == 0 and updated_nodes.turn != 2:
                        if updated_nodes.dict_prop_roads[c] == 'road_player_1':
                            edge_color_map.append('blue')

                        elif updated_nodes.dict_prop_roads[c] == 'road_player_2':
                            edge_color_map.append('violet')

                        elif updated_nodes.dict_prop[c[0]] == 'settlement_player_2' or updated_nodes.dict_prop[
                            c[1]] == 'settlement_player_2' \
                                or updated_nodes.dict_prop[c[0]] == 'city_player_2' or updated_nodes.dict_prop[
                            c[1]] == 'city_player_2':
                            edge_color_map.append('yellow')
                        else:
                            edge_color_map.append('black')


                    # both starting settlements (for each player) have to have one road adjacent to them
                    elif updated_nodes.turn == 2:


                        if updated_nodes.dict_prop_roads[c] == 'road_player_1':
                            edge_color_map.append('blue')

                        elif updated_nodes.dict_prop_roads[c] == 'road_player_2':
                            edge_color_map.append('violet')


                        elif (updated_nodes.dict_prop[c[0]] == 'settlement_player_2' or updated_nodes.dict_prop\
                        [c[1]] == 'settlement_player_2' or updated_nodes.dict_prop[c[0]] == 'city_player_2' or updated_nodes.dict_prop[c[1]] == 'city_player_2'):
                            edge_color_map.append('yellow')

                        else:
                            edge_color_map.append('black')

                        # else:
                        #     edge_color_map.append('black')



                        settlements_player_2 = 0

                        for i in updated_nodes.dict_prop:
                            if updated_nodes.dict_prop[i] == 'settlement_player_2':
                                settlements_player_2 += 1

                        if settlements_player_2 != 2:
                            available_roads_player_2 = edges_list_no_middle

                        elif settlements_player_2 == 2:
                            print(second_settlement_player_2)
                            available_roads_player_2 = ((list(G.edges(second_settlement_player_2))))
                            print(available_roads_player_2)
                            available_roads_player_2 = [list(b) for b in available_roads_player_2]

                            print(available_roads_player_2)
                            print('trakaka')
                            available_roads_player_2 = [c for c in available_roads_player_2 if type(c[0]) == int and type(c[1]) == int]

                            print(available_roads_player_2)
                            for d in available_roads_player_2:
                                d.sort()
                            available_roads_player_2 = [tuple(e) for e in available_roads_player_2]
                            print(available_roads_player_2)
                            print(settlements_player_2)

                        print(list(enumerate(edge_color_map)))
                        print(list(enumerate(edges_list_no_middle)))


                        if settlements_player_2 == 2:
                            print(edge_color_map)
                            print('now her we are')
                            # for t in edge_color_map:
                            #     if t == 'yellow':
                            #         print(edge_color_map.index(t))

                            indices = [i for i, x in enumerate(edge_color_map) if x == "yellow"]
                            print(indices)

                            for y in indices:
                                if edges_list_no_middle[y] not in available_roads_player_2:
                                    edge_color_map[y] = 'black'


                            # for h in g:
                            #     if type(h) == str and h == 'yellow':
                            #         h = 'black'
                                # if h[1] == 'yellow':
                                #     h = 'orange'


                    #
                    #     if updated_nodes.dict_prop_roads[c] == 'road_player_1':
                    #         edge_color_map.append('blue')
                    #
                    #     elif updated_nodes.dict_prop_roads[c] == 'road_player_2':
                    #         edge_color_map.append('violet')
                    #
                    #
                    #     elif updated_nodes.dict_prop[c[0]] == 'settlement_player_2' or updated_nodes.dict_prop[
                    #         c[1]] == 'settlement_player_2' \
                    #             or updated_nodes.dict_prop[c[0]] == 'city_player_2' or updated_nodes.dict_prop[
                    #         c[1]] == 'city_player_2':
                    #         if c in available_roads_player_2:
                    #             edge_color_map.append('yellow')
                    #
                    #     else:
                    #         edge_color_map.append('black')





                # creates yellow edges for the ends of edges where roads are already built
                edges_list = [a for a in edges_list if type(a[1]) == int]

                for r in edges_list:
                    # print(x[1])
                    if updated_nodes.turn % 2 != 0 and updated_nodes.turn != 3:
                        if updated_nodes.dict_prop_roads[r] == 'road_player_1':
                            list_enumerate = edges_list
                            enumerate_prime = enumerate(list_enumerate)
                            list_enumerate_prime = list(enumerate_prime)

                            available_roads_init = list(G.edges([r[1]]))

                            for j in G.edges([r[0]]):
                                available_roads_init.append(j)
                            available_roads_init_2 = [a for a in available_roads_init if type(a[1]) == int]
                            available_roads_init_sorted = []

                            list_enumerate_prime_3 = []
                            for b in list_enumerate_prime:
                                if type(b[1][1]) == int:
                                    list_enumerate_prime_3.append(b)

                            for u in available_roads_init_2:
                                new_u = sorted(u)
                                available_roads_init_sorted.append(new_u)
                            available_roads_init = []
                            for i in available_roads_init_sorted:
                                available_roads_init.append(tuple(i))
                                # print(available_roads_init)
                                # print(updated_nodes.dict_prop_roads.keys())
                            for d in available_roads_init:
                                if updated_nodes.dict_prop_roads[d] != 'road_player_1' and \
                                        updated_nodes.dict_prop_roads[d] != 'road_player_2':
                                    for item in list_enumerate_prime_3:
                                        if d == item[1]:
                                            # print(item[0])
                                            # print(d)
                                            edge_color_map[item[0]] = 'yellow'

                    elif updated_nodes.turn % 2 == 0 and updated_nodes.turn != 2:
                        if updated_nodes.dict_prop_roads[r] == 'road_player_2':
                            list_enumerate = edges_list
                            enumerate_prime = enumerate(list_enumerate)
                            list_enumerate_prime = list(enumerate_prime)

                            available_roads_init = list(G.edges([r[1]]))

                            for j in G.edges([r[0]]):
                                available_roads_init.append(j)
                            available_roads_init_2 = [a for a in available_roads_init if type(a[1]) == int]
                            available_roads_init_sorted = []

                            list_enumerate_prime_3 = []
                            for b in list_enumerate_prime:
                                if type(b[1][1]) == int:
                                    list_enumerate_prime_3.append(b)

                            for u in available_roads_init_2:
                                new_u = sorted(u)
                                available_roads_init_sorted.append(new_u)
                            available_roads_init = []
                            for i in available_roads_init_sorted:
                                available_roads_init.append(tuple(i))
                                # print(available_roads_init)
                                # print(updated_nodes.dict_prop_roads.keys())
                            for d in available_roads_init:
                                if updated_nodes.dict_prop_roads[d] != 'road_player_1' and \
                                        updated_nodes.dict_prop_roads[d] != 'road_player_2':
                                    for item in list_enumerate_prime_3:
                                        if d == item[1]:
                                            # print(item[0])
                                            # print(d)
                                            edge_color_map[item[0]] = 'yellow'

                # 'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
                x = ['road']

                player1_build_road.place_forget()
                player1_build_settlement.place_forget()
                player1_build_city.place_forget()
                player1_buy_dev_card.place_forget()




            ###########################################################################             'confirm road graph'            #########################################################################

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
                # 'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
                x = ['confirm_road']

                if 'red' not in edge_color_map:
                    player1_trade["state"] = "disabled"
                    player1_use_dev_card["state"] = "disabled"
                    player1_build["state"] = "disabled"
                    player1_end_turn["state"] = "disabled"
                    player1_roll_dice["state"] = "disabled"
                    player1_cancel['state'] = 'normal'
                    player1_confirm['state'] = 'disabled'
                else:
                    player1_trade["state"] = "disabled"
                    player1_use_dev_card["state"] = "disabled"
                    player1_build["state"] = "disabled"
                    player1_end_turn["state"] = "disabled"
                    player1_roll_dice["state"] = "disabled"
                    player1_cancel['state'] = 'normal'
                    player1_confirm['state'] = 'normal'

            #########################             'confirm road graph_2'  - needed in order not to take resources for the road from using the 'road building' card##########################################################

            elif self.__dict__['option'] == 'confirm_road_2':
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
                # 'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
                x = ['confirm_road_2']

                if 'red' not in edge_color_map:
                    player1_trade["state"] = "disabled"
                    player1_use_dev_card["state"] = "disabled"
                    player1_build["state"] = "disabled"
                    player1_end_turn["state"] = "disabled"
                    player1_roll_dice["state"] = "disabled"
                    player1_cancel['state'] = 'normal'
                    player1_confirm['state'] = 'disabled'
                else:
                    player1_trade["state"] = "disabled"
                    player1_use_dev_card["state"] = "disabled"
                    player1_build["state"] = "disabled"
                    player1_end_turn["state"] = "disabled"
                    player1_roll_dice["state"] = "disabled"
                    player1_cancel['state'] = 'normal'
                    player1_confirm['state'] = 'normal'



            #########################################################             'confirm road graph' - after playing the development card 'road building'    #########################################################################

            elif self.__dict__['option'] == 'confirm_road_dev_card':
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

                # 'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
                x = ['confirm_road_dev_card']

                if 'red' not in edge_color_map:
                    player1_trade["state"] = "disabled"
                    player1_use_dev_card["state"] = "disabled"
                    player1_build["state"] = "disabled"
                    player1_end_turn["state"] = "disabled"
                    player1_roll_dice["state"] = "disabled"
                    player1_cancel['state'] = 'normal'
                    player1_confirm['state'] = 'disabled'
                else:
                    player1_trade["state"] = "disabled"
                    player1_use_dev_card["state"] = "disabled"
                    player1_build["state"] = "disabled"
                    player1_end_turn["state"] = "disabled"
                    player1_roll_dice["state"] = "disabled"
                    player1_cancel['state'] = 'normal'
                    player1_confirm['state'] = 'normal'

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

                # finds nodes attached to the opponent and makes them available to be blocked (assigns black color to them)
                for enum, node in list(enumerate(G, start=-54)):
                    index = 0
                    if type(node) == str and len(node) == 1:
                        print(enum, node)
                        # print(list(G.neighbors(node)))
                        for c in list(G.neighbors(node)):

                            if updated_nodes.turn % 2 != 0:

                                if (updated_nodes.dict_prop[c] == 'settlement_player_2' or updated_nodes.dict_prop[
                                    c] == 'city_player_2') \
                                        and updated_nodes.dict_mid_nodes_for_robber[node] != 'robber':
                                    middle_node_colors_knight_card[enum] = 'gray'
                            else:

                                if (updated_nodes.dict_prop[c] == 'settlement_player_1' or updated_nodes.dict_prop[
                                    c] == 'city_player_1') \
                                        and updated_nodes.dict_mid_nodes_for_robber[node] != 'robber':
                                    middle_node_colors_knight_card[enum] = 'gray'

                # removes the color from the node containing the desert
                for enum, node in list(enumerate(G, start=-53)):
                    index = 0
                    if type(node) == str and len(node) == 1:
                        # print(enum, node)
                        if updated_nodes.dict_hex_colors[enum] == 'navajowhite':
                            # print('here')
                            middle_node_colors_knight_card[enum - 1] = 'None'
                            # del middle_node_colors_knight_card[enum-1]

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
                x = ['knight_card']

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

                # removes the color from the node containing the desert
                for enum, node in list(enumerate(G, start=-53)):
                    index = 0
                    if type(node) == str and len(node) == 1:
                        print(enum, node)
                        if updated_nodes.dict_hex_colors[enum] == 'navajowhite':
                            print(updated_nodes.dict_hex_colors[enum])
                            middle_node_colors_knight_card_red[enum - 1] = 'None'

                # finds nodes attached to the opponent and makes them available to be blocked (assigns black color to them)
                for enum, node in list(enumerate(G, start=-54)):
                    index = 0
                    if type(node) == str and len(node) == 1:
                        # print(enum, node)
                        # print(list(G.neighbors(node)))
                        for c in list(G.neighbors(node)):
                            if (updated_nodes.dict_prop[c] == 'settlement_player_2' or updated_nodes.dict_prop[
                                c] == 'city_player_2') \
                                    and middle_node_colors_knight_card_red[enum] != 'red' and \
                                    middle_node_colors_knight_card_red[enum] != 'None':
                                # print(enum, node)
                                middle_node_colors_knight_card_red[enum] = 'gold'

                print(middle_node_colors_knight_card_red)

                options = {
                    "font_size": 0,
                    "node_size": 1900,
                    # "node_color": "white",
                    "edgecolors": "black",
                    "linewidths": linewidths_list,
                    "width": 5,
                    # 'node_shape': 'o'
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

        # creates labels for the nodes that have letters assigned to them, gives them a random integer value
        keys_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']

        # creates a dictionary for the harbor nodes - will be used to draw these selected nodes separately with labels
        keys_labels_harbors = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
        values_labels_harbors = ['3:1', 'Wheat\n2:1', 'Rock\n2:1', '3:1', 'Sheep\n2:1', '3:1', '3:1', 'Brick\n2:1',
                                 ' Lumber\n2:1']

        harbors = dict(zip(keys_labels_harbors, values_labels_harbors))

        # list updated every time a new settlement is created - will be used to display nodes having settlements on them
        keys_settlements_cities = [x for x in updated_nodes.dict_prop if
                                   updated_nodes.dict_prop[x] == 'settlement_player_1' \
                                   or updated_nodes.dict_prop[x] == 'city_player_1' \
                                   or updated_nodes.dict_prop[x] == 'settlement_player_2' \
                                   or updated_nodes.dict_prop[x] == 'city_player_2']

        colors_settlements_cities = []
        for elem in keys_settlements_cities:
            if updated_nodes.dict_prop[elem] == 'settlement_player_1':
                colors_settlements_cities.append('blue')
            elif updated_nodes.dict_prop[elem] == 'settlement_player_2':
                colors_settlements_cities.append('violet')

        dict_labels = dict(zip(keys_labels, values_labels))

        # assigns the 'desert' (or really an empty value) value to the desert hexagon,\
        # if 'desert' taken away from other hex -> swaps values
        desert_update = list(dict_labels)
        for e in updated_nodes.dict_hex_colors:
            if updated_nodes.dict_hex_colors[e] == 'navajowhite':
                if dict_labels[desert_update[e - 1]] != ' ':
                    swap = dict_labels[desert_update[e - 1]]
                    dict_labels[desert_update[e - 1]] = ' '
                    for y in dict_labels:
                        if dict_labels[y] == ' ' and y != desert_update[e - 1]:
                            dict_labels[y] = swap

        # cancels drawing of the 'desert' node
        for e in dict_labels:
            if dict_labels[e] == ' ':
                y = desert_update.index(e)
                keys_labels.remove(keys_labels[y])

        # draws only the edges connecting nodes on the vertices of the hexagons withour drawing the ones in the middle of hexes
        edges_no_middle_nodes = [v for v in list(G.edges) if isinstance(v[0], int) and isinstance(v[1], int)]

        # edges_no_middle_nodes = []
        # for v in list(G.edges):
        #     if isinstance(v[0], int) and isinstance(v[1], int):
        #         edges_no_middle_nodes.append(v)

        # lists only the edges in the middle of hexes
        edges_only_middle_nodes = [v for v in list(G.edges) if isinstance(v[0], str) or isinstance(v[1], str)]
        # print(edges_only_middle_nodes)

        ###################################################           drawing of the graph         #########################################################################3

        edgelist = edges_no_middle_nodes

        # plots the nodes and edges on the graph
        nx.draw_networkx(G, pos, edge_color=edge_color_map, edgelist=edgelist, node_color=color_map, **options, ax=a)

        # plots different shaped nodes, depending if a city or a settlement is built on the node
        node_list_settlements = []
        node_list_cities = []
        for s in updated_nodes.dict_prop:
            if updated_nodes.dict_prop[s] == 'settlement_player_1' or updated_nodes.dict_prop[
                s] == 'settlement_player_2':
                node_list_settlements.append(s)

        for s in updated_nodes.dict_prop:
            if updated_nodes.dict_prop[s] == 'city_player_1' or updated_nodes.dict_prop[s] == 'city_player_2':
                node_list_cities.append(s)

        node_color_settlements = []
        node_color_cities = []

        for s in node_list_settlements:
            node_color_settlements.append(color_map[s - 1])

        for s in node_list_cities:
            node_color_cities.append(color_map[s - 1])

        nx.draw_networkx_nodes(G, pos, edgecolors='black', linewidths=2, nodelist=node_list_settlements,
                               node_color=node_color_settlements, node_shape='o', node_size=2000)
        nx.draw_networkx_nodes(G, pos, edgecolors='black', linewidths=2, nodelist=node_list_cities,
                               node_color=node_color_cities, node_shape='p', node_size=3500)

        # draws the labels for the nodes that have letters assigned to them - shows the numerical value assigned to them randomly
        nx.draw_networkx_labels(G, pos, labels=dict_labels, font_size=16)
        # displays the golden nodes in the middle of hexes
        if self.__dict__['option'] != 'knight_card' and self.__dict__['option'] != 'confirm_knight_card':
            nx.draw_networkx_nodes(G, pos, nodelist=keys_labels, node_size=2000, node_color=middle_nodes,
                                   edgecolors='black')
        elif self.__dict__['option'] == 'knight_card':
            middle_node_colors_knight_card.remove('None')
            nx.draw_networkx_nodes(G, pos, nodelist=keys_labels, node_size=2000,
                                   node_color=middle_node_colors_knight_card, edgecolors='black')
        elif self.__dict__['option'] == 'confirm_knight_card':
            middle_node_colors_knight_card_red.remove(middle_node_colors_knight_card_red[y])
            nx.draw_networkx_nodes(G, pos, nodelist=keys_labels, node_size=2000,
                                   node_color=middle_node_colors_knight_card_red, edgecolors='black')
        # draws white harbors
        if self.__dict__['option'] != 'merchant':
            nx.draw_networkx_nodes(G, pos, nodelist=keys_labels_harbors, node_size=2000, node_shape='h',
                                   node_color='white', edgecolors='black')
        # highlights harbors that are available to trade with ('trade with merchant') button
        else:
            nx.draw_networkx_nodes(G, pos, nodelist=keys_labels_harbors, node_size=2100, node_shape='h',
                                   node_color=harbors_highlighted, edgecolors='black')
        # draws the labels for the harbor nodes
        nx.draw_networkx_labels(G, pos, labels=harbors, font_size=10)

        # displays nodes that have settlements or cities on them
        # nx.draw_networkx_nodes(G, pos, nodelist=keys_settlements_cities, node_size=2000, node_color=colors_settlements_cities, edgecolors='black')

        # Set margins for the axes so that nodes aren't clipped
        # ax = plt.gca()
        # ax.margins(0.20)
        # plt.axis("off")

        # create matplotlib canvas using figure f / graph `G`  and assign to widget `board frame`
        self.canvas = FigureCanvasTkAgg(f, master=board_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column=1, row=0)

        # self.canvas.get_tk_widget().place(relx=0.2, rely=0)

        ###########################################################       this section defines actions that happen when graph is clicked
        #                                                           (upon clicking merchant, knight card or building buttons)          #####################################################

        # function to get the coordinates when clicked on the graph
        def on_click(event):
            global color_map_red_old
            global color_map_red
            global middle_node_knight_card_red
            if event.button is MouseButton.LEFT and self.__dict__['option'] == 'settlement':
                global key_settlement
                x, y = event.x, event.y
                ax = event.inaxes  # the axes instance;
                # print('Coordinates: %f %f' % (event.xdata, event.ydata))
                # add a function here later that clears the list 'coordinates' if it is not empty
                coordinates.append(event.xdata)
                coordinates.append(event.ydata)
                # print(coordinates)
                # print(color_map)

                plt.close(f)

                self.clearPlotPage()
                # prints the list of nodes - I can use it later to select the node to be colored red - should it be highlighted here?

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
                # print(list(enumerate(positions)))
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
                # print(coordinates_tuple)
                # print(updated_nodes.dict_prop)
                # creates a list needed to update the values for 'settlement' or 'city' within the 'Graph_Properties' class
                # later will create function that will turn the confirm button off if clicked in the spot that was not allowed
                key_settlement = [w for w in pos if pos[w] == coordinates_tuple]

                # create a list to contain information about which node was clicked
                color_map_red = []

                # assigns the value 'red' in the color_map (which is used to color the nodes in the graph)
                # and leaves other values as they were
                try:
                    for i in pos:
                        if pos[i] == coordinates_tuple and color_map[i - 1] == 'yellow' and coordinates[0] != None \
                                and updated_nodes.dict_prop[i] != 'settlement_player_2' and updated_nodes.dict_prop[
                            i] != 'city_player_2':
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
                    plt.close(f)

                    settlement_graph.create_graph()

                # print(color_map_red)

                # color_map_red = ['red' if pos[i] == coordinates_tuple and updated_nodes.dict_prop[i] == 'settlement_player_1'\
                #                      else 'white' if type(i) == int else 'yellow' for i in pos]

                # check which settlements and cities were already built by both players and adjust the 'color_map_red' accordingly
                for node in G:
                    if type(node) == int:
                        if updated_nodes.dict_prop[node] == 'settlement_player_1':
                            color_map_red[node - 1] = ('blue')
                        elif updated_nodes.dict_prop[node] == 'settlement_player_2':
                            color_map_red[node - 1] = ('violet')
                        elif updated_nodes.dict_prop[node] == 'city_player_1':
                            color_map_red[node - 1] = ('blue')
                        elif updated_nodes.dict_prop[node] == 'city_player_2':
                            color_map_red[node - 1] = ('violet')

                # create a list'color map red old' to compare it with the newly created color map red list - if they are not the same,
                # the player hasn't clicked the red node and the program will not allow it
                # will be used later for the case when the player builds a city
                color_map_red_old = color_map_red

                if 'red' in color_map_red:
                    plt.close(f)

                    confirm_settlement_graph.create_graph()
                else:
                    plt.close(f)

                    settlement_graph.create_graph()

            ###############################################################         defines clicking the settlement that will be upgraded to a city     ##############################################

            elif event.button is MouseButton.LEFT and self.__dict__['option'] == 'city':
                global key_city
                x, y = event.x, event.y
                ax = event.inaxes  # the axes instance; is this expression necessary?
                # print('Coordinates: %f %f' % (event.xdata, event.ydata))
                # add a function here later that clears the list 'coordinates' if it is not empty
                coordinates.append(event.xdata)
                coordinates.append(event.ydata)
                plt.close(f)

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
                # find the nodes (in the dictionary 'pos') that are closest to the elements that were just clicked
                if coordinates[0] != None and coordinates[1] != None:
                    a = (min(positions_first_element, key=lambda x: abs(x - coordinates[0])))
                    b = (min(positions_second_element, key=lambda x: abs(x - coordinates[1])))
                else:
                    a = 0  # later write a function to disable the confirm button if clicked at the wrong spot
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
                        if pos[i] == coordinates_tuple and color_map[i - 1] == 'yellow' and coordinates[0] != None:
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

                # print(color_map_red)
                # print(len(color_map_red))
                # print(len(pos))

                # color_map_red = ['red' if pos[i] == coordinates_tuple else 'white' if type(i) == int else 'yellow' for i in pos]

                # check which settlements and cities were already built by both players and adjust the 'color_map_red' accordingly

                if updated_nodes.turn % 2 != 0:
                    for node in G:
                        if type(node) == int:
                            if updated_nodes.dict_prop[node] == 'settlement_player_1' and color_map_red[
                                node - 1] != 'red':
                                color_map_red[node - 1] = ('blue')
                            elif updated_nodes.dict_prop[node] == 'settlement_player_2':
                                color_map_red[node - 1] = ('violet')
                            elif updated_nodes.dict_prop[node] == 'city_player_1':
                                color_map_red[node - 1] = ('blue')
                            elif updated_nodes.dict_prop[node] == 'city_player_2':
                                color_map_red[node - 1] = ('violet')
                elif updated_nodes.turn % 2 == 0:
                    for node in G:
                        if type(node) == int:
                            if updated_nodes.dict_prop[node] == 'settlement_player_1':
                                color_map_red[node - 1] = ('blue')
                            elif updated_nodes.dict_prop[node] == 'settlement_player_2' and color_map_red[
                                node - 1] != 'red':
                                color_map_red[node - 1] = ('violet')
                            elif updated_nodes.dict_prop[node] == 'city_player_1':
                                color_map_red[node - 1] = ('blue')
                            elif updated_nodes.dict_prop[node] == 'city_player_2':
                                color_map_red[node - 1] = ('violet')

                # print(color_map_red)
                # if color_map_red_old[positions_index] == 'red':
                if 'red' in color_map_red:
                    plt.close(f)
                    confirm_city_graph.create_graph()
                    player1_cancel['state'] = 'normal'
                    player1_confirm['state'] = 'normal'
                else:
                    color_map_red = []
                    plt.close(f)
                    city_graph.create_graph()

            ############################################################################        defines the edge that will be updated to a road         ############################################

            elif event.button is MouseButton.LEFT and self.__dict__['option'] == 'road':
                global edge_color_map_road
                global key_edges
                x, y = event.x, event.y
                ax = event.inaxes
                # print('Coordinates: %f %f' % (event.xdata, event.ydata))
                # add a function here later that clears the list 'coordinates' if it is not empty
                coordinates.append(event.xdata)
                coordinates.append(event.ydata)

                plt.close(f)

                self.clearPlotPage()
                # for each edge it takes the respective values in the dictionary 'pos' and makes an average out of them.
                # will be used later to click the edges that a player wants to build a road on
                edges = edges_list_no_middle

                list_pos = [[pos[y] for y in x] for x in edges]

                list_pos_first_element = [[y[0] for y in x] for x in list_pos]
                list_pos_second_element = [[y[1] for y in x] for x in list_pos]

                avg_first_element = [sum(x) / len(x) for x in list_pos_first_element]
                avg_second_element = [sum(x) / len(x) for x in list_pos_second_element]
                if coordinates[0] != None and coordinates[1] != None:
                    a = (min(avg_first_element, key=lambda x: abs(x - coordinates[0])))
                    b = (min(avg_second_element, key=lambda x: abs(x - coordinates[1])))
                else:
                    a = 999  # later write a function to disable the confirm button if clicked at the wrong spot
                    b = 999

                coordinates_tuple = (a, b)
                print(coordinates_tuple)

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
                list_pos_first_element_matching = ['True' if sum(x) / len(x) == coordinates_tuple[0] else 'False' for x
                                                   in list_pos_first_element]
                list_pos_second_element_matching = ['True' if sum(x) / len(x) == coordinates_tuple[1] else 'False' for x
                                                    in list_pos_second_element]

                final_list = []
                for x, y in zip(list_pos_first_element_matching, list_pos_second_element_matching):
                    if x == 'True':
                        if y == 'True':
                            final_list.append('True')
                        else:
                            final_list.append('False')
                    else:
                        final_list.append('False')

                print(list_pos_first_element_matching)
                print(list_pos_second_element_matching)
                print(final_list)

                index_edges = []

                for index, item in enumerate(final_list):
                    if item == 'True':
                        index_edges.append(index)

                print(index_edges)
                if len(index_edges) > 0:
                    key_edges = edges[
                        index_edges[0]]  # defines a variable used later to update dictionary with 'road' property
                    # print(key_edges)

                edge_color_map_road = []

                if len(index_edges) == 0:
                    coord_edges = ['None']
                elif len(index_edges) > 0:
                    coord_edges = edges[index_edges[0]]

                edge_color_map_enumerated = list(enumerate(edge_color_map))

                print(coord_edges)

                # final step to compare the list with all edges to the edge clicked. when the edge is found it is marked red
                for x in edges_list_no_middle:
                    if x == coord_edges:
                        for a, b in list(enumerate(edges)):
                            if b == coord_edges and edge_color_map[a] == 'yellow':
                                # print(a)
                                edge_color_map_road.append('red')
                            elif b == coord_edges and edge_color_map[a] == 'violet':
                                edge_color_map_road.append('violet')
                            elif b == coord_edges and edge_color_map[a] != 'yellow':
                                edge_color_map_road.append('black')
                    elif b == coord_edges and edge_color_map[a] == 'road_player_2':
                        edge_color_map.append('violet')
                    elif updated_nodes.dict_prop_roads[x] == 'road_player_1':
                        edge_color_map_road.append('blue')
                    elif updated_nodes.dict_prop_roads[x] == 'road_player_2':
                        edge_color_map_road.append('violet')
                    else:
                        edge_color_map_road.append('black')

                if coord_edges == ['None'] or 'red' not in edge_color_map_road:
                    # edge_color_map_road = edge_color_map
                    plt.close(f)
                    road_graph.create_graph()
                else:
                    # next graph is printed depending if the player is building a regular road or playing the 'road building' development card
                    if counter_road_building_dev_card % 2 != 0 and counter_road_building_dev_card != 1:
                        plt.close(f)

                        confirm_road_graph_2.create_graph()

                    elif counter_road_building_dev_card % 2 != 0 and counter_road_building_dev_card == 1:

                        plt.close(f)

                        confirm_road_graph.create_graph()
                    else:
                        plt.close(f)

                        confirm_road_graph_dev_card.create_graph()

                # nx.draw_networkx(G, pos, node_color=color_map_red, **options, ax=a)
                #
                # self.canvas = FigureCanvasTkAgg(f, master=board_frame)
                # self.canvas.draw()
                # self.canvas.get_tk_widget().pack()


            #######################################  draws the graph with red node highlighted, to be blocked by a knight card      ###################################################

            elif event.button is MouseButton.LEFT and self.__dict__['option'] == 'knight_card':
                global key_knight_card
                x, y = event.x, event.y
                ax = event.inaxes  # the axes instance;
                # print('Coordinates: %f %f' % (event.xdata, event.ydata))
                # add a function here later that clears the list 'coordinates' if it is not empty
                coordinates.append(event.xdata)
                coordinates.append(event.ydata)
                print(coordinates)
                plt.close(f)

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
                            round(h, 1)
                    else:
                        round(h, 1)

                # creates a list needed to update the values for 'settlement' or 'city' within the 'Graph_Properties' class
                # later will create function that will turn the confirm button off if clicked in the spot that was not allowed
                key_knight_card = [w for w in pos if pos[w] == coordinates_tuple]
                print(key_knight_card)
                # create a list to contain information about which node was clicked
                color_map_red = []

                edges_only_middle_nodes_letter_only = list(set([l for g, l in edges_only_middle_nodes]))
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
                        print(updated_nodes.dict_hex_colors[(u[0]) + 1])
                        if updated_nodes.dict_hex_colors[(u[0]) + 1] == 'navajowhite':
                            middle_node_knight_card_red.append('None')
                        elif updated_nodes.dict_hex_colors[(u[0]) + 1] != 'navajowhite' and key_knight_card == (
                        list(u[1])) and middle_node_colors_knight_card[int(u[0])] == 'gray':
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

                    if 'red' not in middle_node_knight_card_red:
                        plt.close(f)
                        start_graph.create_graph()
                        player1_trade["state"] = "normal"
                        player1_use_dev_card["state"] = "normal"
                        player1_build["state"] = "normal"
                        player1_end_turn["state"] = "normal"
                        player1_roll_dice["state"] = "disabled"
                        player1_cancel['state'] = 'disabled'
                        player1_confirm['state'] = 'disabled'
                    else:
                        plt.close(f)
                        confirm_knight_card_graph.create_graph()

                except IndexError or TypeError or ValueError or AttributeError:
                    plt.close(f)
                    start_graph.create_graph()

            #######################################  draws the graph with pop up windows after clicking the 'trade with merchant' button      ###################################################

            elif event.button is MouseButton.LEFT and self.__dict__['option'] == 'merchant':
                x, y = event.x, event.y
                ax = event.inaxes  # the axes instance;
                # print('Coordinates: %f %f' % (event.xdata, event.ydata))
                # add a function here later that clears the list 'coordinates' if it is not empty
                coordinates.append(event.xdata)
                coordinates.append(event.ydata)
                print(coordinates)
                # self.clearPlotPage()

                print(list(G.nodes)[-9:])

                coordinates_tuple = tuple(coordinates)
                # print(coordinates_tuple)
                # finding the dictionary 'pos' values that are closest to the coordinates clicked by the player
                positions = []
                for key in pos:
                    if type(key) == str and len(key) == 2:
                        positions.append(pos[key])

                print(positions)

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
                            print('ja')
                            round(h, 1)

                    else:
                        round(h, 1)

                # creates a list needed to update the values for 'settlement' or 'city' within the 'Graph_Properties' class
                # later will create function that will turn the confirm button off if clicked in the spot that was not allowed
                key_merchant = [w for w in pos if pos[w] == coordinates_tuple]
                if len(key_merchant) == 0:
                    plt.close(f)

                    merchant_graph.clearPlotPage()
                    merchant_graph.create_graph()

                print(key_merchant)

                # what happens after the 'confirm' button is clicked

                def confirm_merchant():
                    def button_config():
                        merchant_window.destroy()
                        player1_roll_dice['state'] = 'disable'
                        player1_trade['state'] = 'normal'
                        player1_use_dev_card['state'] = 'normal'
                        player1_build['state'] = 'normal'
                        player1_end_turn['state'] = 'normal'
                        player1_confirm['state'] = 'disable'
                        player1_cancel['state'] = 'disable'
                        merchant_graph.clearPlotPage()
                        start_graph.create_graph()

                    # what happens when the harbor '3:1' is clicked
                    if key_merchant[0] == 'A1' or key_merchant[0] == 'A4' or key_merchant[0] == 'A6' or \
                            key_merchant[0] == 'A7':

                        if updated_nodes.turn % 2 != 0:

                            if v.get() == 'Brick' and Player_1.brick >= 3:
                                if z.get() == 'Brick':
                                    Player_1.brick -= 2
                                    brick.set(Player_1.brick)
                                elif z.get() == 'Lumber':
                                    Player_1.lumber += 1
                                    Player_1.brick -= 3
                                    brick.set(Player_1.brick)
                                    lumber.set(Player_1.lumber)
                                elif z.get() == 'Sheep':
                                    Player_1.sheep += 1
                                    Player_1.brick -= 3
                                    brick.set(Player_1.brick)
                                    sheep.set(Player_1.sheep)
                                elif z.get() == 'Wheat':
                                    Player_1.hay += 1
                                    Player_1.brick -= 3
                                    brick.set(Player_1.brick)
                                    hay.set(Player_1.hay)
                                elif z.get() == 'Rock':
                                    Player_1.rock += 1
                                    Player_1.brick -= 3
                                    brick.set(Player_1.brick)
                                    rock.set(Player_1.rock)

                                button_config()

                            elif v.get() == 'Lumber' and Player_1.lumber >= 3:
                                if z.get() == 'Lumber':
                                    Player_1.lumber -= 3
                                    lumber.set(Player_1.lumber)
                                elif z.get() == 'Brick':
                                    Player_1.lumber -= 3
                                    Player_1.brick += 1
                                    brick.set(Player_1.brick)
                                    lumber.set(Player_1.lumber)
                                elif z.get() == 'Sheep':
                                    Player_1.sheep += 1
                                    Player_1.lumber -= 3
                                    lumber.set(Player_1.lumber)
                                    sheep.set(Player_1.sheep)
                                elif z.get() == 'Wheat':
                                    Player_1.hay += 1
                                    Player_1.lumber -= 3
                                    lumber.set(Player_1.lumber)
                                    hay.set(Player_1.hay)
                                elif z.get() == 'Rock':
                                    Player_1.rock += 1
                                    Player_1.lumber -= 3
                                    rock.set(Player_1.rock)
                                    lumber.set(Player_1.lumber)

                                button_config()

                            elif v.get() == 'Sheep' and Player_1.sheep >= 3:
                                if z.get() == 'Sheep':
                                    Player_1.sheep -= 3
                                    sheep.set(Player_1.sheep)
                                elif z.get() == 'Brick':
                                    Player_1.sheep -= 3
                                    Player_1.brick += 1
                                    sheep.set(Player_1.sheep)
                                    brick.set(Player_1.brick)
                                elif z.get() == 'Lumber':
                                    Player_1.sheep -= 3
                                    Player_1.lumber += 1
                                    sheep.set(Player_1.sheep)
                                    lumber.set(Player_1.lumber)
                                elif z.get() == 'Wheat':
                                    Player_1.sheep -= 3
                                    Player_1.hay += 1
                                    sheep.set(Player_1.sheep)
                                    hay.set(Player_1.hay)
                                elif z.get() == 'Rock':
                                    Player_1.sheep -= 3
                                    Player_1.rock += 1
                                    sheep.set(Player_1.sheep)
                                    rock.set(Player_1.rock)

                                button_config()


                            elif v.get() == 'Wheat' and Player_1.hay >= 3:
                                if z.get() == 'Wheat':
                                    Player_1.hay -= 3
                                    hay.set(Player_1.hay)
                                elif z.get() == 'Brick':
                                    Player_1.hay -= 3
                                    Player_1.brick += 1
                                    hay.set(Player_1.hay)
                                    brick.set(Player_1.brick)
                                elif z.get() == 'Lumber':
                                    Player_1.hay -= 3
                                    Player_1.lumber += 1
                                    hay.set(Player_1.hay)
                                    lumber.set(Player_1.lumber)
                                elif z.get() == 'Sheep':
                                    Player_1.hay -= 3
                                    Player_1.sheep += 1
                                    sheep.set(Player_1.sheep)
                                    hay.set(Player_1.hay)
                                elif z.get() == 'Rock':
                                    Player_1.hay -= 3
                                    Player_1.rock += 1
                                    hay.set(Player_1.hay)
                                    rock.set(Player_1.rock)

                                button_config()

                            elif v.get() == 'Rock' and Player_1.rock >= 3:
                                if z.get() == 'Rock':
                                    Player_1.rock -= 3
                                    rock.set(Player_1.rock)
                                elif z.get() == 'Brick':
                                    Player_1.rock -= 3
                                    Player_1.brick += 1
                                    rock.set(Player_1.rock)
                                    brick.set(Player_1.brick)
                                elif z.get() == 'Lumber':
                                    Player_1.rock -= 3
                                    Player_1.lumber += 1
                                    rock.set(Player_1.rock)
                                    lumber.set(Player_1.lumber)
                                elif z.get() == 'Sheep':
                                    Player_1.rock -= 3
                                    Player_1.sheep += 1
                                    sheep.set(Player_1.sheep)
                                    rock.set(Player_1.rock)
                                elif z.get() == 'Wheat':
                                    Player_1.rock -= 3
                                    Player_1.hay += 1
                                    hay.set(Player_1.hay)
                                    rock.set(Player_1.rock)

                                button_config()




                            else:
                                merchant_window.attributes('-topmost', 0)
                                messagebox.showinfo("", "At least 3 cards of this kind required!")
                                merchant_window.attributes('-topmost', 1)

                        elif updated_nodes.turn % 2 == 0:

                            if v.get() == 'Brick' and Player_2.brick >= 3:
                                if z.get() == 'Brick':
                                    Player_2.brick -= 2
                                    brick2.set(Player_2.brick)
                                elif z.get() == 'Lumber':
                                    Player_2.lumber += 1
                                    Player_2.brick -= 3
                                    brick2.set(Player_2.brick)
                                    lumber2.set(Player_2.lumber)
                                elif z.get() == 'Sheep':
                                    Player_2.sheep += 1
                                    Player_2.brick -= 3
                                    brick2.set(Player_2.brick)
                                    sheep2.set(Player_2.sheep)
                                elif z.get() == 'Wheat':
                                    Player_2.hay += 1
                                    Player_2.brick -= 3
                                    brick2.set(Player_2.brick)
                                    hay2.set(Player_2.hay)
                                elif z.get() == 'Rock':
                                    Player_2.rock += 1
                                    Player_2.brick -= 3
                                    brick2.set(Player_2.brick)
                                    rock2.set(Player_2.rock)

                                button_config()

                            elif v.get() == 'Lumber' and Player_2.lumber >= 3:
                                if z.get() == 'Lumber':
                                    Player_2.lumber -= 3
                                    lumber2.set(Player_2.lumber)
                                elif z.get() == 'Brick':
                                    Player_2.lumber -= 3
                                    Player_2.brick += 1
                                    brick2.set(Player_2.brick)
                                    lumber2.set(Player_2.lumber)
                                elif z.get() == 'Sheep':
                                    Player_2.sheep += 1
                                    Player_2.lumber -= 3
                                    lumber2.set(Player_2.lumber)
                                    sheep2.set(Player_2.sheep)
                                elif z.get() == 'Wheat':
                                    Player_2.hay += 1
                                    Player_2.lumber -= 3
                                    lumber2.set(Player_2.lumber)
                                    hay2.set(Player_2.hay)
                                elif z.get() == 'Rock':
                                    Player_2.rock += 1
                                    Player_2.lumber -= 3
                                    rock2.set(Player_2.rock)
                                    lumber2.set(Player_2.lumber)

                                button_config()

                            elif v.get() == 'Sheep' and Player_2.sheep >= 3:
                                if z.get() == 'Sheep':
                                    Player_2.sheep -= 3
                                    sheep2.set(Player_2.sheep)
                                elif z.get() == 'Brick':
                                    Player_2.sheep -= 3
                                    Player_2.brick += 1
                                    sheep2.set(Player_2.sheep)
                                    brick2.set(Player_2.brick)
                                elif z.get() == 'Lumber':
                                    Player_2.sheep -= 3
                                    Player_2.lumber += 1
                                    sheep2.set(Player_2.sheep)
                                    lumber2.set(Player_2.lumber)
                                elif z.get() == 'Wheat':
                                    Player_2.sheep -= 3
                                    Player_2.hay += 1
                                    sheep2.set(Player_2.sheep)
                                    hay2.set(Player_2.hay)
                                elif z.get() == 'Rock':
                                    Player_2.sheep -= 3
                                    Player_2.rock += 1
                                    sheep2.set(Player_2.sheep)
                                    rock2.set(Player_2.rock)

                                button_config()


                            elif v.get() == 'Wheat' and Player_2.hay >= 3:
                                if z.get() == 'Wheat':
                                    Player_2.hay -= 3
                                    hay2.set(Player_2.hay)
                                elif z.get() == 'Brick':
                                    Player_2.hay -= 3
                                    Player_2.brick += 1
                                    hay2.set(Player_2.hay)
                                    brick2.set(Player_2.brick)
                                elif z.get() == 'Lumber':
                                    Player_2.hay -= 3
                                    Player_2.lumber += 1
                                    hay2.set(Player_2.hay)
                                    lumber2.set(Player_2.lumber)
                                elif z.get() == 'Sheep':
                                    Player_2.hay -= 3
                                    Player_2.sheep += 1
                                    sheep2.set(Player_2.sheep)
                                    hay2.set(Player_2.hay)
                                elif z.get() == 'Rock':
                                    Player_2.hay -= 3
                                    Player_2.rock += 1
                                    hay2.set(Player_2.hay)
                                    rock2.set(Player_2.rock)

                                button_config()

                            elif v.get() == 'Rock' and Player_2.rock >= 3:
                                if z.get() == 'Rock':
                                    Player_2.rock -= 3
                                    rock2.set(Player_2.rock)
                                elif z.get() == 'Brick':
                                    Player_2.rock -= 3
                                    Player_2.brick += 1
                                    rock2.set(Player_2.rock)
                                    brick2.set(Player_2.brick)
                                elif z.get() == 'Lumber':
                                    Player_2.rock -= 3
                                    Player_2.lumber += 1
                                    rock2.set(Player_2.rock)
                                    lumber2.set(Player_2.lumber)
                                elif z.get() == 'Sheep':
                                    Player_2.rock -= 3
                                    Player_2.sheep += 1
                                    sheep2.set(Player_2.sheep)
                                    rock2.set(Player_2.rock)
                                elif z.get() == 'Wheat':
                                    Player_2.rock -= 3
                                    Player_2.hay += 1
                                    hay2.set(Player_2.hay)
                                    rock2.set(Player_2.rock)

                                button_config()




                            else:
                                merchant_window.attributes('-topmost', 0)
                                messagebox.showinfo("", "At least 3 cards of this kind required!")
                                merchant_window.attributes('-topmost', 1)



                    # what happens when the harbor '2:1' is clicked
                    elif key_merchant[0] == 'A2':

                        if updated_nodes.turn % 2 != 0:

                            if v.get() == 'Brick' and Player_1.hay >= 2:
                                Player_1.brick += 1
                                Player_1.hay -= 2
                                brick.set(Player_1.brick)
                                hay.set(Player_1.hay)
                                button_config()
                            elif v.get() == 'Lumber' and Player_1.hay >= 2:
                                Player_1.lumber += 1
                                Player_1.hay -= 2
                                lumber.set(Player_1.lumber)
                                hay.set(Player_1.hay)
                                button_config()
                            elif v.get() == 'Sheep' and Player_1.hay >= 2:
                                Player_1.brick += 1
                                Player_1.hay -= 2
                                sheep.set(Player_1.sheep)
                                hay.set(Player_1.hay)
                                button_config()
                            elif v.get() == 'Wheat' and Player_1.hay >= 2:
                                Player_1.hay += 1
                                Player_1.hay -= 2
                                hay.set(Player_1.hay)
                                button_config()
                            elif v.get() == 'Rock' and Player_1.hay >= 2:
                                Player_1.rock += 1
                                Player_1.hay -= 2
                                rock.set(Player_1.rock)
                                hay.set(Player_1.hay)
                                button_config()

                            else:
                                merchant_window.attributes('-topmost', 0)
                                messagebox.showinfo("", "At least 2 cards of this kind required!")
                                merchant_window.attributes('-topmost', 1)

                        if updated_nodes.turn % 2 == 0:

                            if v.get() == 'Brick' and Player_2.hay >= 2:
                                Player_2.brick += 1
                                Player_2.hay -= 2
                                brick2.set(Player_2.brick)
                                hay2.set(Player_2.hay)
                                button_config()
                            elif v.get() == 'Lumber' and Player_2.hay >= 2:
                                Player_2.lumber += 1
                                Player_2.hay -= 2
                                lumber2.set(Player_2.lumber)
                                hay2.set(Player_2.hay)
                                button_config()
                            elif v.get() == 'Sheep' and Player_2.hay >= 2:
                                Player_2.brick += 1
                                Player_2.hay -= 2
                                sheep2.set(Player_2.sheep)
                                hay2.set(Player_2.hay)
                                button_config()
                            elif v.get() == 'Wheat' and Player_2.hay >= 2:
                                Player_2.hay += 1
                                Player_2.hay -= 2
                                hay2.set(Player_2.hay)
                                button_config()
                            elif v.get() == 'Rock' and Player_2.hay >= 2:
                                Player_2.rock += 1
                                Player_2.hay -= 2
                                rock2.set(Player_2.rock)
                                hay2.set(Player_2.hay)
                                button_config()

                            else:
                                merchant_window.attributes('-topmost', 0)
                                messagebox.showinfo("", "At least 2 cards of this kind required!")
                                merchant_window.attributes('-topmost', 1)






                    elif key_merchant[0] == 'A3':

                        if updated_nodes.turn % 2 != 0:

                            if v.get() == 'Brick' and Player_1.rock >= 2:
                                Player_1.brick += 1
                                Player_1.rock -= 2
                                brick.set(Player_1.brick)
                                rock.set(Player_1.rock)
                                button_config()
                            elif v.get() == 'Lumber' and Player_1.rock >= 2:
                                Player_1.lumber += 1
                                Player_1.rock -= 2
                                lumber.set(Player_1.lumber)
                                rock.set(Player_1.rock)
                                button_config()
                            elif v.get() == 'Sheep' and Player_1.rock >= 2:
                                Player_1.sheep += 1
                                Player_1.rock -= 2
                                sheep.set(Player_1.sheep)
                                rock.set(Player_1.rock)
                                button_config()
                            elif v.get() == 'Rock' and Player_1.rock >= 2:
                                Player_1.rock += 1
                                Player_1.rock -= 2
                                rock.set(Player_1.rock)
                                button_config()
                            elif v.get() == 'Wheat' and Player_1.rock >= 2:
                                Player_1.hay += 1
                                Player_1.rock -= 2
                                rock.set(Player_1.rock)
                                hay.set(Player_1.hay)
                                button_config()

                            else:
                                merchant_window.attributes('-topmost', 0)
                                messagebox.showinfo("", "At least 2 cards of this kind required!")
                                merchant_window.attributes('-topmost', 1)

                        if updated_nodes.turn % 2 == 0:
                            if v.get() == 'Brick' and Player_2.rock >= 2:
                                Player_2.brick += 1
                                Player_2.rock -= 2
                                brick2.set(Player_2.brick)
                                rock2.set(Player_2.rock)
                                button_config()
                            elif v.get() == 'Lumber' and Player_2.rock >= 2:
                                Player_2.lumber += 1
                                Player_2.rock -= 2
                                lumber2.set(Player_2.lumber)
                                rock2.set(Player_2.rock)
                                button_config()
                            elif v.get() == 'Sheep' and Player_2.rock >= 2:
                                Player_2.sheep += 1
                                Player_2.rock -= 2
                                sheep2.set(Player_2.sheep)
                                rock2.set(Player_2.rock)
                                button_config()
                            elif v.get() == 'Rock' and Player_2.rock >= 2:
                                Player_2.rock += 1
                                Player_2.rock -= 2
                                rock2.set(Player_2.rock)
                                button_config()
                            elif v.get() == 'Wheat' and Player_2.rock >= 2:
                                Player_2.hay += 1
                                Player_2.rock -= 2
                                rock2.set(Player_2.rock)
                                hay2.set(Player_2.hay)
                                button_config()

                            else:
                                merchant_window.attributes('-topmost', 0)
                                messagebox.showinfo("", "At least 2 cards of this kind required!")
                                merchant_window.attributes('-topmost', 1)

                    elif key_merchant[0] == 'A5':

                        if updated_nodes.turn % 2 != 0:

                            if v.get() == 'Brick' and Player_1.sheep >= 2:
                                Player_1.brick += 1
                                Player_1.sheep -= 2
                                brick.set(Player_1.brick)
                                sheep.set(Player_1.sheep)
                                button_config()
                            elif v.get() == 'Lumber' and Player_1.sheep >= 2:
                                Player_1.lumber += 1
                                Player_1.sheep -= 2
                                lumber.set(Player_1.lumber)
                                sheep.set(Player_1.sheep)
                                button_config()
                            elif v.get() == 'Sheep' and Player_1.sheep >= 2:
                                Player_1.sheep += 1
                                Player_1.sheep -= 2
                                sheep.set(Player_1.sheep)
                                button_config()
                            elif v.get() == 'Wheat' and Player_1.sheep >= 2:
                                Player_1.hay += 1
                                Player_1.sheep -= 2
                                hay.set(Player_1.hay)
                                sheep.set(Player_1.sheep)
                                button_config()
                            elif v.get() == 'Rock' and Player_1.sheep >= 2:
                                Player_1.rock += 1
                                Player_1.sheep -= 2
                                rock.set(Player_1.rock)
                                sheep.set(Player_1.sheep)
                                button_config()

                            else:
                                merchant_window.attributes('-topmost', 0)
                                messagebox.showinfo("", "At least 2 cards of this kind required!")
                                merchant_window.attributes('-topmost', 1)

                        if updated_nodes.turn % 2 == 0:

                            if v.get() == 'Brick' and Player_2.sheep >= 2:
                                Player_2.brick += 1
                                Player_2.sheep -= 2
                                brick2.set(Player_2.brick)
                                sheep2.set(Player_2.sheep)
                                button_config()
                            elif v.get() == 'Lumber' and Player_2.sheep >= 2:
                                Player_2.lumber += 1
                                Player_2.sheep -= 2
                                lumber2.set(Player_2.lumber)
                                sheep2.set(Player_2.sheep)
                                button_config()
                            elif v.get() == 'Sheep' and Player_2.sheep >= 2:
                                Player_2.sheep += 1
                                Player_2.sheep -= 2
                                sheep2.set(Player_2.sheep)
                                button_config()
                            elif v.get() == 'Wheat' and Player_2.sheep >= 2:
                                Player_2.hay += 1
                                Player_2.sheep -= 2
                                hay2.set(Player_2.hay)
                                sheep2.set(Player_2.sheep)
                                button_config()
                            elif v.get() == 'Rock' and Player_2.sheep >= 2:
                                Player_2.rock += 1
                                Player_2.sheep -= 2
                                rock2.set(Player_2.rock)
                                sheep2.set(Player_2.sheep)
                                button_config()

                            else:
                                merchant_window.attributes('-topmost', 0)
                                messagebox.showinfo("", "At least 2 cards of this kind required!")
                                merchant_window.attributes('-topmost', 1)




                    elif key_merchant[0] == 'A8':

                        if updated_nodes.turn % 2 != 0:

                            if v.get() == 'Brick' and Player_1.brick >= 2:
                                Player_1.brick += 1
                                Player_1.brick -= 2
                                brick.set(Player_1.brick)
                                button_config()
                            elif v.get() == 'Lumber' and Player_1.brick >= 2:
                                Player_1.lumber += 1
                                Player_1.brick -= 2
                                lumber.set(Player_1.lumber)
                                brick.set(Player_1.brick)
                                button_config()
                            elif v.get() == 'Sheep' and Player_1.brick >= 2:
                                Player_1.sheep += 1
                                Player_1.brick -= 2
                                sheep.set(Player_1.sheep)
                                brick.set(Player_1.brick)
                                button_config()
                            elif v.get() == 'Wheat' and Player_1.brick >= 2:
                                Player_1.hay += 1
                                Player_1.brick -= 2
                                hay.set(Player_1.hay)
                                brick.set(Player_1.brick)
                                button_config()
                            elif v.get() == 'Rock' and Player_1.brick >= 2:
                                Player_1.rock += 1
                                Player_1.sheep -= 2
                                rock.set(Player_1.rock)
                                brick.set(Player_1.brick)
                                button_config()

                            else:
                                merchant_window.attributes('-topmost', 0)
                                messagebox.showinfo("", "At least 2 cards of this kind required!")
                                merchant_window.attributes('-topmost', 1)

                        if updated_nodes.turn % 2 == 0:

                            if v.get() == 'Brick' and Player_2.brick >= 2:
                                Player_2.brick += 1
                                Player_2.brick -= 2
                                brick2.set(Player_2.brick)
                                button_config()
                            elif v.get() == 'Lumber' and Player_2.brick >= 2:
                                Player_2.lumber += 1
                                Player_2.brick -= 2
                                lumber2.set(Player_2.lumber)
                                brick2.set(Player_2.brick)
                                button_config()
                            elif v.get() == 'Sheep' and Player_2.brick >= 2:
                                Player_2.sheep += 1
                                Player_2.brick -= 2
                                sheep2.set(Player_2.sheep)
                                brick2.set(Player_2.brick)
                                button_config()
                            elif v.get() == 'Wheat' and Player_2.brick >= 2:
                                Player_2.hay += 1
                                Player_2.brick -= 2
                                hay2.set(Player_2.hay)
                                brick2.set(Player_2.brick)
                                button_config()
                            elif v.get() == 'Rock' and Player_2.brick >= 2:
                                Player_2.rock += 1
                                Player_2.brick -= 2
                                rock2.set(Player_2.rock)
                                brick2.set(Player_2.brick)
                                button_config()

                            else:
                                merchant_window.attributes('-topmost', 0)
                                messagebox.showinfo("", "At least 2 cards of this kind required!")
                                merchant_window.attributes('-topmost', 1)


                    elif key_merchant[0] == 'A9':

                        if updated_nodes.turn % 2 != 0:

                            if v.get() == 'Brick' and Player_1.lumber >= 2:
                                Player_1.brick += 1
                                Player_1.lumber -= 2
                                brick.set(Player_1.brick)
                                lumber.set(Player_1.lumber)
                                button_config()
                            elif v.get() == 'Lumber' and Player_1.lumber >= 2:
                                Player_1.lumber += 1
                                Player_1.lumber -= 2
                                lumber.set(Player_1.lumber)
                                button_config()
                            elif v.get() == 'Sheep' and Player_1.lumber >= 2:
                                Player_1.sheep += 1
                                Player_1.lumber -= 2
                                sheep.set(Player_1.sheep)
                                lumber.set(Player_1.lumber)
                                button_config()
                            elif v.get() == 'Wheat' and Player_1.lumber >= 2:
                                Player_1.hay += 1
                                Player_1.lumber -= 2
                                hay.set(Player_1.hay)
                                lumber.set(Player_1.lumber)
                                button_config()
                            elif v.get() == 'Rock' and Player_1.lumber >= 2:
                                Player_1.rock += 1
                                Player_1.lumber -= 2
                                rock.set(Player_1.rock)
                                lumber.set(Player_1.lumber)
                                button_config()

                            else:
                                merchant_window.attributes('-topmost', 0)
                                messagebox.showinfo("", "At least 2 cards of this kind required!")
                                merchant_window.attributes('-topmost', 1)

                        if updated_nodes.turn % 2 == 0:

                            if v.get() == 'Brick' and Player_2.lumber >= 2:
                                Player_2.brick += 1
                                Player_2.lumber -= 2
                                brick.set(Player_2.brick)
                                lumber.set(Player_2.lumber)
                                button_config()
                            elif v.get() == 'Lumber' and Player_2.lumber >= 2:
                                Player_2.lumber += 1
                                Player_2.lumber -= 2
                                lumber.set(Player_2.lumber)
                                button_config()
                            elif v.get() == 'Sheep' and Player_2.lumber >= 2:
                                Player_2.sheep += 1
                                Player_2.lumber -= 2
                                sheep.set(Player_2.sheep)
                                lumber.set(Player_2.lumber)
                                button_config()
                            elif v.get() == 'Wheat' and Player_2.lumber >= 2:
                                Player_2.hay += 1
                                Player_2.lumber -= 2
                                hay.set(Player_2.hay)
                                lumber.set(Player_2.lumber)
                                button_config()
                            elif v.get() == 'Rock' and Player_2.lumber >= 2:
                                Player_2.rock += 1
                                Player_2.lumber -= 2
                                rock.set(Player_2.rock)
                                lumber.set(Player_2.lumber)
                                button_config()

                            else:
                                merchant_window.attributes('-topmost', 0)
                                messagebox.showinfo("", "At least 2 cards of this kind required!")
                                merchant_window.attributes('-topmost', 1)

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
                    merchant_graph.clearPlotPage()
                    plt.close(f)

                    start_graph.create_graph()

                # what happens when 'X' on the top bar of the pop up window is clicked
                def on_exit():
                    player1_roll_dice['state'] = 'disable'
                    player1_trade['state'] = 'normal'
                    player1_use_dev_card['state'] = 'normal'
                    player1_build['state'] = 'normal'
                    player1_end_turn['state'] = 'normal'
                    player1_confirm['state'] = 'disable'
                    player1_cancel['state'] = 'disable'
                    merchant_window.destroy()

                if len(key_merchant) != 0:
                    if (key_merchant == ['A1'] and harbors_highlighted[0] == 'yellow') or \
                            (key_merchant == ['A4'] and harbors_highlighted[3] == 'yellow') or \
                            (key_merchant == ['A6'] and harbors_highlighted[5] == 'yellow') or \
                            (key_merchant == ['A7'] and harbors_highlighted[6] == 'yellow'):

                        # Toplevel object which will
                        # be treated as a new window
                        merchant_window = Toplevel(root)

                        # sets the title of the
                        # Toplevel widget
                        merchant_window.title(" ")

                        # sets the geometry of toplevel
                        merchant_window.geometry("300x250")

                        merchant_window.protocol("WM_DELETE_WINDOW", on_exit)

                        # puts the new window in the center
                        width = root.winfo_x()
                        height = root.winfo_y()
                        merchant_window.geometry("+%d+%d" % (width + 700, height + 400))

                        # Make topLevelWindow remain on top until destroyed, or attribute changes.
                        merchant_window.attributes('-topmost', 'true')

                        # A Label widget to show in toplevel - this 'dummy' label is made to put two other columns in the middle on the window
                        Label(merchant_window, text="     ", font=("Times New Roman", 12), padx=10, pady=10).grid(row=0,
                                                                                                                  column=0,
                                                                                                                  columnspan=1)

                        # A Label widget to show in toplevel
                        Label(merchant_window, text="Your 3 cards:", font=("Times New Roman", 12), padx=10,
                              pady=10).grid(
                            row=0, column=2, columnspan=1)

                        # A Label widget to show in toplevel
                        Label(merchant_window, text="For 1 card:", font=("Times New Roman", 12), padx=30, pady=10).grid(
                            row=0, column=4, columnspan=1)

                        #########################            ####################

                        # Tkinter string variable
                        # able to store any string value
                        v = StringVar(merchant_window, "1")

                        # Tkinter string variable
                        # able to store any string value
                        z = StringVar(merchant_window, "1")

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
                            Radiobutton(merchant_window, width=10, text=text, variable=v,
                                        value=value, indicator=0,
                                        background="lightskyblue").grid(row=y, column=2, columnspan=2)
                            y += 1

                        b = 1

                        # Loop is used to create multiple Radiobuttons
                        # rather than creating each button separately
                        for (text_2, value_2) in values_2.items():
                            Radiobutton(merchant_window, width=10, text=text_2, variable=z,
                                        value=value_2, indicator=0,
                                        background="lightskyblue").grid(row=b, column=4, columnspan=2)
                            b += 1

                        # 'cancel' button inside this window
                        cancel_merchant = Button(merchant_window, width=3, height=1, bg='white', text=chr(10008),
                                                 fg='red', \
                                                 font=('Times New Roman', 20), \
                                                 command=close_window).grid(row=6, column=2, columnspan=1, padx=10,
                                                                            pady=20)

                        # 'confirm' button inside this window
                        confirm_merchant = Button(merchant_window, width=3, height=1, bg='white', text=chr(10003),
                                                  fg='green', \
                                                  font=('Times New Roman', 20), \
                                                  command=confirm_merchant).grid(row=6, column=4, columnspan=2,
                                                                                 padx=10, pady=20)



                    elif (key_merchant == ['A2'] and harbors_highlighted[1] == 'yellow') or \
                            (key_merchant == ['A3'] and harbors_highlighted[2] == 'yellow') or \
                            (key_merchant == ['A5'] and harbors_highlighted[4] == 'yellow') or \
                            (key_merchant == ['A8'] and harbors_highlighted[7] == 'yellow') or \
                            (key_merchant == ['A9'] and harbors_highlighted[8] == 'yellow'):

                        # Toplevel object which will
                        # be treated as a new window
                        merchant_window = Toplevel(root)

                        merchant_window.protocol("WM_DELETE_WINDOW", on_exit)

                        # sets the title of the
                        # Toplevel widget
                        merchant_window.title(" ")

                        # sets the geometry of toplevel
                        merchant_window.geometry("210x250")

                        # puts the new window in the center
                        width = root.winfo_x()
                        height = root.winfo_y()
                        merchant_window.geometry("+%d+%d" % (width + 700, height + 400))

                        # Make topLevelWindow remain on top until destroyed, or attribute changes.
                        merchant_window.attributes('-topmost', 'true')

                        # # A Label widget to show in toplevel - this 'dummy' label is made to put two other columns in the middle on the window
                        # Label(merchant_window, text="     ", font=("Times New Roman", 12), padx=10, pady=10).grid(row=0,
                        #                                                                                           column=0,
                        #                                                                                           columnspan=1)

                        # A Label widget to show in toplevel
                        Label(merchant_window, text="Trade for one of the following:", font=("Times New Roman", 12),
                              padx=10, pady=10).grid(
                            row=0, column=0, columnspan=2)
                        #
                        # # A Label widget to show in toplevel
                        # Label(merchant_window, text="For 1 card:", font=("Times New Roman", 12), padx=30, pady=10).grid(
                        #     row=0, column=4, columnspan=1)
                        #

                        #########################            ####################

                        # Tkinter string variable
                        # able to store any string value
                        v = StringVar(merchant_window, "1")

                        # Tkinter string variable
                        # able to store any string value
                        # z = StringVar(merchant_window, "1")

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
                            Radiobutton(merchant_window, width=10, text=text, variable=v,
                                        value=value, indicator=0,
                                        background="lightskyblue").grid(row=y, column=0, columnspan=2)
                            y += 1

                        # 'cancel' button inside this window
                        cancel_merchant = Button(merchant_window, width=3, height=1, bg='white', text=chr(10008),
                                                 fg='red', \
                                                 font=('Times New Roman', 20), \
                                                 command=close_window).grid(row=6, column=0, columnspan=1, padx=10,
                                                                            pady=20)

                        # 'confirm' button inside this window
                        confirm_merchant = Button(merchant_window, width=3, height=1, bg='white', text=chr(10003),

                                                  fg='green', \
                                                  font=('Times New Roman', 20), \
                                                  command=confirm_merchant).grid(row=6, column=1, columnspan=1,
                                                                                 padx=10, pady=20)

                    else:
                        plt.close(f)
                        merchant_graph.clearPlotPage()
                        merchant_graph.create_graph()

                        player1_trade["state"] = "disabled"
                        player1_use_dev_card["state"] = "disabled"
                        player1_build["state"] = "disabled"
                        player1_end_turn["state"] = "disabled"
                        player1_roll_dice["state"] = "disabled"
                        player1_cancel['state'] = 'normal'
                        player1_confirm['state'] = 'disabled'
                # try:
                #
                # except IndexError or TypeError or ValueError or AttributeError:
                #     start_graph.create_graph()
                #

        # connect 'button press event' with on_click function, can later be disconnected with:
        # plt.disconnect(cid)
        cid = plt.connect('button_press_event', on_click)

    # clear the canvas to prepare for the next version of the graph
    def clearPlotPage(self):
        plt.close(f)

        self.canvas.get_tk_widget().pack_forget()

    # cancels
    # the action and goes back to the normal view
    # def cancel_selection(self):
    #
    #     plt.close(f)
    #     self.clearPlotPage()
    #     start_graph.create_graph()
    #


# initializes a dictionary that stores information about the nodes (if it's settlement / city)
class Graph_Properties:
    five_roads_player_1 = None
    six_roads_player_1 = None
    seven_roads_player_1 = None
    eight_roads_player_1 = None
    nine_roads_player_1 = None
    ten_roads_player_1 = None
    eleven_roads_player_1 = None
    twelve_roads_player_1 = None

    five_roads_player_2 = None
    six_roads_player_2 = None
    seven_roads_player_2 = None
    eight_roads_player_2 = None
    nine_roads_player_2 = None
    ten_roads_player_2 = None
    eleven_roads_player_2 = None
    twelve_roads_player_2 = None


    def __init__(self, turn):
        self.turn = turn
        # resources_list = ['wood', 'rock', 'wheat']
        # random.shuffle(resources_list)
        # hexagons_resources = ['A', 'B', 'C']
        # list to be used to create a dictionary with 'settlement' or 'city' or 'None' value for each node
        properties = [y for y in range(1, 60)]
        # should later make a list at the beginning with all the edges that are needed to create a graph in the 'Graph' class and in the dict below
        # list with edges to create a dictionary for roads

        roads = [(1, 2), (1, 6), (2, 3), (3, 4), (3, 15), (4, 5), (4, 18), (5, 6), (5, 7), (6, 10), (7, 8), (7, 20),
                 (8, 9), (8, 11), \
                 (9, 10), (9, 14), (11, 12), (11, 22), (12, 13), (12, 25), (13, 14), (15, 16), (16, 17), (16, 26),
                 (17, 18), (17, 29), \
                 (18, 19), (19, 20), (19, 31), (20, 21), (21, 22), (21, 33), (22, 23), (23, 24), (23, 35), (24, 25),
                 (24, 38), (26, 27), \
                 (27, 28), (28, 29), (28, 39), (29, 30), (30, 31), (30, 41), (31, 32), (32, 33), (32, 43), (33, 34),
                 (34, 35), (34, 45), \
                 (35, 36), (36, 37), (36, 47), (37, 38), (39, 40), (40, 41), (40, 48), (41, 42), (42, 43), (42, 50),
                 (43, 44), (44, 45), \
                 (44, 52), (45, 46), (46, 47), (46, 54), (48, 49), (49, 50), (50, 51), (51, 52), (52, 53), (53, 54)]





        mid_nodes_keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
        mid_nodes_values = ['None' for x in range(19)]
        self.dict_mid_nodes_for_robber = dict(zip(mid_nodes_keys, mid_nodes_values))

        self.dict_prop = dict.fromkeys(properties)
        self.dict_prop_roads = dict.fromkeys(roads)
        # self.dict_resources = dict(zip(hexagons_resources, resources_list))

        # creates bogus conditions after first rounds of settling so i can modify the graphs - remove later
        # self.dict_prop[1] = 'settlement_player_1'
        # self.dict_prop[12] = 'settlement_player_2'
        # self.dict_prop_roads[1, 2] = 'road_player_1'
        # self.dict_prop_roads[11, 12] = 'road_player_2'

        # creates a dictionary with hexagons as keys and randomly assigned colors as values
        colors_hexagons_keys = [x for x in range(1, 20)]
        colors_hexagons_values = ['lime', 'yellow', 'yellow', 'yellow', 'yellow', 'forestgreen', 'dimgrey', 'red',
                                  'red', \
                                  'forestgreen', 'lime', 'lime', 'lime', 'forestgreen', 'forestgreen', 'dimgrey',
                                  'dimgrey', 'red', 'navajowhite']
        random.shuffle(colors_hexagons_values)
        colors_hexagons = dict(zip(colors_hexagons_keys, colors_hexagons_values))
        # print(colors_hexagons)

        # bogus dictionary with colors of the hexes (dependent on the resources associated with them)
        self.dict_hex_colors = colors_hexagons
        # print(self.dict_hex_colors)

    # prepares a dictionary to store information about the type of resource associated with a node -
    # probably move up outside of this function
    # def assign_resources_to_hexagons(self):
    #     random.shuffle(resources_list)
    #     list_for_resources_all = ['A', 'B', 'C']
    #     list_for_resources_selected = [x for x in list_for_resources_all if isinstance(x, str)]
    #     dict_resources = dict(zip(list_for_resources_selected, resources_list))
    #     print(dict_resources)

    # assigns a 'settlement' value to a node specified by a click within the 'Graph.onclick(confirm settlement)' function
    def assign_settlement_value(self):
        global second_settlement_player_2
        global second_settlement_player_1

        if updated_nodes.turn % 2 != 0:
            for r in updated_nodes.dict_prop:
                if r == key_settlement[0]:  # 'key settlement' is a list created within the Graph.create_graph
                    updated_nodes.dict_prop[r] = 'settlement_player_1'
                    score_player_1.set(str(Player_1.score) + ' Points')
                    second_settlement_player_1 = []
                    if updated_nodes.turn ==3:
                        second_settlement_player_1.append(r)
            # print(updated_nodes.dict_prop)
        if updated_nodes.turn % 2 == 0:
            for r in updated_nodes.dict_prop:
                if r == key_settlement[0]:  # 'key settlement' is a list created within the Graph.create_graph
                    updated_nodes.dict_prop[r] = 'settlement_player_2'
                    score_player_2.set(str(Player_2.score) + ' Points')
                    second_settlement_player_2 = []
                    if updated_nodes.turn ==2:
                        second_settlement_player_2.append(r)
            # print(updated_nodes.dict_prop)

    # assigns a 'city' value to a node specified by a click within the 'Graph.onclick(confirm city)' function
    def assign_city_value(self):
        if updated_nodes.turn % 2 != 0:
            for r in updated_nodes.dict_prop:
                if r == key_city[0]:  # 'key settlement' is a list created within the Graph.create_graph
                    updated_nodes.dict_prop[r] = 'city_player_1'
                    score_player_1.set(str(Player_1.score) + ' Points')

            # print(updated_nodes.dict_prop)
        if updated_nodes.turn % 2 == 0:
            for r in updated_nodes.dict_prop:
                if r == key_city[0]:  # 'key settlement' is a list created within the Graph.create_graph
                    updated_nodes.dict_prop[r] = 'city_player_2'
                    score_player_2.set(str(Player_2.score) + ' Points')

            # print(updated_nodes.dict_prop)

    # assigns a 'road' value to an edge specified by a click within the 'Graph.onclick(confirm road)' function
    def assign_road_value(self):

        # needed for the longest roads
        roads_neghbors = {  # 'A' hex
            (1, 2): ((2, 3), (1, 6)),
            (1, 6): ((1, 2), (5, 6), (6, 10)),

            (2, 3): ((1, 2), (3, 4), (3, 15)),
            (3, 4): ((2, 3), (4, 18), (3, 15), (4, 5)),
            (4, 5): ((3, 4), (4, 18), (5, 6), (5, 7)),
            (5, 6): ((1, 6), (4, 5), (5, 7), (6, 10)),

            # 'B' hex
            (5, 7): ((4, 5), (7, 20), (7, 8), (5, 6)),
            (7, 8): ((5, 7), (7, 20), (8, 11), (8, 9)),
            (8, 9): ((7, 8), (8, 11), (9, 10), (9, 14)),
            (9, 10): ((8, 9), (9, 14), (6, 10)),
            (6, 10): ((5, 6), (1, 6), (9, 10)),

            # 'C' hex
            (9, 14): ((8, 9), (13, 14), (9, 10)),
            (13, 14): ((9, 14), (12, 13)),

            (8, 11): ((7, 8), (8, 9), (11, 12), (11, 22)),
            (11, 12): ((8, 11), (11, 22), (12, 25), (12, 13)),
            (12, 13): ((11, 12), (12, 25), (13, 14)),

            # 'D' hex
            (3, 15): ((2, 3), (3, 4), (15, 16)),
            (15, 16): ((3, 15), (16, 26), (16, 17)),

            (16, 17): ((16, 26), (15, 16), (17, 29), (17, 18)),
            (17, 18): ((17, 29), (16, 17), (18, 19), (4, 18)),
            (4, 18): ((3, 4), (4, 5), (17, 18), (18, 19)),

            # 'E' hex, (4,18 - 4,5 - 5, 7 are done)
            (18, 19): ((17, 18),(4, 18),(19, 31), (19, 20)),
            (19, 20):((18, 19), (19, 31), (7, 20), (20, 21)),
            (7, 20): ((5, 7), (7, 8), (19, 20), (20, 21)),

            # 'F' hex (7, 20) (7,8) ( 8, 11) are done
            (20, 21): ((19, 20), (7, 20), (21, 22), (21, 33)),
            (21, 22): ((20, 21), (21, 33), (22, 23), (11, 22)),
            (11, 22): ((8, 11), (11, 12), (21, 22), (22, 23)),

            #'G' Hex
            (22, 23): ((21, 22), (11, 22), (23, 35), (23, 24)),
            (23, 24): ((22, 23), (23, 35), (24, 38), (24, 25)),
            (24, 25): ((23, 24), (24, 38), (12, 25)),
            (12, 25): ((11, 12), (12, 13), (24, 25)),

            # 'H' Hex
            (16, 26): ((15, 16), (16, 17), (26, 27)),
            (26, 27): ((16, 26), (27, 28)),
            (27, 28): ((26, 27), (28, 29), (28, 39)),
            (28, 29): ((27, 28), (28, 39), (29, 30), (17, 29)),
            (17, 29): ((28, 29), (29, 30), (16, 17), (17, 18)),

            #'I' Hex
            (29, 30): ((17, 29), (28, 29), (30, 41), (30, 31)),
            (30, 31): ((29, 30), (30, 41), (19, 31), (31, 32)),
            (19, 31): ((30, 31), (31, 32), (18, 19), (19, 20)),

            #'J' Hex
            (31, 32): ((30, 31), (19, 31), (32, 43), (32, 33)),
            (32, 33): ((31, 32), (32, 43), (21, 33), (33,34)),
            (21, 33): ((20, 21), (21, 22), (32, 33), (33, 34)),

            #'K Hex
            (33, 34): ((21, 33), (32, 33), (34, 45), (34, 35)),
            (34, 35): ((33, 34), (34, 45), (23, 35), (35, 36)),
            (23, 35): ((22, 23), (23, 24), (34, 35), (35, 36)),

            #'L" Hex
            (35, 36): ((23, 35), (34, 35), (36, 47), (36, 37)),
            (36, 37): ((35, 36), (36, 47), (37, 38)),
            (37, 38): ((36, 37), (24, 38)),
            (24, 38): ((23, 24), (24, 25), (37, 38)),

            #'M' Hex
            (28, 39): ((27, 28), (28, 29), (39, 40)),
            (39, 40): ((28, 39), (40, 41), (40, 48)),
            (40, 41): ((39, 40), (40, 48), (30, 41), (41, 42)),
            (30, 41): ((29, 30), (30, 31), (40, 41), (41, 42)),

            #'N' Hex
            (41, 42): ((30, 41), (40, 41), (42, 50), (42, 43)),
            (42, 43): ((41, 42), (42, 50), (32, 43), (43, 44)),
            (32, 43): ((31, 32), (32, 33), (42, 43), (43,44)),

            #'O' Hex
            (43, 44): ((32, 43), (42, 43), (44, 52), (44, 45)),
            (44, 45): ((43, 44), (44, 52), (34, 45), (45, 46)),
            (34, 45): ((33, 34), (34, 35), (44, 45), (45, 46)),

            #'P' Hex
            (45, 46): ((34, 45), (44, 45), (46, 54), (46, 47)),
            (46, 47): ((45, 46), (46, 54), (36, 47)),
            (36, 47): ((35, 36), (36, 37),(46, 47)),

            #'Q' Hex
            (40, 48): ((39, 40), (40, 41), (48, 49)),
            (48, 49): ((40, 48), (49, 50)),
            (49, 50): ((48, 49), (50, 51), (42, 50)),
            (42, 50): ((41, 42), (42, 43), (49, 50), (50, 51)),

            #'R' Hex
            (50, 51): ((49, 50), (42, 50), (51, 52)),
            (51, 52): ((50, 51), (44, 52), (52, 53)),
            (44, 52): ((51, 52), (52, 53), (43, 44), (44, 45)),

            #'S' Hex
            (52, 53): ((51, 52), (44, 52), (53, 54)),
            (53, 54): ((52, 53), (46, 54)),
            (46, 54): ((45, 46), (46, 47), (53, 54))



        }
        #
        # five_roads_player_1 = None
        # six_roads_player_1 = None
        # seven_roads_player_1 = None
        # eight_roads_player_1 = None
        # nine_roads_player_1 = None
        # ten_roads_player_1 = None
        # eleven_roads_player_1 = None
        # twelve_roads_player_1 = None
        #
        # five_roads_player_2 = None
        # six_roads_player_2 = None
        # seven_roads_player_2 = None
        # eight_roads_player_2 = None
        # nine_roads_player_2 = None
        # ten_roads_player_2 = None
        # eleven_roads_player_2 = None
        # twelve_roads_player_2 = None


        ########################################################################                    LONGEST ROAD                                ####################################################################


        if updated_nodes.turn % 2 != 0:


            for n in updated_nodes.dict_prop_roads:
                # if self.five_roads_player_1 == True and self.five_roads_player_2 != True:
                #     break

                if n == key_edges:  # 'key settlement' is a list created within the Graph.create_graph

                    updated_nodes.dict_prop_roads[n] = 'road_player_1'

                    longest_road_counter_player_1 = 1

                    # check for the second road

                    for elem in roads_neghbors[n]:

                        if updated_nodes.dict_prop_roads[elem] != 'road_player_1':
                            longest_road_counter_player_1 = 1
                            print(elem)
                            print('only one road in this direction, starting over')
                            # self.five_roads_player_1 = False
                            # self.six_roads_player_1 = False

                        elif updated_nodes.dict_prop_roads[elem] == 'road_player_1':
                            longest_road_counter_player_1 += 1
                            print(elem)
                            second_segment = list(roads_neghbors[elem])
                            print(second_segment)
                            print('second segment')
                            try:
                                for part in second_segment:
                                    if part == n or part in roads_neghbors[n]:
                                        second_segment.remove(n)
                            except ValueError:
                                self.six_roads_player_1 = True

                            for part in second_segment:
                                for inner_part in part:
                                    if inner_part in n:
                                        second_segment.remove(part)
                            print(second_segment)
                            print('second segment')
                            # self.five_roads_player_1 = False
                            # self.six_roads_player_1 = False

                            # check for the third road
                            for elem_elem in second_segment:
                                # if self.five_roads_player_1 == True:
                                #     break

                                if updated_nodes.dict_prop_roads[elem_elem] != 'road_player_1':
                                    longest_road_counter_player_1 = 2
                                    print(elem_elem)
                                    print('two roads in this direction, starting over')
                                    # self.five_roads_player_1 = False
                                    # self.six_roads_player_1 = False

                                elif updated_nodes.dict_prop_roads[elem_elem] == 'road_player_1':

                                    # if self.five_roads_player_1 == True:
                                    #     break

                                    longest_road_counter_player_1 += 1

                                    print(elem_elem)
                                    print(roads_neghbors[elem_elem])
                                    third_segment = list(roads_neghbors[elem_elem])
                                    print('third segment')

                                    for part_2 in third_segment:
                                        if part_2 == elem:
                                            third_segment.remove(elem)
                                    print(third_segment)
                                    # self.five_roads_player_1 = False
                                    # self.six_roads_player_1 = False

                                    # check for the fourth road:
                                    for elem_elem_elem in third_segment:
                                        # if self.five_roads_player_1 == True:
                                        #     break

                                        if updated_nodes.dict_prop_roads[elem_elem_elem] != 'road_player_1':
                                            print(longest_road_counter_player_1)
                                            longest_road_counter_player_1 = 3
                                            print('three roads in this direction -  starting over')
                                            # self.five_roads_player_1 = False
                                            # self.six_roads_player_1 = False

                                        elif updated_nodes.dict_prop_roads[elem_elem_elem] == 'road_player_1':
                                            # if self.five_roads_player_1 == True:
                                            #     break
                                            longest_road_counter_player_1 += 1
                                            print(elem_elem_elem)
                                            print(roads_neghbors[elem_elem_elem])
                                            fourth_segment = list(roads_neghbors[elem_elem_elem])
                                            print('fourth segment')
                                            for part_3 in fourth_segment:
                                                if part_3 == elem_elem:
                                                    fourth_segment.remove(elem_elem)
                                                print(fourth_segment)
                                                # self.five_roads_player_1 = False
                                                # self.six_roads_player_1 = False

                                            # check for the fifth road:
                                            for elem_elem_elem_elem in fourth_segment:
                                                # if self.five_roads_player_1 == True:
                                                #     break
                                                if updated_nodes.dict_prop_roads[
                                                    elem_elem_elem_elem] != 'road_player_1':
                                                    print(longest_road_counter_player_1)
                                                    longest_road_counter_player_1 = 4
                                                    print('four roads in this direction -  starting over')
                                                    # self.five_roads_player_1 = False
                                                    # self.six_roads_player_1 = False

                                                elif updated_nodes.dict_prop_roads[
                                                    elem_elem_elem_elem] == 'road_player_1':
                                                    # if self.five_roads_player_1 == True:
                                                    #     break

                                                    longest_road_counter_player_1 += 1
                                                    print(elem_elem_elem_elem)
                                                    print(roads_neghbors[elem_elem_elem_elem])
                                                    fifth_segment = list(roads_neghbors[elem_elem_elem_elem])
                                                    print('fifth segment')
                                                    for part_4 in fifth_segment:
                                                        if part_4 == elem_elem_elem:
                                                            fifth_segment.remove(elem_elem_elem)
                                                        print(fifth_segment)

                                                    self.five_roads_player_1 = True

                                                    # if self.five_roads_player_1 == True and self.five_roads_player_2 != True:
                                                    #     break

                                                    # check for the sixth road

                                                    for elem_elem_elem_elem_elem in fifth_segment:
                                                        # if updated_nodes.dict_prop_roads[
                                                        #     elem_elem_elem_elem_elem] != 'road_player_1':
                                                        #     print(longest_road_counter_player_1)
                                                        #     longest_road_counter_player_1 = 5
                                                        #     print('five roads in this direction -  starting over')
                                                        #     self.five_roads_player_1 = True
                                                        #     self.six_roads_player_1 = False

                                                        if updated_nodes.dict_prop_roads[
                                                            elem_elem_elem_elem_elem] == 'road_player_1':
                                                            longest_road_counter_player_1 += 1
                                                            print(elem_elem_elem_elem_elem)
                                                            print(roads_neghbors[elem_elem_elem_elem_elem])
                                                            sixth_segment = list(
                                                                roads_neghbors[elem_elem_elem_elem_elem])
                                                            print('sixth segment')

                                                            for part_5 in sixth_segment:
                                                                if part_5 == elem_elem_elem_elem or part_5 == n or part_5 == elem or part_5 == elem_elem or part_5 == elem_elem_elem:
                                                                    sixth_segment.remove(elem_elem_elem_elem)
                                                                print(sixth_segment)

                                                            self.six_roads_player_1 = True
                                                            # if self.six_roads_player_1 == True and self.six_roads_player_2 != True:
                                                            #     break

                                                            # check for the seventh road

                                                            for elem_elem_elem_elem_elem_elem in sixth_segment:
                                                                if elem_elem_elem_elem_elem_elem != n and elem_elem_elem_elem_elem_elem != elem_elem and \
                                                                        elem_elem_elem_elem_elem_elem != elem_elem_elem and elem_elem_elem_elem_elem_elem != elem_elem_elem_elem\
                                                                    and elem_elem_elem_elem_elem_elem != elem_elem_elem_elem_elem:
                                                                # if updated_nodes.dict_prop_roads[
                                                                #     elem_elem_elem_elem_elem_elem] != 'road_player_1':
                                                                #
                                                                #     self.five_roads_player_1 = True
                                                                #     self.six_roads_player_1 = True
                                                                #     self.seven_roads_player_1 = False

                                                                    if updated_nodes.dict_prop_roads[elem_elem_elem_elem_elem_elem] == 'road_player_1':

                                                                        seventh_segment = list(
                                                                            roads_neghbors[elem_elem_elem_elem_elem_elem])

                                                                        try:
                                                                            for part_6 in seventh_segment:
                                                                                if part_6 == elem_elem_elem_elem_elem or part_6 == n or part_6 == elem or part_6 == elem_elem or part_6 == elem_elem_elem_elem:

                                                                                    seventh_segment.remove(
                                                                                        elem_elem_elem_elem_elem)

                                                                        except ValueError:
                                                                            self.seven_roads_player_1 = True
                                                                            self.eight_roads_player_1 = False


                                                                        self.seven_roads_player_1 = True
                                                                        print('seventh segment is true')
                                                                        # if self.seven_roads_player_1 == True and self.seven_roads_player_2 != True:
                                                                        #     break

                                                                        # check for the eight road



                                                                        for elem_elem_elem_elem_elem_elem_elem in seventh_segment:


                                                                            if updated_nodes.dict_prop_roads[
                                                                                elem_elem_elem_elem_elem_elem_elem] == 'road_player_1':

                                                                                eighth_segment = list(roads_neghbors[
                                                                                                          elem_elem_elem_elem_elem_elem_elem])

                                                                                for part_7 in eighth_segment:
                                                                                    if part_7 == elem_elem_elem_elem_elem_elem:
                                                                                        eighth_segment.remove(
                                                                                            elem_elem_elem_elem_elem_elem)


                                                                                self.eight_roads_player_1 = True
                                                                                self.nine_roads_player_1 = False
                                                                                self.ten_roads_player_1 = False




                                                                                # if self.eight_roads_player_1 == True and self.eight_roads_player_2 != True:
                                                                                #     break

                                                                                # check for the ninth road

                                                                                for elem_elem_elem_elem_elem_elem_elem_elem in eighth_segment:


                                                                                    if updated_nodes.dict_prop_roads[
                                                                                        elem_elem_elem_elem_elem_elem_elem_elem] == 'road_player_1':

                                                                                        ninth_segment = list(
                                                                                            roads_neghbors[
                                                                                                elem_elem_elem_elem_elem_elem_elem_elem])

                                                                                        for part_8 in ninth_segment:
                                                                                            if part_8 == elem_elem_elem_elem_elem_elem_elem:
                                                                                                ninth_segment.remove(
                                                                                                    elem_elem_elem_elem_elem_elem_elem)


                                                                                        self.nine_roads_player_1 = True
                                                                                        #
                                                                                        # if self.nine_roads_player_1 == True and self.nine_roads_player_2 != True:
                                                                                        #     break

                                                                                        # check for the tenth road

                                                                                        for elem_elem_elem_elem_elem_elem_elem_elem_elem in ninth_segment:


                                                                                            if \
                                                                                                    updated_nodes.dict_prop_roads[
                                                                                                        elem_elem_elem_elem_elem_elem_elem_elem_elem] == 'road_player_1':

                                                                                                tenth_segment = list(
                                                                                                    roads_neghbors[
                                                                                                        elem_elem_elem_elem_elem_elem_elem_elem_elem])

                                                                                                for part_9 in tenth_segment:
                                                                                                    if part_9 == elem_elem_elem_elem_elem_elem_elem_elem:
                                                                                                        tenth_segment.remove(
                                                                                                            elem_elem_elem_elem_elem_elem_elem_elem)

                                                                                                self.ten_roads_player_1 = True

                                                                                                # if ten_roads_player_1 == True and self.ten_roads_player_2 != True:
                                                                                                #     break

                                                                                                # check for the eleventh road

                                                                                                for elem_elem_elem_elem_elem_elem_elem_elem_elem_elem in tenth_segment:


                                                                                                    if \
                                                                                                            updated_nodes.dict_prop_roads[
                                                                                                                elem_elem_elem_elem_elem_elem_elem_elem_elem_elem] == 'road_player_1':

                                                                                                        eleventh_segment = list(
                                                                                                            roads_neghbors[
                                                                                                                elem_elem_elem_elem_elem_elem_elem_elem_elem_elem])

                                                                                                        for part_10 in eleventh_segment:
                                                                                                            if part_10 == elem_elem_elem_elem_elem_elem_elem_elem_elem:
                                                                                                                eleventh_segment.remove(
                                                                                                                    elem_elem_elem_elem_elem_elem_elem_elem_elem)


                                                                                                        self.eleven_roads_player_1 = True

                                                                                                        # if self.eleven_roads_player_1 == True and self.eleven_roads_player_2 != True:
                                                                                                        #     break

                                                                                                        # check for the twelfth road

                                                                                                        for elem_elem_elem_elem_elem_elem_elem_elem_elem_elem_elem in eleventh_segment:


                                                                                                            if \
                                                                                                                    updated_nodes.dict_prop_roads[
                                                                                                                        elem_elem_elem_elem_elem_elem_elem_elem_elem_elem_elem] == 'road_player_1':

                                                                                                                twelfth_segment = list(
                                                                                                                    roads_neghbors[
                                                                                                                        elem_elem_elem_elem_elem_elem_elem_elem_elem_elem_elem])

                                                                                                                for part_11 in twelfth_segment:
                                                                                                                    if part_11 == elem_elem_elem_elem_elem_elem_elem_elem_elem_elem:
                                                                                                                        twelfth_segment.remove(
                                                                                                                            elem_elem_elem_elem_elem_elem_elem_elem_elem_elem)


                                                                                                                self.twelve_roads_player_1 = True

                                                                                                                # if self.twelve_roads_player_1 == True and self.twelve_roads_player_2 != True:
                                                                                                                #     break


            # five roads

            if self.five_roads_player_1 == True and self.five_roads_player_2 != True:
                if Player_1.longest_road != True and Player_2.longest_road != True:
                    Player_1.longest_road = True
                    Player_2.longest_road = False
                    Player_1.score += 2
                    score_player_1.set(str(Player_1.score) + ' Points')



            elif self.five_roads_player_1 == True and self.five_roads_player_2 == True and self.six_roads_player_2 != True:

                if Player_2.longest_road == True:

                    Player_1.longest_road = False
                    Player_2.longest_road = False
                    Player_2.score -= 2
                    score_player_2.set(str(Player_2.score) + ' Points')


            # six roads

            if self.six_roads_player_1 == True and self.six_roads_player_2 != True:
                if Player_1.longest_road != True and Player_2.longest_road != True:
                    Player_1.longest_road = True
                    Player_2.longest_road = False
                    Player_1.score += 2
                    score_player_1.set(str(Player_1.score) + ' Points')


            elif self.six_roads_player_1 == True and self.six_roads_player_2 == True and self.seven_roads_player_2 !=True:
                if Player_2.longest_road == True:

                    Player_2.longest_road = False
                    Player_2.score -= 2
                    score_player_2.set(str(Player_2.score) + ' Points')

            # seven roads

            if self.seven_roads_player_1 == True and self.seven_roads_player_2 != True:

                if Player_1.longest_road != True and Player_2.longest_road != True:
                    Player_1.longest_road = True
                    Player_2.longest_road = False
                    Player_1.score += 2
                    score_player_1.set(str(Player_1.score) + ' Points')


            elif self.seven_roads_player_1 == True and self.seven_roads_player_2 == True and self.eight_roads_player_2 !=True:

                if Player_2.longest_road == True:

                    Player_2.longest_road = False
                    Player_2.score -= 2
                    score_player_2.set(str(Player_2.score) + ' Points')

            # eight roads

            if self.eight_roads_player_1 == True and self.eight_roads_player_2 != True:
                if Player_1.longest_road != True and Player_2.longest_road != True:
                    Player_1.longest_road = True
                    Player_2.longest_road = False
                    Player_1.score += 2
                    score_player_1.set(str(Player_1.score) + ' Points')


            elif self.eight_roads_player_1 == True and self.eight_roads_player_2 == True and self.nine_roads_player_2 != True:
                if Player_2.longest_road == True:

                    Player_2.longest_road = False
                    Player_2.score -= 2
                    score_player_2.set(str(Player_2.score) + ' Points')
            # nine roads

            if self.nine_roads_player_1 == True and self.nine_roads_player_2 != True:
                if Player_1.longest_road != True and Player_2.longest_road != True:
                    Player_1.longest_road = True
                    Player_2.longest_road = False
                    Player_1.score += 2
                    score_player_1.set(str(Player_1.score) + ' Points')



            elif self.nine_roads_player_1 == True and self.nine_roads_player_2 == True and self.ten_roads_player_2 !=True:
                if Player_2.longest_road == True:

                    Player_2.longest_road = False
                    Player_2.score -= 2
                    score_player_2.set(str(Player_2.score) + ' Points')

            # ten roads

            if self.ten_roads_player_1 == True and self.ten_roads_player_2 != True:
                if Player_1.longest_road != True and Player_2.longest_road != True:
                    Player_1.longest_road = True
                    Player_2.longest_road = False
                    Player_1.score += 2
                    score_player_1.set(str(Player_1.score) + ' Points')


            elif self.ten_roads_player_1 == True and self.ten_roads_player_2 == True and self.eleven_roads_player_2 !=True:
                Player_2.longest_road = False
                Player_2.score -= 2
                score_player_2.set(str(Player_2.score) + ' Points')
            # eleven roads

            if self.eleven_roads_player_1 == True and self.eleven_roads_player_2 != True:
                if Player_1.longest_road != True and Player_2.longest_road != True:
                    Player_1.longest_road = True
                    Player_2.longest_road = False
                    Player_1.score += 2
                    score_player_1.set(str(Player_1.score) + ' Points')


            elif self.eleven_roads_player_1 == True and self.eleven_roads_player_2 == True and self.twelve_roads_player_2 != True:
                Player_2.longest_road = False
                Player_2.score -= 2
                score_player_2.set(str(Player_2.score) + ' Points')

            # twelve roads

            if self.twelve_roads_player_1 == True and self.twelve_roads_player_2 != True:
                if Player_1.longest_road != True and Player_2.longest_road != True:
                    Player_1.longest_road = True
                    Player_2.longest_road = False
                    Player_1.score += 2
                    score_player_1.set(str(Player_1.score) + ' Points')


            elif self.twelve_roads_player_1 == True and self.twelve_roads_player_2 == True:
                Player_2.longest_road = False
                Player_2.score -= 2
                score_player_2.set(str(Player_2.score) + ' Points')




        elif updated_nodes.turn % 2 == 0:
            for n in updated_nodes.dict_prop_roads:
                # if self.five_roads_player_1 == True and self.five_roads_player_2 != True:
                #     break

                for n in updated_nodes.dict_prop_roads:
                    # if self.five_roads_player_2 == True and self.five_roads_player_2 != True:
                    #     break

                    if n == key_edges:  # 'key settlement' is a list created within the Graph.create_graph

                        updated_nodes.dict_prop_roads[n] = 'road_player_2'

                        longest_road_counter_player_1 = 1
                        print(roads_neghbors[n])

                        # check for the second road

                        for elem in roads_neghbors[n]:
                            # if self.five_roads_player_2 == True:
                            #     break

                            if updated_nodes.dict_prop_roads[elem] != 'road_player_2':
                                longest_road_counter_player_1 = 1
                                print(elem)
                                print('only one road in this direction, starting over')
                                # self.five_roads_player_2 = False
                                # self.six_roads_player_2 = False

                            elif updated_nodes.dict_prop_roads[elem] == 'road_player_2':
                                longest_road_counter_player_1 += 1
                                print(elem)
                                second_segment = list(roads_neghbors[elem])
                                print(second_segment)
                                print('second segment')
                                try:
                                    for part in second_segment:
                                        if part == n or part in roads_neghbors[n]:
                                            second_segment.remove(n)
                                except ValueError:
                                    self.six_roads_player_2 = True

                                for part in second_segment:
                                    for inner_part in part:
                                        if inner_part in n:
                                            second_segment.remove(part)
                                print(second_segment)
                                print('second segment')
                                # self.five_roads_player_2 = False
                                # self.six_roads_player_2 = False

                                # check for the third road
                                for elem_elem in second_segment:
                                    # if self.five_roads_player_2 == True:
                                    #     break

                                    if updated_nodes.dict_prop_roads[elem_elem] != 'road_player_2':
                                        longest_road_counter_player_1 = 2
                                        print(elem_elem)
                                        print('two roads in this direction, starting over')
                                        # self.five_roads_player_2 = False
                                        # self.six_roads_player_2 = False

                                    elif updated_nodes.dict_prop_roads[elem_elem] == 'road_player_2':

                                        # if self.five_roads_player_2 == True:
                                        #     break

                                        longest_road_counter_player_1 += 1

                                        print(elem_elem)
                                        print(roads_neghbors[elem_elem])
                                        third_segment = list(roads_neghbors[elem_elem])
                                        print('third segment')

                                        for part_2 in third_segment:
                                            if part_2 == elem:
                                                third_segment.remove(elem)
                                        print(third_segment)
                                        # self.five_roads_player_2 = False
                                        # self.six_roads_player_2 = False

                                        # check for the fourth road:
                                        for elem_elem_elem in third_segment:
                                            # if self.five_roads_player_2 == True:
                                            #     break

                                            if updated_nodes.dict_prop_roads[elem_elem_elem] != 'road_player_2':
                                                print(longest_road_counter_player_1)
                                                longest_road_counter_player_1 = 3
                                                print('three roads in this direction -  starting over')
                                                # self.five_roads_player_2 = False
                                                # self.six_roads_player_2 = False

                                            elif updated_nodes.dict_prop_roads[elem_elem_elem] == 'road_player_2':
                                                # if self.five_roads_player_2 == True:
                                                #     break
                                                longest_road_counter_player_1 += 1
                                                print(elem_elem_elem)
                                                print(roads_neghbors[elem_elem_elem])
                                                fourth_segment = list(roads_neghbors[elem_elem_elem])
                                                print('fourth segment')
                                                for part_3 in fourth_segment:
                                                    if part_3 == elem_elem:
                                                        fourth_segment.remove(elem_elem)
                                                    print(fourth_segment)
                                                    # self.five_roads_player_2 = False
                                                    # self.six_roads_player_2 = False

                                                # check for the fifth road:
                                                for elem_elem_elem_elem in fourth_segment:
                                                    # if self.five_roads_player_2 == True:
                                                    #     break
                                                    if updated_nodes.dict_prop_roads[
                                                        elem_elem_elem_elem] != 'road_player_2':
                                                        print(longest_road_counter_player_1)
                                                        longest_road_counter_player_1 = 4
                                                        print('four roads in this direction -  starting over')
                                                        # self.five_roads_player_2 = False
                                                        # self.six_roads_player_2 = False

                                                    elif updated_nodes.dict_prop_roads[
                                                        elem_elem_elem_elem] == 'road_player_2':
                                                        # if self.five_roads_player_2 == True:
                                                        #     break

                                                        longest_road_counter_player_1 += 1
                                                        print(elem_elem_elem_elem)
                                                        print(roads_neghbors[elem_elem_elem_elem])
                                                        fifth_segment = list(roads_neghbors[elem_elem_elem_elem])
                                                        print('fifth segment')
                                                        for part_4 in fifth_segment:
                                                            if part_4 == elem_elem_elem:
                                                                fifth_segment.remove(elem_elem_elem)
                                                            print(fifth_segment)

                                                        self.five_roads_player_2 = True

                                                        # if self.five_roads_player_2 == True and self.five_roads_player_2 != True:
                                                        #     break

                                                        # check for the sixth road

                                                        for elem_elem_elem_elem_elem in fifth_segment:
                                                            # if updated_nodes.dict_prop_roads[
                                                            #     elem_elem_elem_elem_elem] != 'road_player_2':
                                                            #     print(longest_road_counter_player_1)
                                                            #     longest_road_counter_player_1 = 5
                                                            #     print('five roads in this direction -  starting over')
                                                            #     self.five_roads_player_2 = True
                                                            #     self.six_roads_player_2 = False

                                                            if updated_nodes.dict_prop_roads[
                                                                elem_elem_elem_elem_elem] == 'road_player_2':
                                                                longest_road_counter_player_1 += 1
                                                                print(elem_elem_elem_elem_elem)
                                                                print(roads_neghbors[elem_elem_elem_elem_elem])
                                                                sixth_segment = list(
                                                                    roads_neghbors[elem_elem_elem_elem_elem])
                                                                print('sixth segment')

                                                                for part_5 in sixth_segment:
                                                                    if part_5 == elem_elem_elem_elem or part_5 == n or part_5 == elem or part_5 == elem_elem or part_5 == elem_elem_elem:
                                                                        sixth_segment.remove(elem_elem_elem_elem)
                                                                    print(sixth_segment)

                                                                self.six_roads_player_2 = True
                                                                # if self.six_roads_player_2 == True and self.six_roads_player_2 != True:
                                                                #     break

                                                                # check for the seventh road

                                                                for elem_elem_elem_elem_elem_elem in sixth_segment:
                                                                    if elem_elem_elem_elem_elem_elem != n and elem_elem_elem_elem_elem_elem != elem_elem and \
                                                                            elem_elem_elem_elem_elem_elem != elem_elem_elem and elem_elem_elem_elem_elem_elem != elem_elem_elem_elem \
                                                                            and elem_elem_elem_elem_elem_elem != elem_elem_elem_elem_elem:
                                                                        # if updated_nodes.dict_prop_roads[
                                                                        #     elem_elem_elem_elem_elem_elem] != 'road_player_2':
                                                                        #
                                                                        #     self.five_roads_player_2 = True
                                                                        #     self.six_roads_player_2 = True
                                                                        #     self.seven_roads_player_2 = False

                                                                        if updated_nodes.dict_prop_roads[
                                                                            elem_elem_elem_elem_elem_elem] == 'road_player_2':

                                                                            seventh_segment = list(
                                                                                roads_neghbors[
                                                                                    elem_elem_elem_elem_elem_elem])

                                                                            try:
                                                                                for part_6 in seventh_segment:
                                                                                    if part_6 == elem_elem_elem_elem_elem or part_6 == n or part_6 == elem or part_6 == elem_elem or part_6 == elem_elem_elem_elem:
                                                                                        seventh_segment.remove(
                                                                                            elem_elem_elem_elem_elem)

                                                                            except ValueError:
                                                                                self.seven_roads_player_2 = True
                                                                                self.eight_roads_player_2 = False

                                                                            self.seven_roads_player_2 = True
                                                                            print('seventh segment is true')
                                                                            # if self.seven_roads_player_2 == True and self.seven_roads_player_2 != True:
                                                                            #     break

                                                                            # check for the eight road

                                                                            for elem_elem_elem_elem_elem_elem_elem in seventh_segment:

                                                                                if updated_nodes.dict_prop_roads[
                                                                                    elem_elem_elem_elem_elem_elem_elem] == 'road_player_2':

                                                                                    eighth_segment = list(
                                                                                        roads_neghbors[
                                                                                            elem_elem_elem_elem_elem_elem_elem])

                                                                                    for part_7 in eighth_segment:
                                                                                        if part_7 == elem_elem_elem_elem_elem_elem:
                                                                                            eighth_segment.remove(
                                                                                                elem_elem_elem_elem_elem_elem)

                                                                                    self.eight_roads_player_2 = True
                                                                                    self.nine_roads_player_2 = False
                                                                                    self.ten_roads_player_2 = False

                                                                                    # if self.eight_roads_player_2 == True and self.eight_roads_player_2 != True:
                                                                                    #     break

                                                                                    # check for the ninth road

                                                                                    for elem_elem_elem_elem_elem_elem_elem_elem in eighth_segment:

                                                                                        if \
                                                                                        updated_nodes.dict_prop_roads[
                                                                                            elem_elem_elem_elem_elem_elem_elem_elem] == 'road_player_2':

                                                                                            ninth_segment = list(
                                                                                                roads_neghbors[
                                                                                                    elem_elem_elem_elem_elem_elem_elem_elem])

                                                                                            for part_8 in ninth_segment:
                                                                                                if part_8 == elem_elem_elem_elem_elem_elem_elem:
                                                                                                    ninth_segment.remove(
                                                                                                        elem_elem_elem_elem_elem_elem_elem)

                                                                                            self.nine_roads_player_2 = True
                                                                                            #
                                                                                            # if self.nine_roads_player_2 == True and self.nine_roads_player_2 != True:
                                                                                            #     break

                                                                                            # check for the tenth road

                                                                                            for elem_elem_elem_elem_elem_elem_elem_elem_elem in ninth_segment:

                                                                                                if \
                                                                                                        updated_nodes.dict_prop_roads[
                                                                                                            elem_elem_elem_elem_elem_elem_elem_elem_elem] == 'road_player_2':

                                                                                                    tenth_segment = list(
                                                                                                        roads_neghbors[
                                                                                                            elem_elem_elem_elem_elem_elem_elem_elem_elem])

                                                                                                    for part_9 in tenth_segment:
                                                                                                        if part_9 == elem_elem_elem_elem_elem_elem_elem_elem:
                                                                                                            tenth_segment.remove(
                                                                                                                elem_elem_elem_elem_elem_elem_elem_elem)

                                                                                                    self.ten_roads_player_2 = True

                                                                                                    # if ten_roads_player_2 == True and self.ten_roads_player_2 != True:
                                                                                                    #     break

                                                                                                    # check for the eleventh road

                                                                                                    for elem_elem_elem_elem_elem_elem_elem_elem_elem_elem in tenth_segment:

                                                                                                        if \
                                                                                                                updated_nodes.dict_prop_roads[
                                                                                                                    elem_elem_elem_elem_elem_elem_elem_elem_elem_elem] == 'road_player_2':

                                                                                                            eleventh_segment = list(
                                                                                                                roads_neghbors[
                                                                                                                    elem_elem_elem_elem_elem_elem_elem_elem_elem_elem])

                                                                                                            for part_10 in eleventh_segment:
                                                                                                                if part_10 == elem_elem_elem_elem_elem_elem_elem_elem_elem:
                                                                                                                    eleventh_segment.remove(
                                                                                                                        elem_elem_elem_elem_elem_elem_elem_elem_elem)

                                                                                                            self.eleven_roads_player_2 = True

                                                                                                            # if self.eleven_roads_player_2 == True and self.eleven_roads_player_2 != True:
                                                                                                            #     break

                                                                                                            # check for the twelfth road

                                                                                                            for elem_elem_elem_elem_elem_elem_elem_elem_elem_elem_elem in eleventh_segment:

                                                                                                                if \
                                                                                                                        updated_nodes.dict_prop_roads[
                                                                                                                            elem_elem_elem_elem_elem_elem_elem_elem_elem_elem_elem] == 'road_player_2':

                                                                                                                    twelfth_segment = list(
                                                                                                                        roads_neghbors[
                                                                                                                            elem_elem_elem_elem_elem_elem_elem_elem_elem_elem_elem])

                                                                                                                    for part_11 in twelfth_segment:
                                                                                                                        if part_11 == elem_elem_elem_elem_elem_elem_elem_elem_elem_elem:
                                                                                                                            twelfth_segment.remove(
                                                                                                                                elem_elem_elem_elem_elem_elem_elem_elem_elem_elem)

                                                                                                                    self.twelve_roads_player_2 = True

                                                                                                                    # if self.twelve_roads_player_2 == True and self.twelve_roads_player_2 != True:
                                                                                                                    #     break

            # five roads

            if self.five_roads_player_2 == True and self.five_roads_player_1 != True:
                if Player_1.longest_road != True and Player_2.longest_road != True:
                    Player_2.longest_road = True
                    Player_1.longest_road = False
                    Player_2.score += 2
                    score_player_2.set(str(Player_2.score) + ' Points')


            elif self.five_roads_player_2 == True and self.five_roads_player_1 == True and self.six_roads_player_1 != True:
                if Player_1.longest_road == True:

                    Player_1.longest_road = False
                    Player_1.score -= 2
                    score_player_1.set(str(Player_1.score) + ' Points')

            # six roads

            if self.six_roads_player_2 == True and self.six_roads_player_1 != True:
                if Player_1.longest_road != True and Player_2.longest_road != True:
                    Player_2.longest_road = True
                    Player_1.longest_road = False
                    Player_2.score += 2
                    score_player_2.set(str(Player_2.score) + ' Points')


            elif self.six_roads_player_2 == True and self.six_roads_player_1 == True and self.seven_roads_player_1 != True:
                if Player_1.longest_road == True:

                    Player_1.longest_road = False
                    Player_1.score -= 2
                    score_player_1.set(str(Player_1.score) + ' Points')


            # seven roads

            if self.seven_roads_player_2 == True and self.seven_roads_player_1 != True:
                if Player_1.longest_road != True and Player_2.longest_road != True:
                    Player_2.longest_road = True
                    Player_1.longest_road = False
                    Player_2.score += 2
                    score_player_2.set(str(Player_2.score) + ' Points')


            elif self.seven_roads_player_2 == True and self.seven_roads_player_1 == True and self.eight_roads_player_1 != True:
                if Player_1.longest_road == True:

                    Player_1.longest_road = False
                    Player_1.score -= 2
                    score_player_1.set(str(Player_1.score) + ' Points')
            # eight roads

            if self.eight_roads_player_2 == True and self.eight_roads_player_1 != True:
                if Player_1.longest_road != True and Player_2.longest_road != True:
                    Player_2.longest_road = True
                    Player_1.longest_road = False
                    Player_2.score += 2
                    score_player_2.set(str(Player_2.score) + ' Points')


            elif self.eight_roads_player_2 == True and self.eight_roads_player_1 == True and self.nine_roads_player_1 != True:
                if Player_1.longest_road == True:

                    Player_1.longest_road = False
                    Player_1.score -= 2
                    score_player_1.set(str(Player_1.score) + ' Points')

            # nine roads

            if self.nine_roads_player_2 == True and self.nine_roads_player_1 != True:
                if Player_1.longest_road != True and Player_2.longest_road != True:
                    Player_2.longest_road = True
                    Player_1.longest_road = False
                    Player_2.score += 2
                    score_player_2.set(str(Player_2.score) + ' Points')



            elif self.nine_roads_player_1 == True and self.nine_roads_player_2 == True and self.ten_roads_player_1 != True:
                if Player_1.longest_road == True:

                    Player_1.longest_road = False
                    Player_1.score -= 2
                    score_player_1.set(str(Player_1.score) + ' Points')

            # ten roads

            if self.ten_roads_player_2 == True and self.ten_roads_player_1 != True:
                if Player_1.longest_road != True and Player_2.longest_road != True:
                    Player_2.longest_road = True
                    Player_1.longest_road = False
                    Player_2.score += 2
                    score_player_2.set(str(Player_2.score) + ' Points')

            elif self.ten_roads_player_2 == True and self.ten_roads_player_1 == True and self.eleven_roads_player_1 != True:
                if Player_1.longest_road == True:

                    Player_1.longest_road = False
                    Player_1.score -= 2
                    score_player_1.set(str(Player_1.score) + ' Points')
            # eleven roads

            if self.eleven_roads_player_2 == True and self.eleven_roads_player_1 != True:
                if Player_1.longest_road != True and Player_2.longest_road != True:
                    Player_2.longest_road = True
                    Player_1.longest_road = False
                    Player_2.score += 2
                    score_player_2.set(str(Player_2.score) + ' Points')


            elif self.eleven_roads_player_2 == True and self.eleven_roads_player_1 == True and self.twelve_roads_player_1 !=True:
                if Player_1.longest_road == True:

                    Player_1.longest_road = False
                    Player_1.score -= 2
                    score_player_1.set(str(Player_1.score) + ' Points')

            # twelve roads

            if self.twelve_roads_player_2 == True and self.twelve_roads_player_1 != True:
                if Player_1.longest_road != True and Player_2.longest_road != True:
                    Player_2.longest_road = True
                    Player_1.longest_road = False
                    Player_2.score += 2
                    score_player_2.set(str(Player_2.score) + ' Points')


            elif self.twelve_roads_player_2 == True and self.twelve_roads_player_1 == True:
                if Player_1.longest_road == True:

                    Player_1.longest_road = False
                    Player_1.score -= 2
                    score_player_1.set(str(Player_1.score) + ' Points')

        print(self.five_roads_player_1)
        print(self.six_roads_player_1)
        print(self.seven_roads_player_1)
        print(self.eight_roads_player_1)
        print(self.nine_roads_player_1)
        print(self.ten_roads_player_1)
        print('now second player')
        print(self.five_roads_player_2)
        print(self.six_roads_player_2)
        print(self.seven_roads_player_2)
        print(self.eight_roads_player_2)
        print(self.nine_roads_player_2)
        print(self.ten_roads_player_2)




    def assign_robber(self):
        print(key_knight_card)
        for n in updated_nodes.dict_mid_nodes_for_robber:
            print('\'' + n + '\'')
            # if ('\'' +n+'\'') == key_knight_card[0]:
            if n == str(key_knight_card[0]):
                updated_nodes.dict_mid_nodes_for_robber[n] = 'robber'
            else:
                updated_nodes.dict_mid_nodes_for_robber[n] = 'None'


updated_nodes = Graph_Properties(1)


# create a 'player' class (maybe store score, resources and so on in it later?)
class Player:
    def __init__(self, score, hay, lumber, rock, brick, sheep, knight_times_played, largest_army=None,
                 longest_road=None):
        self.score = score
        self.hay = hay
        self.lumber = lumber
        self.rock = rock
        self.brick = brick
        self.sheep = sheep
        self.knight_times_played = knight_times_played
        if largest_army is None:
            largest_army = []
        self.largest_army = largest_army
        if longest_road is None:
            longest_road = []
        self.longest_road = longest_road



Player_1 = Player(0, 0, 0, 0, 0, 0, 0)
Player_2 = Player(0, 0, 0, 0, 0, 0, 0)



#####################################################                          functions of the buttons         ############################################################


# Clears the canvas and plots a new graph

def change_view_settlement():
    player1_build_road.place_forget()
    player1_build_settlement.place_forget()
    player1_build_city.place_forget()
    player1_buy_dev_card.place_forget()

    if updated_nodes.turn % 2 != 0:
        if Player_1.brick > 0 and Player_1.lumber > 0 and Player_1.sheep > 0 and Player_1.hay > 0:

            plt.close(f)

            start_graph.clearPlotPage()
            settlement_graph.create_graph()
            player1_build_road.place_forget()
            player1_build_settlement.place_forget()
            player1_build_city.place_forget()
            player1_buy_dev_card.place_forget()
            player1_trade["state"] = "disabled"
            player1_use_dev_card["state"] = "disabled"
            player1_build["state"] = "disabled"
            player1_end_turn["state"] = "disabled"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'normal'
            player1_confirm['state'] = 'disabled'

        else:
            messagebox.showinfo("", "Not enough resources to do that!")


    elif updated_nodes.turn % 2 == 0:
        if Player_2.brick > 0 and Player_2.lumber > 0 and Player_2.sheep > 0 and Player_2.hay > 0:

            plt.close(f)

            start_graph.clearPlotPage()
            settlement_graph.create_graph()
            player1_build_road.place_forget()
            player1_build_settlement.place_forget()
            player1_build_city.place_forget()
            player1_buy_dev_card.place_forget()
            player1_trade["state"] = "disabled"
            player1_use_dev_card["state"] = "disabled"
            player1_build["state"] = "disabled"
            player1_end_turn["state"] = "disabled"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'normal'
            player1_confirm['state'] = 'disabled'

        else:
            messagebox.showinfo("", "Not enough resources to do that!")


def change_view_city():
    player1_build_road.place_forget()
    player1_build_settlement.place_forget()
    player1_build_city.place_forget()
    player1_buy_dev_card.place_forget()

    if updated_nodes.turn % 2 != 0:
        if Player_1.rock > 2 and Player_1.hay > 1:

            plt.close(f)

            start_graph.clearPlotPage()
            city_graph.create_graph()
            player1_build_road.place_forget()
            player1_build_settlement.place_forget()
            player1_build_city.place_forget()
            player1_buy_dev_card.place_forget()
            player1_trade["state"] = "disabled"
            player1_use_dev_card["state"] = "disabled"
            player1_build["state"] = "disabled"
            player1_end_turn["state"] = "disabled"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'normal'
            player1_confirm['state'] = 'disabled'

        else:
            messagebox.showinfo("", "Not enough resources to do that!")


    elif updated_nodes.turn % 2 == 0:
        if Player_2.rock > 2 and Player_2.hay > 1:

            plt.close(f)

            start_graph.clearPlotPage()
            city_graph.create_graph()
            player1_build_road.place_forget()
            player1_build_settlement.place_forget()
            player1_build_city.place_forget()
            player1_buy_dev_card.place_forget()
            player1_trade["state"] = "disabled"
            player1_use_dev_card["state"] = "disabled"
            player1_build["state"] = "disabled"
            player1_end_turn["state"] = "disabled"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'normal'
            player1_confirm['state'] = 'disabled'

        else:
            messagebox.showinfo("", "Not enough resources to do that!")


# confirms selection based on the type of action performed.
def confirm_selection():
    global counter_road_building_dev_card
    global road_counter

    def reduce_road_building():
        buy_development_card.cards_player_1.road_building -= 1
        road_building_amount.set(
            'Road Building' + ' (' + str(buy_development_card.cards_player_1.road_building) + ')')

    def reduce_road_building_2():
        buy_development_card.cards_player_2.road_building -= 1
        road_building_amount2.set(
            'Road Building' + ' (' + str(buy_development_card.cards_player_2.road_building) + ')')

    if x == ['settlement']:
        # dict_properties.update({1:'settlement'})
        plt.close(f)
        settlement_graph.clearPlotPage()
        start_graph.create_graph()



    elif x == ['confirm_settlement']:

        if updated_nodes.turn % 2 != 0 and updated_nodes.turn != 1 and updated_nodes.turn !=3:

            Player_1.sheep -= 1
            Player_1.lumber -= 1
            Player_1.hay -= 1
            Player_1.brick -= 1

            sheep.set(Player_1.sheep)
            lumber.set(Player_1.lumber)
            hay.set(Player_1.hay)
            brick.set(Player_1.brick)

            Player_1.score += 1
            score_player_1.set(Player_1.score)
            if Player_1.score >= 10:
                messagebox.showinfo('', 'Congratulations! Player 1 wins!')
                root.quit()
            elif Player_2.score >= 10:
                messagebox.showinfo('', 'Congratulations! Player 2 wins!')
                root.quit()


        elif updated_nodes.turn % 2 == 0 and updated_nodes.turn != 2:

            Player_2.sheep -= 1
            Player_2.lumber -= 1
            Player_2.hay -= 1
            Player_2.brick -= 1

            sheep2.set(Player_2.sheep)
            lumber2.set(Player_2.lumber)
            hay2.set(Player_2.hay)
            brick2.set(Player_2.brick)

            Player_2.score += 1
            score_player_2.set(Player_2.score)

            if Player_1.score >= 10:
                messagebox.showinfo('', 'Congratulations! Player 1 wins!')
                root.quit()
            elif Player_2.score >= 10:
                messagebox.showinfo('', 'Congratulations! Player 2 wins!')
                root.quit()

        plt.close(f)

        if updated_nodes.turn == 1 or updated_nodes.turn == 3:
            confirm_settlement_graph.clearPlotPage()
            updated_nodes.assign_settlement_value()
            Player_1.score += 1
            if updated_nodes.turn == 1:
                score_player_1.set(str(Player_1.score) + ' Point')
            elif updated_nodes.turn == 3:
                score_player_1.set(str(Player_1.score) + ' Points')

            if Player_1.score >= 10:
                messagebox.showinfo('', 'Congratulations! Player 1 wins!')
                root.quit()
            elif Player_2.score >= 10:
                messagebox.showinfo('', 'Congratulations! Player 2 wins!')
                root.quit()


            road_graph.create_graph()
            player1_trade["state"] = "disabled"
            player1_use_dev_card["state"] = "disabled"
            player1_build["state"] = "disabled"
            player1_end_turn["state"] = "disabled"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'

        elif updated_nodes.turn == 2:
            settlement_counter = 0
            confirm_settlement_graph.clearPlotPage()
            updated_nodes.assign_settlement_value()
            Player_2.score += 1
            if Player_2.score == 1:
                score_player_2.set(str(Player_2.score) + ' Point')
            else:
                score_player_2.set(str(Player_2.score) + ' Points')

            road_graph.create_graph()
            player1_trade["state"] = "disabled"
            player1_use_dev_card["state"] = "disabled"
            player1_build["state"] = "disabled"
            player1_end_turn["state"] = "disabled"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'

        else:
            confirm_settlement_graph.clearPlotPage()
            updated_nodes.assign_settlement_value()
            player1_trade["state"] = "normal"
            player1_use_dev_card["state"] = "normal"
            player1_build["state"] = "normal"
            player1_end_turn["state"] = "normal"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'
            # print(updated_nodes.dict_prop)
            # for r in updated_nodes.dict_prop:
            #     if r == key_settlement:
            #         print(updated_nodes[r].dict_prop)
            # updated_nodes.dict_prop.update({1:'settlement'})
            # print(updated_nodes.dict_prop)
            # print(Player_2.score)
            start_graph.create_graph()

            if Player_1.score >= 10:
                messagebox.showinfo('', 'Congratulations! Player 1 wins!')
                root.quit()
            elif Player_2.score >= 10:
                messagebox.showinfo('', 'Congratulations! Player 2 wins!')
                root.quit()

    elif x == ['confirm_city']:

        if updated_nodes.turn % 2 != 0:

            Player_1.hay -= 2
            Player_1.rock -= 3

            hay.set(Player_1.hay)
            rock.set(Player_1.rock)

            Player_1.score += 1

            if Player_1.score >= 10:
                messagebox.showinfo('', 'Congratulations! Player 1 wins!')
                root.quit()
            elif Player_2.score >= 10:
                messagebox.showinfo('', 'Congratulations! Player 2 wins!')
                root.quit()

        elif updated_nodes.turn % 2 == 0:

            Player_2.hay -= 2
            Player_2.rock -= 3

            hay2.set(Player_2.hay)
            rock2.set(Player_2.rock)

            Player_2.score += 1

            if Player_1.score >= 10:
                messagebox.showinfo('', 'Congratulations! Player 1 wins!')
                root.quit()
            elif Player_2.score >= 10:
                messagebox.showinfo('', 'Congratulations! Player 2 wins!')
                root.quit()

        plt.close(f)
        confirm_city_graph.clearPlotPage()
        updated_nodes.assign_city_value()
        # print(updated_nodes.dict_prop)
        # for r in updated_nodes.dict_prop:
        #     if r == key_settlement:
        #         print(updated_nodes[r].dict_prop)
        # updated_nodes.dict_prop.update({1:'settlement'})
        # print(updated_nodes.dict_prop)
        Player_2.score += 1
        # print(Player_2.score)
        start_graph.create_graph()
        player1_trade["state"] = "normal"
        player1_use_dev_card["state"] = "normal"
        player1_build["state"] = "normal"
        player1_end_turn["state"] = "normal"
        player1_roll_dice["state"] = "disabled"
        player1_cancel['state'] = 'normal'
        player1_confirm['state'] = 'normal'
        player1_cancel['state'] = 'disabled'
        player1_confirm['state'] = 'disabled'

    elif x == ['road']:
        plt.close(f)
        road_graph.clearPlotPage()
        start_graph.create_graph()


    elif x == ['confirm_road']:

        if updated_nodes.turn % 2 != 0 and updated_nodes.turn != 1 and updated_nodes.turn != 3:

            Player_1.brick -= 1
            Player_1.lumber -= 1

            brick.set(Player_1.brick)
            lumber.set(Player_1.lumber)

        elif updated_nodes.turn % 2 == 0 and updated_nodes.turn !=2:

            Player_2.brick -= 1
            Player_2.lumber -= 1

            brick2.set(Player_2.brick)
            lumber2.set(Player_2.lumber)


        if updated_nodes.turn == 1:
            plt.close(f)

            confirm_road_graph.clearPlotPage()
            updated_nodes.assign_road_value()
            player1_trade["state"] = "disabled"
            player1_use_dev_card["state"] = "disabled"
            player1_build["state"] = "disabled"
            player1_end_turn["state"] = "normal"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'
            start_graph.create_graph()

        elif updated_nodes.turn == 3:
            plt.close(f)

            confirm_road_graph.clearPlotPage()
            updated_nodes.assign_road_value()
            player1_trade["state"] = "disabled"
            player1_use_dev_card["state"] = "disabled"
            player1_build["state"] = "disabled"
            player1_end_turn["state"] = "disabled"
            player1_roll_dice["state"] = "normal"
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'
            start_graph.create_graph()




        elif updated_nodes.turn == 2:
            plt.close(f)

            confirm_road_graph.clearPlotPage()
            updated_nodes.assign_road_value()

            road_counter = 0

            for h in updated_nodes.dict_prop_roads:
                if updated_nodes.dict_prop_roads[h] == 'road_player_2':
                    road_counter += 1

            if road_counter == 1:

                player1_trade["state"] = "disabled"
                player1_use_dev_card["state"] = "disabled"
                player1_build["state"] = "disabled"
                player1_end_turn["state"] = "disabled"
                player1_roll_dice["state"] = "disabled"
                player1_cancel['state'] = 'disabled'
                player1_confirm['state'] = 'disabled'
                player1_cancel['state'] = 'disabled'
                player1_confirm['state'] = 'disabled'
                settlement_graph.create_graph()

            elif road_counter == 2:
                player1_trade["state"] = "disabled"
                player1_use_dev_card["state"] = "disabled"
                player1_build["state"] = "disabled"
                player1_end_turn["state"] = "normal"
                player1_roll_dice["state"] = "disabled"
                player1_cancel['state'] = 'disabled'
                player1_confirm['state'] = 'disabled'
                player1_cancel['state'] = 'disabled'
                player1_confirm['state'] = 'disabled'
                start_graph.create_graph()


        else:
            plt.close(f)

            confirm_road_graph.clearPlotPage()
            updated_nodes.assign_road_value()
            player1_trade["state"] = "normal"
            player1_use_dev_card["state"] = "normal"
            player1_build["state"] = "normal"
            player1_end_turn["state"] = "normal"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'normal'
            player1_confirm['state'] = 'normal'
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'
            start_graph.create_graph()



    elif x == ['confirm_road_2']:

        if updated_nodes.turn % 2 != 0:
            reduce_road_building()

        elif updated_nodes.turn % 2 == 0:
            reduce_road_building_2()

        plt.close(f)

        confirm_road_graph_2.clearPlotPage()
        updated_nodes.assign_road_value()
        player1_trade["state"] = "normal"
        player1_use_dev_card["state"] = "normal"
        player1_build["state"] = "normal"
        player1_end_turn["state"] = "normal"
        player1_roll_dice["state"] = "disabled"
        player1_cancel['state'] = 'normal'
        player1_confirm['state'] = 'normal'
        player1_cancel['state'] = 'disabled'
        player1_confirm['state'] = 'disabled'
        start_graph.create_graph()
        counter_road_building_dev_card = 1



    elif x == ['confirm_road_dev_card']:
        print(counter_road_building_dev_card)
        if counter_road_building_dev_card % 2 != 0:
            print('first')
            plt.close(f)
            confirm_road_graph_dev_card.clearPlotPage()
            updated_nodes.assign_road_value()
            player1_trade["state"] = "normal"
            player1_use_dev_card["state"] = "normal"
            player1_build["state"] = "normal"
            player1_end_turn["state"] = "normal"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'
            start_graph.create_graph()
        else:
            print('second')
            plt.close(f)
            confirm_road_graph_dev_card.clearPlotPage()
            updated_nodes.assign_road_value()
            updated_nodes.assign_road_value()
            player1_trade["state"] = "disabled"
            player1_use_dev_card["state"] = "disabled"
            player1_build["state"] = "disabled"
            player1_end_turn["state"] = "disabled"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'
            road_building_dev_card()

        #
        # if updated_nodes.turn % 2 != 0:
        #     reduce_road_building()
        #     # if updated_nodes.turn % 2 != 0:
        #     #     reduce_road_building()
        #     # elif updated_nodes.turn % 2 == 0:
        #     #     reduce_road_building_2()
        #
        # elif updated_nodes.turn % 2 == 0:
        #     reduce_road_building_2()
        #


    elif x == ['confirm_knight_card']:
        plt.close(f)
        confirm_knight_card_graph.clearPlotPage()
        updated_nodes.assign_robber()
        print(updated_nodes.dict_mid_nodes_for_robber)
        player1_trade["state"] = "normal"
        player1_use_dev_card["state"] = "normal"
        player1_build["state"] = "normal"
        player1_end_turn["state"] = "normal"
        player1_roll_dice["state"] = "disabled"
        player1_cancel['state'] = 'disabled'
        player1_confirm['state'] = 'disabled'

        if updated_nodes.turn % 2 != 0:
            buy_development_card.cards_player_1.knight -= 1
            knight_card_amount.set('Knight Card' + ' (' + str(buy_development_card.cards_player_1.knight) + ')')

            # checking if player eligible for 'the largest army' card:
            Player_1.knight_times_played += 1
            print((Player_1.knight_times_played))
            if Player_1.knight_times_played >= 3 and Player_1.knight_times_played > Player_2.knight_times_played and Player_2.largest_army != True:

                if  Player_1.largest_army != True:
                    Player_1.largest_army = True
                    Player_2.largest_army = False
                    Player_1.score += 2
                    score_player_1.set(str(Player_1.score) + ' Points')

                    if Player_1.score >= 10:
                        messagebox.showinfo('', 'Congratulations! Player 1 wins!')
                        root.quit()
                    elif Player_2.score >= 10:
                        messagebox.showinfo('', 'Congratulations! Player 2 wins!')
                        root.quit()


            elif Player_1.knight_times_played >= 3 and Player_1.knight_times_played > Player_2.knight_times_played and Player_2.largest_army == True:


                if  Player_2.largest_army != True:
                    Player_2.largest_army = True
                    Player_1.largest_army = False
                    Player_1.score += 2
                    score_player_1.set(str(Player_1.score) + ' Points')
                    Player_2.score -= 2
                    score_player_2.set(str(Player_2.score) + ' Points')

                    if Player_1.score >= 10:
                        messagebox.showinfo('', 'Congratulations! Player 1 wins!')
                        root.quit()
                    elif Player_2.score >= 10:
                        messagebox.showinfo('', 'Congratulations! Player 2 wins!')
                        root.quit()




            elif Player_1.knight_times_played >= 3 and Player_1.knight_times_played == Player_2.knight_times_played and Player_2.largest_army == True:

                Player_2.largest_army = False
                Player_2.score -= 2
                score_player_2.set(str(Player_2.score) + ' Points')

                if Player_1.score >= 10:
                    messagebox.showinfo('', 'Congratulations! Player 1 wins!')
                    root.quit()
                elif Player_2.score >= 10:
                    messagebox.showinfo('', 'Congratulations! Player 2 wins!')
                    root.quit()


        elif updated_nodes.turn % 2 == 0:
            buy_development_card.cards_player_2.knight -= 1
            knight_card_amount2.set('Knight Card' + ' (' + str(buy_development_card.cards_player_2.knight) + ')')

            # checking if player eligible for 'the largest army' card:
            Player_2.knight_times_played += 1
            if Player_2.knight_times_played >= 3 and Player_2.knight_times_played > Player_1.knight_times_played and Player_1.largest_army != True:

                Player_2.largest_army = True
                Player_2.score += 2
                score_player_2.set(str(Player_2.score) + ' Points')

                if Player_1.score >= 10:
                    messagebox.showinfo('', 'Congratulations! Player 1 wins!')
                    root.quit()
                elif Player_2.score >= 10:
                    messagebox.showinfo('', 'Congratulations! Player 2 wins!')
                    root.quit()


            elif Player_2.knight_times_played >= 3 and Player_2.knight_times_played > Player_1.knight_times_played and Player_1.largest_army == True:

                Player_2.largest_army = True
                Player_1.largest_army = False
                Player_2.score += 2
                score_player_2.set(str(Player_2.score) + ' Points')
                Player_1.score -= 2
                score_player_1.set(str(Player_1.score) + ' Points')

                if Player_1.score >= 10:
                    messagebox.showinfo('', 'Congratulations! Player 1 wins!')
                    root.quit()
                elif Player_2.score >= 10:
                    messagebox.showinfo('', 'Congratulations! Player 2 wins!')
                    root.quit()



            elif Player_2.knight_times_played >= 3 and Player_2.knight_times_played == Player_1.knight_times_played and Player_1.largest_army == True:

                Player_1.largest_army = False
                Player_1.score -= 2
                score_player_1.set(str(Player_1.score) + ' Points')

                if Player_1.score >= 10:
                    messagebox.showinfo('', 'Congratulations! Player 1 wins!')
                    root.quit()
                elif Player_2.score >= 10:
                    messagebox.showinfo('', 'Congratulations! Player 2 wins!')
                    root.quit()

        start_graph.create_graph()


# cancels the action and goes back to the normal view
def cancel_selection():
    global counter_road_building_dev_card
    if x == ['settlement']:

        plt.close(f)
        settlement_graph.clearPlotPage()
        start_graph.create_graph()
        if updated_nodes.turn == 1 or updated_nodes.turn == 2:

            player1_trade["state"] = "normal"
            player1_use_dev_card["state"] = "normal"
            player1_build["state"] = "normal"
            player1_end_turn["state"] = "normal"
            player1_roll_dice["state"] = "normal"
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'

    elif x == ['merchant']:
        plt.close(f)
        merchant_graph.clearPlotPage()
        player1_trade["state"] = "normal"
        player1_use_dev_card["state"] = "normal"
        player1_build["state"] = "normal"
        player1_end_turn["state"] = "normal"
        player1_roll_dice["state"] = "normal"
        player1_cancel['state'] = 'disabled'
        player1_confirm['state'] = 'disabled'
        start_graph.create_graph()


    elif x == ['confirm_settlement']:
        if updated_nodes.turn == 1 or updated_nodes.turn == 2 or updated_nodes.turn == 3:
            plt.close(f)
            confirm_settlement_graph.clearPlotPage()
            settlement_graph.create_graph()
            player1_trade["state"] = "disabled"
            player1_use_dev_card["state"] = "disabled"
            player1_build["state"] = "disabled"
            player1_end_turn["state"] = "disabled"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'
        else:
            plt.close(f)
            confirm_settlement_graph.clearPlotPage()
            start_graph.create_graph()
            player1_trade["state"] = "normal"
            player1_use_dev_card["state"] = "normal"
            player1_build["state"] = "normal"
            player1_end_turn["state"] = "normal"
            player1_roll_dice["state"] = "normal"
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'

    elif x == ['confirm_city']:
        plt.close(f)
        confirm_city_graph.clearPlotPage()
        start_graph.create_graph()
        player1_trade["state"] = "normal"
        player1_use_dev_card["state"] = "normal"
        player1_build["state"] = "normal"
        player1_end_turn["state"] = "normal"
        player1_roll_dice["state"] = "normal"
        player1_cancel['state'] = 'disabled'
        player1_confirm['state'] = 'disabled'

    elif x == ['road']:
        plt.close(f)
        road_graph.clearPlotPage()
        start_graph.create_graph()
        if counter_road_building_dev_card % 2 == 0:
            counter_road_building_dev_card -= 1
            print(counter_road_building_dev_card)
        player1_trade["state"] = "normal"
        player1_use_dev_card["state"] = "normal"
        player1_build["state"] = "normal"
        player1_end_turn["state"] = "normal"
        player1_roll_dice["state"] = "normal"
        player1_cancel['state'] = 'disabled'
        player1_confirm['state'] = 'disabled'

    elif x == ['confirm_road']:
        plt.close(f)
        confirm_road_graph.clearPlotPage()
        if counter_road_building_dev_card % 2 == 0:
            start_graph.create_graph()
            player1_trade["state"] = "normal"
            player1_use_dev_card["state"] = "normal"
            player1_build["state"] = "normal"
            player1_end_turn["state"] = "normal"
            player1_roll_dice["state"] = "normal"
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'
        if counter_road_building_dev_card % 2 != 0:
            road_graph.create_graph()
            player1_trade["state"] = "disabled"
            player1_use_dev_card["state"] = "disabled"
            player1_build["state"] = "disabled"
            player1_end_turn["state"] = "disabled"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'

    elif x == ['confirm_road_dev_card']:
        plt.close(f)
        confirm_road_graph_dev_card.clearPlotPage()
        start_graph.create_graph()
        counter_road_building_dev_card -= 1
        print(counter_road_building_dev_card)

        player1_trade["state"] = "normal"
        player1_use_dev_card["state"] = "normal"
        player1_build["state"] = "normal"
        player1_end_turn["state"] = "normal"
        player1_roll_dice["state"] = "normal"
        player1_cancel['state'] = 'disabled'
        player1_confirm['state'] = 'disabled'

    elif x == ['city']:
        plt.close(f)
        city_graph.clearPlotPage()
        start_graph.create_graph()
        player1_trade["state"] = "normal"
        player1_use_dev_card["state"] = "normal"
        player1_build["state"] = "normal"
        player1_end_turn["state"] = "normal"
        player1_roll_dice["state"] = "normal"
        player1_cancel['state'] = 'disabled'
        player1_confirm['state'] = 'disabled'
    elif x == ['knight_card']:
        plt.close(f)
        knight_card_graph.clearPlotPage()
        start_graph.create_graph()
        player1_trade["state"] = "normal"
        player1_use_dev_card["state"] = "normal"
        player1_build["state"] = "normal"
        player1_end_turn["state"] = "normal"
        player1_roll_dice["state"] = "normal"
        player1_cancel['state'] = 'disabled'
        player1_confirm['state'] = 'disabled'
    elif x == ['confirm_knight_card']:

        plt.close(f)
        confirm_knight_card_graph.clearPlotPage()
        start_graph.create_graph()


    if updated_nodes.turn == 1 or updated_nodes.turn == 2:

        player1_trade["state"] = "disabled"
        player1_use_dev_card["state"] = "disabled"
        player1_build["state"] = "disabled"
        player1_end_turn["state"] = "disabled"
        player1_roll_dice["state"] = "disabled"
        player1_cancel['state'] = 'disabled'
        player1_confirm['state'] = 'disabled'

    elif updated_nodes.turn == 3:
        roads_turn_3 = 0
        for v in updated_nodes.dict_prop_roads:
            if updated_nodes.dict_prop_roads[v] == 'road_player_1':
                roads_turn_3 += 1
        if roads_turn_3 < 2:
            player1_trade["state"] = "disabled"
            player1_use_dev_card["state"] = "disabled"
            player1_build["state"] = "disabled"
            player1_end_turn["state"] = "disabled"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'

        else:
            player1_trade["state"] = "normal"
            player1_use_dev_card["state"] = "normal"
            player1_build["state"] = "normal"
            player1_end_turn["state"] = "normal"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'disabled'
            player1_confirm['state'] = 'disabled'


    else:

        player1_trade["state"] = "normal"
        player1_use_dev_card["state"] = "normal"
        player1_build["state"] = "normal"
        player1_end_turn["state"] = "normal"
        player1_roll_dice["state"] = "disabled"
        player1_cancel['state'] = 'disabled'
        player1_confirm['state'] = 'disabled'


def build_road():
    player1_build_road.place_forget()
    player1_build_settlement.place_forget()
    player1_build_city.place_forget()
    player1_buy_dev_card.place_forget()

    if updated_nodes.turn % 2 != 0:
        if Player_1.brick > 0 and Player_1.lumber > 0:

            plt.close(f)
            start_graph.clearPlotPage()
            road_graph.create_graph()

            player1_trade["state"] = "disabled"
            player1_use_dev_card["state"] = "disabled"
            player1_build["state"] = "disabled"
            player1_end_turn["state"] = "disabled"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'normal'
            player1_confirm['state'] = 'disabled'

        else:

            messagebox.showinfo("", "Not enough resources to do that!")


    elif updated_nodes.turn % 2 == 0:
        if Player_2.brick > 0 and Player_2.lumber > 0:
            plt.close(f)
            start_graph.clearPlotPage()
            road_graph.create_graph()

            player1_trade["state"] = "disabled"
            player1_use_dev_card["state"] = "disabled"
            player1_build["state"] = "disabled"
            player1_end_turn["state"] = "disabled"
            player1_roll_dice["state"] = "disabled"
            player1_cancel['state'] = 'normal'
            player1_confirm['state'] = 'disabled'


        else:

            messagebox.showinfo("", "Not enough resources to do that!")


#########################################################               defines 'buy dev card' button           ####################################################################


def buy_card():
    player1_build_road.place_forget()
    player1_build_settlement.place_forget()
    player1_build_city.place_forget()
    player1_buy_dev_card.place_forget()

    if updated_nodes.turn % 2 != 0:

        if Player_1.sheep > 0 and Player_1.hay > 0 and Player_1.rock > 0:

            Player_1.sheep -= 1
            Player_1.hay -= 1
            Player_1.rock -= 1

            sheep.set(Player_1.sheep)
            hay.set(Player_1.hay)
            rock.set(Player_1.rock)

            victory_points_before_1 = buy_development_card.cards_player_1.victory_point

            buy_development_card.cards_player_1.pick_card()
            knight_card_amount.set('Knight Card' + ' (' + str(buy_development_card.cards_player_1.knight) + ')')
            year_of_plenty_amount.set(
                'Year of Plenty' + ' (' + str(buy_development_card.cards_player_1.year_of_plenty) + ')')
            road_building_amount.set(
                'Road Building' + ' (' + str(buy_development_card.cards_player_1.road_building) + ')')
            monopoly_amount.set('Monopoly' + ' (' + str(buy_development_card.cards_player_1.monopoly) + ')')

            # updates the score if a victory point card drawn
            if buy_development_card.cards_player_1.victory_point > victory_points_before_1:
                Player_1.score += 1
                score_player_1.set(str(Player_1.score) + ' Points')

                if Player_1.score >= 10:
                    messagebox.showinfo('', 'Congratulations! Player 1 wins!')
                    root.quit()
                elif Player_2.score >= 10:
                    messagebox.showinfo('', 'Congratulations! Player 2 wins!')
                    root.quit()


        else:
            messagebox.showinfo("", "Not enough resources to do that!")

    if updated_nodes.turn % 2 == 0:
        if Player_2.sheep > 0 and Player_2.hay > 0 and Player_2.rock > 0:

            Player_2.sheep -= 1
            Player_2.hay -= 1
            Player_2.rock -= 1

            sheep2.set(Player_2.sheep)
            hay2.set(Player_2.hay)
            rock2.set(Player_2.rock)

            victory_points_before_2 = buy_development_card.cards_player_2.victory_point

            buy_development_card.cards_player_2.pick_card()
            knight_card_amount2.set('Knight Card' + ' (' + str(buy_development_card.cards_player_2.knight) + ')')
            year_of_plenty_amount2.set(
                'Year of Plenty' + ' (' + str(buy_development_card.cards_player_2.year_of_plenty) + ')')
            road_building_amount2.set(
                'Road Building' + ' (' + str(buy_development_card.cards_player_2.road_building) + ')')
            monopoly_amount2.set('Monopoly' + ' (' + str(buy_development_card.cards_player_2.monopoly) + ')')

            if buy_development_card.cards_player_2.victory_point > victory_points_before_2:
                Player_2.score += 1
                score_player_2.set(str(Player_2.score) + ' Points')

                if Player_1.score >= 10:
                    messagebox.showinfo('', 'Congratulations! Player 1 wins!')
                    root.quit()
                elif Player_2.score >= 10:
                    messagebox.showinfo('', 'Congratulations! Player 2 wins!')
                    root.quit()



        else:
            messagebox.showinfo("", "Not enough resources to do that!")


# #########################################################           defines 'end_turn" button                   ######################################################################
#
# def end_turn():
#     updated_nodes.turn += 1
#     #print(updated_nodes.turn)

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
    global roll_counter

    if roll_counter < 2:
        roll_1 = int(random.randint(1, 6))
        roll_2 = int(random.randint(1, 6))

        sum_both_rolls = roll_1 + roll_2

        # gets rid of of half a player's deck if he has more than 7 cards and 7 was rolled
        if sum_both_rolls == 7:
            hand_player_1 = []
            hand_player_2 = []

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

            for i in range(int(Player_2.lumber)):
                hand_player_2.append('lumber')
            for i in range(int(Player_2.sheep)):
                hand_player_2.append('sheep')
            for i in range(int(Player_2.brick)):
                hand_player_2.append('brick')
            for i in range(int(Player_2.rock)):
                hand_player_2.append('rock')
            for i in range(int(Player_2.hay)):
                hand_player_2.append('hay')


            sum_hand_player_1 = len(hand_player_1)
            sum_hand_player_2 = len(hand_player_2)

            half_deck_player_1 = int(0.5 * int(sum_hand_player_1))
            half_deck_player_2 = int(0.5 * int(sum_hand_player_2))

            random.shuffle(hand_player_1)
            random.shuffle(hand_player_2)

            if sum_hand_player_1 > 7:
                if sum_hand_player_1 % 2 == 0:
                    del hand_player_1[0:half_deck_player_1]
                elif sum_hand_player_1 % 2 != 0:
                    del hand_player_1[0:half_deck_player_1+1]

            if sum_hand_player_2 > 7:
                if sum_hand_player_2 % 2 == 0:
                    del hand_player_2[0:half_deck_player_2]
                elif sum_hand_player_2 % 2 != 0:
                    del hand_player_2[0:half_deck_player_2+1]

            Player_1.lumber = Counter(hand_player_1)['lumber']
            Player_1.brick = Counter(hand_player_1)['brick']
            Player_1.sheep = Counter(hand_player_1)['sheep']
            Player_1.rock = Counter(hand_player_1)['rock']
            Player_1.hay = Counter(hand_player_1)['hay']

            Player_2.lumber = Counter(hand_player_2)['lumber']
            Player_2.brick = Counter(hand_player_2)['brick']
            Player_2.sheep = Counter(hand_player_2)['sheep']
            Player_2.rock = Counter(hand_player_2)['rock']
            Player_2.hay = Counter(hand_player_2)['hay']

        # assigns resources to the players based on their settlements / cities and the dice roll
        nodes_rolled = []
        neighbors_middle_node = []

        for key, record in dict_labels.items():
            if dict_labels[key] == sum_both_rolls and updated_nodes.dict_mid_nodes_for_robber[key] != 'robber':
                nodes_rolled.append(key)
                for element in edges_only_middle_nodes:
                    if str(key) in element:
                        neighbors_middle_node.append(element)

        mid_nodes = []
        for edge in edges_only_middle_nodes:
            mid_nodes.append(edge[1])
        mid_nodes = set(mid_nodes)
        mid_nodes = sorted(list(mid_nodes))
        mid_nodes_enumerated = list(enumerate(mid_nodes, 1))

        for element in neighbors_middle_node:
            if updated_nodes.dict_prop[element[0]] == 'settlement_player_1':
                price = element[1]
                for a in mid_nodes_enumerated:
                    if price in a:
                        color_index = a[0]
                        if updated_nodes.dict_hex_colors[color_index] == 'dimgrey':
                            Player_1.rock += 1
                        if updated_nodes.dict_hex_colors[color_index] == 'yellow':
                            Player_1.hay += 1
                        if updated_nodes.dict_hex_colors[color_index] == 'lime':
                            Player_1.sheep += 1
                        if updated_nodes.dict_hex_colors[color_index] == 'red':
                            Player_1.brick += 1
                        if updated_nodes.dict_hex_colors[color_index] == 'forestgreen':
                            Player_1.lumber += 1
            elif updated_nodes.dict_prop[element[0]] == 'city_player_1':
                price = element[1]
                for a in mid_nodes_enumerated:
                    if price in a:
                        color_index = a[0]
                        if updated_nodes.dict_hex_colors[color_index] == 'dimgrey':
                            Player_1.rock += 2
                        if updated_nodes.dict_hex_colors[color_index] == 'yellow':
                            Player_1.hay += 2
                        if updated_nodes.dict_hex_colors[color_index] == 'lime':
                            Player_1.sheep += 2
                        if updated_nodes.dict_hex_colors[color_index] == 'red':
                            Player_1.brick += 2
                        if updated_nodes.dict_hex_colors[color_index] == 'forestgreen':
                            Player_1.lumber += 2

            if updated_nodes.dict_prop[element[0]] == 'settlement_player_2':
                price = element[1]
                for a in mid_nodes_enumerated:
                    if price in a:
                        color_index = a[0]
                        if updated_nodes.dict_hex_colors[color_index] == 'dimgrey':
                            Player_2.rock += 1
                        if updated_nodes.dict_hex_colors[color_index] == 'yellow':
                            Player_2.hay += 1
                        if updated_nodes.dict_hex_colors[color_index] == 'lime':
                            Player_2.sheep += 1
                        if updated_nodes.dict_hex_colors[color_index] == 'red':
                            Player_2.brick += 1
                        if updated_nodes.dict_hex_colors[color_index] == 'forestgreen':
                            Player_2.lumber += 1

            elif updated_nodes.dict_prop[element[0]] == 'city_player_2':
                price = element[1]
                for a in mid_nodes_enumerated:
                    if price in a:
                        color_index = a[0]
                        if updated_nodes.dict_hex_colors[color_index] == 'dimgrey':
                            Player_2.rock += 2
                        if updated_nodes.dict_hex_colors[color_index] == 'yellow':
                            Player_2.hay += 2
                        if updated_nodes.dict_hex_colors[color_index] == 'lime':
                            Player_2.sheep += 2
                        if updated_nodes.dict_hex_colors[color_index] == 'red':
                            Player_2.brick += 2
                        if updated_nodes.dict_hex_colors[color_index] == 'forestgreen':
                            Player_2.lumber += 2

        lumber.set(Player_1.lumber)
        rock.set(Player_1.rock)
        brick.set(Player_1.brick)
        sheep.set(Player_1.sheep)
        hay.set(Player_1.hay)

        lumber2.set(Player_2.lumber)
        rock2.set(Player_2.rock)
        brick2.set(Player_2.brick)
        sheep2.set(Player_2.sheep)
        hay2.set(Player_2.hay)

        # player 1 - displays the result of the first roll
        player1_roll_1 = Label(root, width=3, height=1, bg='white', text=roll_1, font=('Times New Roman', 30))
        player1_roll_1.place(x=25, y=270)

        # player 1 - displays the result of the other roll
        player1_roll_2 = Label(root, width=3, height=1, bg='white', text=roll_2, font=('Times New Roman', 30),
                               state='normal')
        player1_roll_2.place(x=115, y=270)

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
        if updated_nodes.turn % 2 != 0:

            player1_trade_bank.place_forget()
            player1_trade_merchant.place_forget()
            player1_build_road.place_forget()
            player1_build_settlement.place_forget()
            player1_build_city.place_forget()
            player1_buy_dev_card.place_forget()
            player1_knight_card.place(x=270, y=390)
            player1_year_of_plenty_card.place(x=270, y=440)
            player1_road_building_card.place(x=270, y=490)
            player1_monopoly_card.place(x=270, y=540)
            counter_dev_card = True
            counter_trade = False
        else:

            player1_trade_bank.place_forget()
            player1_trade_merchant.place_forget()
            player1_build_road.place_forget()
            player1_build_settlement.place_forget()
            player1_build_city.place_forget()
            player1_buy_dev_card.place_forget()
            player2_knight_card.place(x=270, y=390)
            player2_year_of_plenty_card.place(x=270, y=440)
            player2_road_building_card.place(x=270, y=490)
            player2_monopoly_card.place(x=270, y=540)
            counter_dev_card = True
            counter_trade = False

    elif counter_dev_card == True:
        player1_knight_card.place_forget()
        player1_year_of_plenty_card.place_forget()
        player1_road_building_card.place_forget()
        player1_monopoly_card.place_forget()
        player2_knight_card.place_forget()
        player2_year_of_plenty_card.place_forget()
        player2_road_building_card.place_forget()
        player2_monopoly_card.place_forget()
        counter_dev_card = False

    # function that expand the menu "Trade"


def trade():
    global counter_dev_card
    global counter_trade
    global counter

    if counter_trade == False:
        player2_knight_card.place_forget()
        player2_year_of_plenty_card.place_forget()
        player2_road_building_card.place_forget()
        player2_monopoly_card.place_forget()
        player1_build_road.place_forget()
        player1_build_settlement.place_forget()
        player1_build_city.place_forget()
        player1_buy_dev_card.place_forget()
        player1_knight_card.place_forget()
        player1_year_of_plenty_card.place_forget()
        player1_road_building_card.place_forget()
        player1_monopoly_card.place_forget()
        player1_trade_bank.place(x=270, y=390)
        player1_trade_merchant.place(x=270, y=340)
        counter_trade = True
        counter = False
        counter_dev_card = False

    elif counter_trade == True:
        player2_knight_card.place_forget()
        player2_year_of_plenty_card.place_forget()
        player2_road_building_card.place_forget()
        player2_monopoly_card.place_forget()
        player1_knight_card.place_forget()
        player1_year_of_plenty_card.place_forget()
        player1_road_building_card.place_forget()
        player1_monopoly_card.place_forget()
        player1_trade_bank.place_forget()
        player1_trade_merchant.place_forget()
        counter_trade = False


########################################            function that creates a new window to trade with the bank       #######################################################
def trade_bank():
    # disable all buttons until you close the new window
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

    # puts the new window in the center
    width = root.winfo_x()
    height = root.winfo_y()
    bank_window.geometry("+%d+%d" % (width + 700, height + 400))

    # Make topLevelWindow remain on top until destroyed, or attribute changes.
    bank_window.attributes('-topmost', 1)

    # A Label widget to show in toplevel - this 'dummy' label is made to put two other columns in the middle on the window
    Label(bank_window, text="     ", font=("Times New Roman", 10), padx=10, pady=10).grid(row=0, column=0, columnspan=1)

    # A Label widget to show in toplevel
    Label(bank_window, text="Your 4 cards:", font=("Times New Roman", 10), padx=10, pady=10).grid(row=0, column=2,
                                                                                                  columnspan=1)

    # A Label widget to show in toplevel
    Label(bank_window, text="For bank's 1 card:", font=("Times New Roman", 10), padx=30, pady=10).grid(row=0, column=4,
                                                                                                       columnspan=1)

    # funtion that closes  the "trade bank" new window

    def close_window():
        bank_window.destroy()
        player1_roll_dice['state'] = 'disable'
        player1_trade['state'] = 'normal'
        player1_use_dev_card['state'] = 'normal'
        player1_build['state'] = 'normal'
        player1_end_turn['state'] = 'normal'
        player1_confirm['state'] = 'disable'
        player1_cancel['state'] = 'disable'

        # what happens after the 'confirm' button is clicked

    def confirm_bank():

        if updated_nodes.turn % 2 != 0:
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

        if updated_nodes.turn % 2 == 0:
            if v.get() == 'Brick' and Player_2.brick >= 4:
                if z.get() == 'Brick':
                    Player_2.brick -= 3
                    brick2.set(Player_2.brick)
                elif z.get() == 'Lumber':
                    Player_2.lumber += 1
                    Player_2.brick -= 4
                    brick2.set(Player_2.brick)
                    lumber2.set(Player_2.lumber)
                elif z.get() == 'Sheep':
                    Player_2.sheep += 1
                    Player_2.brick -= 4
                    brick2.set(Player_2.brick)
                    sheep2.set(Player_2.sheep)
                elif z.get() == 'Wheat':
                    Player_2.hay += 1
                    Player_2.brick -= 4
                    brick2.set(Player_2.brick)
                    hay2.set(Player_2.hay)
                elif z.get() == 'Rock':
                    Player_2.rock += 1
                    Player_2.brick -= 4
                    brick2.set(Player_2.brick)
                    rock2.set(Player_2.rock)

                bank_window.destroy()
                player1_roll_dice['state'] = 'disable'
                player1_trade['state'] = 'normal'
                player1_use_dev_card['state'] = 'normal'
                player1_build['state'] = 'normal'
                player1_end_turn['state'] = 'normal'
                player1_confirm['state'] = 'disable'
                player1_cancel['state'] = 'disable'

            elif v.get() == 'Lumber' and Player_2.lumber >= 4:
                if z.get() == 'Lumber':
                    Player_2.lumber -= 3
                    lumber2.set(Player_2.lumber)
                elif z.get() == 'Brick':
                    Player_2.lumber -= 4
                    Player_2.brick += 1
                    brick2.set(Player_2.brick)
                    lumber2.set(Player_2.lumber)
                elif z.get() == 'Sheep':
                    Player_2.sheep += 1
                    Player_2.lumber -= 4
                    lumber2.set(Player_2.lumber)
                    sheep2.set(Player_2.sheep)
                elif z.get() == 'Wheat':
                    Player_2.hay += 1
                    Player_2.lumber -= 4
                    lumber2.set(Player_2.lumber)
                    hay2.set(Player_2.hay)
                elif z.get() == 'Rock':
                    Player_2.rock += 1
                    Player_2.lumber -= 4
                    rock2.set(Player_2.rock)
                    lumber2.set(Player_2.lumber)

                bank_window.destroy()
                player1_roll_dice['state'] = 'disable'
                player1_trade['state'] = 'normal'
                player1_use_dev_card['state'] = 'normal'
                player1_build['state'] = 'normal'
                player1_end_turn['state'] = 'normal'
                player1_confirm['state'] = 'disable'
                player1_cancel['state'] = 'disable'


            elif v.get() == 'Sheep' and Player_2.sheep >= 4:
                if z.get() == 'Sheep':
                    Player_2.sheep -= 3
                    sheep2.set(Player_2.sheep)
                elif z.get() == 'Brick':
                    Player_2.sheep -= 4
                    Player_2.brick += 1
                    sheep2.set(Player_2.sheep)
                    brick2.set(Player_2.brick)
                elif z.get() == 'Lumber':
                    Player_2.sheep -= 4
                    Player_2.lumber += 1
                    sheep2.set(Player_2.sheep)
                    lumber2.set(Player_2.lumber)
                elif z.get() == 'Wheat':
                    Player_2.sheep -= 4
                    Player_2.hay += 1
                    sheep2.set(Player_2.sheep)
                    hay2.set(Player_2.hay)
                elif z.get() == 'Rock':
                    Player_2.sheep -= 4
                    Player_2.rock += 1
                    sheep2.set(Player_2.sheep)
                    rock2.set(Player_2.rock)

                bank_window.destroy()
                player1_roll_dice['state'] = 'disable'
                player1_trade['state'] = 'normal'
                player1_use_dev_card['state'] = 'normal'
                player1_build['state'] = 'normal'
                player1_end_turn['state'] = 'normal'
                player1_confirm['state'] = 'disable'
                player1_cancel['state'] = 'disable'

            elif v.get() == 'Wheat' and Player_2.hay >= 4:
                if z.get() == 'Wheat':
                    Player_2.hay -= 3
                    hay2.set(Player_2.hay)
                elif z.get() == 'Brick':
                    Player_2.hay -= 4
                    Player_2.brick += 1
                    hay2.set(Player_2.hay)
                    brick2.set(Player_2.brick)
                elif z.get() == 'Lumber':
                    Player_2.hay -= 4
                    Player_2.lumber += 1
                    hay2.set(Player_2.hay)
                    lumber2.set(Player_2.lumber)
                elif z.get() == 'Sheep':
                    Player_2.hay -= 4
                    Player_2.sheep += 1
                    sheep2.set(Player_2.sheep)
                    hay2.set(Player_2.hay)
                elif z.get() == 'Rock':
                    Player_2.hay -= 4
                    Player_2.rock += 1
                    hay2.set(Player_2.hay)
                    rock2.set(Player_2.rock)

                bank_window.destroy()
                player1_roll_dice['state'] = 'disable'
                player1_trade['state'] = 'normal'
                player1_use_dev_card['state'] = 'normal'
                player1_build['state'] = 'normal'
                player1_end_turn['state'] = 'normal'
                player1_confirm['state'] = 'disable'
                player1_cancel['state'] = 'disable'


            elif v.get() == 'Rock' and Player_2.rock >= 4:
                if z.get() == 'Rock':
                    Player_2.rock -= 3
                    rock2.set(Player_2.rock)
                elif z.get() == 'Brick':
                    Player_2.rock -= 4
                    Player_2.brick += 1
                    rock2.set(Player_2.rock)
                    brick2.set(Player_2.brick)
                elif z.get() == 'Lumber':
                    Player_2.rock -= 4
                    Player_2.lumber += 1
                    rock2.set(Player_2.rock)
                    lumber2.set(Player_2.lumber)
                elif z.get() == 'Sheep':
                    Player_2.rock -= 4
                    Player_2.sheep += 1
                    sheep2.set(Player_2.sheep)
                    rock2.set(Player_2.rock)
                elif z.get() == 'Wheat':
                    Player_2.rock -= 4
                    Player_2.hay += 1
                    hay2.set(Player_2.hay)
                    rock2.set(Player_2.rock)

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
        y += 1

    b = 1

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    for (text_2, value_2) in values_2.items():
        Radiobutton(bank_window, width=10, text=text_2, variable=z,
                    value=value_2, indicator=0,
                    background="lightskyblue").grid(row=b, column=4, columnspan=2)
        b += 1

    # 'cancel' button inside this window
    cancel_bank = Button(bank_window, width=3, height=1, bg='white', text=chr(10008), fg='red', \
                         font=('Times New Roman', 20), \
                         command=close_window).grid(row=6, column=2, columnspan=1, padx=10, pady=20)

    # 'confirm' button inside this window
    confirm_bank = Button(bank_window, width=3, height=1, bg='white', text=chr(10003), fg='green', \
                          font=('Times New Roman', 20), \
                          command=confirm_bank).grid(row=6, column=4, columnspan=2, padx=10, pady=20)


########################################            function that creates a new window to trade with the merchant       #######################################################
def trade_merchant():
    # disable all buttons until you close the new window
    player1_trade_bank.place_forget()
    player1_trade_merchant.place_forget()
    player1_build["state"] = "disabled"
    player1_trade["state"] = "disabled"
    player1_use_dev_card["state"] = "disabled"
    player1_end_turn["state"] = "disabled"
    player1_cancel["state"] = "normal"
    player1_confirm["state"] = "disabled"

    plt.close(f)

    start_graph.clearPlotPage()
    merchant_graph.create_graph()


################################### #                function that expands the menu "Build"         #########################################
def click_build():
    global counter
    global counter_dev_card
    global counter_trade

    if counter == True:
        player2_knight_card.place_forget()
        player2_year_of_plenty_card.place_forget()
        player2_road_building_card.place_forget()
        player2_monopoly_card.place_forget()
        player1_build_road.place_forget()
        player1_build_settlement.place_forget()
        player1_build_city.place_forget()
        player1_buy_dev_card.place_forget()
        counter = False

    elif counter == False:
        player2_knight_card.place_forget()
        player2_year_of_plenty_card.place_forget()
        player2_road_building_card.place_forget()
        player2_monopoly_card.place_forget()
        player1_trade_bank.place_forget()
        player1_trade_merchant.place_forget()
        player1_knight_card.place_forget()
        player1_year_of_plenty_card.place_forget()
        player1_road_building_card.place_forget()
        player1_monopoly_card.place_forget()
        player1_build_road.place(x=270, y=440)
        player1_build_settlement.place(x=270, y=490)
        player1_build_city.place(x=270, y=540)
        player1_buy_dev_card.place(x=270, y=590)
        counter = True
        counter_dev_card = False
        counter_trade = False


#####################################################         functions to define the development cards buttons        ###########################################


def knight_card():
    if updated_nodes.turn % 2 != 0:
        if buy_development_card.cards_player_1.knight != 0:
            plt.close(f)
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
            player2_knight_card.place_forget()
            player2_monopoly_card.place_forget()
            player2_year_of_plenty_card.place_forget()
            player2_road_building_card.place_forget()

            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'disable'
            player1_use_dev_card['state'] = 'disable'
            player1_build['state'] = 'disable'
            player1_end_turn['state'] = 'disable'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'normal'

        else:
            player1_road_building_card.place_forget()
            player1_monopoly_card.place_forget()
            player1_knight_card.place_forget()
            player1_year_of_plenty_card.place_forget()
            player2_knight_card.place_forget()
            player2_monopoly_card.place_forget()
            player2_year_of_plenty_card.place_forget()
            player2_road_building_card.place_forget()
            messagebox.showinfo("", ('You do not own any cards of this type!'))

    elif updated_nodes.turn % 2 == 0:
        if buy_development_card.cards_player_2.knight != 0:
            plt.close(f)
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
            player2_knight_card.place_forget()
            player2_monopoly_card.place_forget()
            player2_year_of_plenty_card.place_forget()
            player2_road_building_card.place_forget()

            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'disable'
            player1_use_dev_card['state'] = 'disable'
            player1_build['state'] = 'disable'
            player1_end_turn['state'] = 'disable'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'normal'

        else:
            player1_road_building_card.place_forget()
            player1_monopoly_card.place_forget()
            player1_knight_card.place_forget()
            player1_year_of_plenty_card.place_forget()
            player2_knight_card.place_forget()
            player2_monopoly_card.place_forget()
            player2_year_of_plenty_card.place_forget()
            player2_road_building_card.place_forget()
            messagebox.showinfo("", ('You do not own any cards of this type!'))


############################    function that defines what happens after clicking the 'year of plenty' button     ##################################################################
############################    function that defines what happens after clicking the 'year of plenty' button     ##################################################################
def year_of_plenty():
    def reduce_year_of_plenty():
        buy_development_card.cards_player_1.year_of_plenty -= 1
        year_of_plenty_amount.set(
            'Year of Plenty' + ' (' + str(buy_development_card.cards_player_1.year_of_plenty) + ')')

    def reduce_year_of_plenty_2():
        buy_development_card.cards_player_2.year_of_plenty -= 1
        year_of_plenty_amount2.set(
            'Year of Plenty' + ' (' + str(buy_development_card.cards_player_2.year_of_plenty) + ')')

    if updated_nodes.turn % 2 != 0:
        if buy_development_card.cards_player_1.year_of_plenty == 0:

            player1_road_building_card.place_forget()
            player1_monopoly_card.place_forget()
            player1_knight_card.place_forget()
            player1_year_of_plenty_card.place_forget()
            messagebox.showinfo("", ('You do not own any cards of this type!'))

        else:

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

            # what happens when 'X' on the top bar is clicked
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
            Label(year_of_plenty, text="            ", font=("Times New Roman", 10), padx=10, pady=10).grid(row=0,
                                                                                                            column=0,
                                                                                                            columnspan=1)

            # A Label widget to show in toplevel
            Label(year_of_plenty, text="Draw 2 cards from the bank", font=("Times New Roman", 10), padx=10,
                  pady=10).grid(row=0, column=1,
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

                if updated_nodes.turn % 2 != 0:

                    if v.get() == 'Brick':
                        Player_1.brick += 2
                        brick.set(Player_1.brick)
                        year_of_plenty.destroy()
                        player1_roll_dice['state'] = 'disable'
                        player1_trade['state'] = 'normal'
                        player1_use_dev_card['state'] = 'normal'
                        player1_build['state'] = 'normal'
                        player1_end_turn['state'] = 'normal'
                        player1_confirm['state'] = 'disable'
                        player1_cancel['state'] = 'disable'
                        reduce_year_of_plenty()



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
                        reduce_year_of_plenty()


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
                        reduce_year_of_plenty()

                    elif v.get() == 'Sheep':
                        Player_1.sheep += 2
                        sheep.set(Player_1.sheep)
                        year_of_plenty.destroy()
                        player1_roll_dice['state'] = 'disable'
                        player1_trade['state'] = 'normal'
                        player1_use_dev_card['state'] = 'normal'
                        player1_build['state'] = 'normal'
                        player1_end_turn['state'] = 'normal'
                        player1_confirm['state'] = 'disable'
                        player1_cancel['state'] = 'disable'
                        reduce_year_of_plenty()


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
                        reduce_year_of_plenty()



                    else:
                        year_of_plenty.attributes('-topmost', 0)
                        messagebox.showinfo("", "Choose a resource!")
                        year_of_plenty.attributes('-topmost', 1)

                elif updated_nodes.turn % 2 == 0:
                    if v.get() == 'Brick':
                        Player_2.brick += 2
                        brick2.set(Player_2.brick)
                        year_of_plenty.destroy()
                        player1_roll_dice['state'] = 'disable'
                        player1_trade['state'] = 'normal'
                        player1_use_dev_card['state'] = 'normal'
                        player1_build['state'] = 'normal'
                        player1_end_turn['state'] = 'normal'
                        player1_confirm['state'] = 'disable'
                        player1_cancel['state'] = 'disable'
                        reduce_year_of_plenty_2()

                    elif v.get() == 'Lumber':
                        Player_2.lumber += 2
                        lumber2.set(Player_2.lumber)
                        year_of_plenty.destroy()
                        player1_roll_dice['state'] = 'disable'
                        player1_trade['state'] = 'normal'
                        player1_use_dev_card['state'] = 'normal'
                        player1_build['state'] = 'normal'
                        player1_end_turn['state'] = 'normal'
                        player1_confirm['state'] = 'disable'
                        player1_cancel['state'] = 'disable'
                        reduce_year_of_plenty_2()

                    elif v.get() == 'Wheat':
                        Player_2.hay += 2
                        hay2.set(Player_2.hay)
                        year_of_plenty.destroy()
                        player1_roll_dice['state'] = 'disable'
                        player1_trade['state'] = 'normal'
                        player1_use_dev_card['state'] = 'normal'
                        player1_build['state'] = 'normal'
                        player1_end_turn['state'] = 'normal'
                        player1_confirm['state'] = 'disable'
                        player1_cancel['state'] = 'disable'
                        reduce_year_of_plenty_2()


                    elif v.get() == 'Sheep':
                        Player_2.sheep += 2
                        sheep2.set(Player_2.sheep)
                        year_of_plenty.destroy()
                        player1_roll_dice['state'] = 'disable'
                        player1_trade['state'] = 'normal'
                        player1_use_dev_card['state'] = 'normal'
                        player1_build['state'] = 'normal'
                        player1_end_turn['state'] = 'normal'
                        player1_confirm['state'] = 'disable'
                        player1_cancel['state'] = 'disable'
                        reduce_year_of_plenty_2()


                    elif v.get() == 'Rock':
                        Player_2.rock += 2
                        rock2.set(Player_2.rock)
                        year_of_plenty.destroy()
                        player1_roll_dice['state'] = 'disable'
                        player1_trade['state'] = 'normal'
                        player1_use_dev_card['state'] = 'normal'
                        player1_build['state'] = 'normal'
                        player1_end_turn['state'] = 'normal'
                        player1_confirm['state'] = 'disable'
                        player1_cancel['state'] = 'disable'
                        reduce_year_of_plenty_2()



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





    elif updated_nodes.turn % 2 == 0:
        if buy_development_card.cards_player_2.year_of_plenty == 0:

            player2_road_building_card.place_forget()
            player2_monopoly_card.place_forget()
            player2_knight_card.place_forget()
            player2_year_of_plenty_card.place_forget()
            messagebox.showinfo("", ('You do not own any cards of this type!'))

        else:

            player2_knight_card.place_forget()
            player2_year_of_plenty_card.place_forget()
            player1_build_road.place_forget()
            player1_build_settlement.place_forget()
            player1_build_city.place_forget()
            player1_buy_dev_card.place_forget()
            player2_road_building_card.place_forget()
            player2_monopoly_card.place_forget()

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

            # what happens when 'X' on the top bar is clicked
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
            Label(year_of_plenty, text="            ", font=("Times New Roman", 10), padx=10, pady=10).grid(row=0,
                                                                                                            column=0,
                                                                                                            columnspan=1)

            # A Label widget to show in toplevel
            Label(year_of_plenty, text="Draw 2 cards from the bank", font=("Times New Roman", 10), padx=10,
                  pady=10).grid(row=0, column=1,
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

                if updated_nodes.turn % 2 != 0:
                    if v.get() == 'Brick':
                        Player_1.brick += 2
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
                        year_of_plenty.destroy()
                        player1_roll_dice['state'] = 'disable'
                        player1_trade['state'] = 'normal'
                        player1_use_dev_card['state'] = 'normal'
                        player1_build['state'] = 'normal'
                        player1_end_turn['state'] = 'normal'
                        player1_confirm['state'] = 'disable'
                        player1_cancel['state'] = 'disable'
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

                if updated_nodes.turn % 2 == 0:
                    if v.get() == 'Brick':
                        Player_2.brick += 2
                        brick2.set(Player_2.brick)
                        year_of_plenty.destroy()
                        player1_roll_dice['state'] = 'disable'
                        player1_trade['state'] = 'normal'
                        player1_use_dev_card['state'] = 'normal'
                        player1_build['state'] = 'normal'
                        player1_end_turn['state'] = 'normal'
                        player1_confirm['state'] = 'disable'
                        player1_cancel['state'] = 'disable'
                        reduce_year_of_plenty_2()

                    elif v.get() == 'Lumber':
                        Player_2.lumber += 2
                        lumber2.set(Player_2.lumber)
                        year_of_plenty.destroy()
                        player1_roll_dice['state'] = 'disable'
                        player1_trade['state'] = 'normal'
                        player1_use_dev_card['state'] = 'normal'
                        player1_build['state'] = 'normal'
                        player1_end_turn['state'] = 'normal'
                        player1_confirm['state'] = 'disable'
                        player1_cancel['state'] = 'disable'
                        reduce_year_of_plenty_2()

                    elif v.get() == 'Wheat':
                        Player_2.hay += 2
                        hay2.set(Player_2.hay)
                        year_of_plenty.destroy()
                        player1_roll_dice['state'] = 'disable'
                        player1_trade['state'] = 'normal'
                        player1_use_dev_card['state'] = 'normal'
                        player1_build['state'] = 'normal'
                        player1_end_turn['state'] = 'normal'
                        player1_confirm['state'] = 'disable'
                        player1_cancel['state'] = 'disable'
                        reduce_year_of_plenty_2()

                    elif v.get() == 'Sheep':
                        Player_2.sheep += 2
                        sheep2.set(Player_2.sheep)
                        year_of_plenty.destroy()
                        player1_roll_dice['state'] = 'disable'
                        player1_trade['state'] = 'normal'
                        player1_use_dev_card['state'] = 'normal'
                        player1_build['state'] = 'normal'
                        player1_end_turn['state'] = 'normal'
                        player1_confirm['state'] = 'disable'
                        player1_cancel['state'] = 'disable'
                        reduce_year_of_plenty_2()

                    elif v.get() == 'Rock':
                        Player_2.rock += 2
                        rock2.set(Player_2.rock)
                        year_of_plenty.destroy()
                        player1_roll_dice['state'] = 'disable'
                        player1_trade['state'] = 'normal'
                        player1_use_dev_card['state'] = 'normal'
                        player1_build['state'] = 'normal'
                        player1_end_turn['state'] = 'normal'
                        player1_confirm['state'] = 'disable'
                        player1_cancel['state'] = 'disable'
                        reduce_year_of_plenty_2()


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


################################################################        defines the 'road building' development card        ###################################################################
counter_road_building_dev_card = 1


def road_building_dev_card():
    global counter_road_building_dev_card

    if updated_nodes.turn % 2 != 0:

        if buy_development_card.cards_player_1.road_building == 0:
            player1_road_building_card.place_forget()
            player1_monopoly_card.place_forget()
            player1_knight_card.place_forget()
            player1_year_of_plenty_card.place_forget()
            player2_road_building_card.place_forget()
            player2_monopoly_card.place_forget()
            player2_knight_card.place_forget()
            player2_year_of_plenty_card.place_forget()
            messagebox.showinfo("", ('You do not own any cards of this type!'))


        else:

            plt.close(f)

            start_graph.clearPlotPage()
            road_graph.create_graph()

            counter_road_building_dev_card += 1
            print(counter_road_building_dev_card)

            player1_knight_card.place_forget()
            player1_year_of_plenty_card.place_forget()
            player1_road_building_card.place_forget()
            player1_monopoly_card.place_forget()
            player2_road_building_card.place_forget()
            player2_monopoly_card.place_forget()
            player2_knight_card.place_forget()
            player2_year_of_plenty_card.place_forget()

            if counter_road_building_dev_card % 2 != 0:

                player1_roll_dice['state'] = 'disabled'
                player1_trade['state'] = 'disabled'
                player1_use_dev_card['state'] = 'disabled'
                player1_build['state'] = 'disabled'
                player1_end_turn['state'] = 'disabled'
                player1_confirm['state'] = 'disabled'
                player1_cancel['state'] = 'disabled'

            elif counter_road_building_dev_card % 2 == 0:

                player1_roll_dice['state'] = 'disabled'
                player1_trade['state'] = 'disabled'
                player1_use_dev_card['state'] = 'disabled'
                player1_build['state'] = 'disabled'
                player1_end_turn['state'] = 'disabled'
                player1_confirm['state'] = 'disabled'
                player1_cancel['state'] = 'normal'

    elif updated_nodes.turn % 2 == 0:

        if buy_development_card.cards_player_2.road_building == 0:
            player1_road_building_card.place_forget()
            player1_monopoly_card.place_forget()
            player1_knight_card.place_forget()
            player1_year_of_plenty_card.place_forget()
            player2_road_building_card.place_forget()
            player2_monopoly_card.place_forget()
            player2_knight_card.place_forget()
            player2_year_of_plenty_card.place_forget()
            messagebox.showinfo("", ('You do not own any cards of this type!'))


        else:
            plt.close(f)
            start_graph.clearPlotPage()
            road_graph.create_graph()
            counter_road_building_dev_card += 1
            print(counter_road_building_dev_card)

            player1_knight_card.place_forget()
            player1_year_of_plenty_card.place_forget()
            player1_road_building_card.place_forget()
            player1_monopoly_card.place_forget()
            player2_road_building_card.place_forget()
            player2_monopoly_card.place_forget()
            player2_knight_card.place_forget()
            player2_year_of_plenty_card.place_forget()

            if counter_road_building_dev_card % 2 != 0:

                player1_roll_dice['state'] = 'disabled'
                player1_trade['state'] = 'disabled'
                player1_use_dev_card['state'] = 'disabled'
                player1_build['state'] = 'disabled'
                player1_end_turn['state'] = 'disabled'
                player1_confirm['state'] = 'disabled'
                player1_cancel['state'] = 'disabled'

            elif counter_road_building_dev_card % 2 == 0:

                player1_roll_dice['state'] = 'disabled'
                player1_trade['state'] = 'disabled'
                player1_use_dev_card['state'] = 'disabled'
                player1_build['state'] = 'disabled'
                player1_end_turn['state'] = 'disabled'
                player1_confirm['state'] = 'disabled'
                player1_cancel['state'] = 'normal'


#####################################################      function on clicking the "monopoly" development card                    ###########################################
#          needs to have the buttons adjusted (confirm, cancel, radio buttons),
#       after other player is made                                  ###################################################
def monopoly():

    def create_monopoly_window():
            # Toplevel object which will
            # be treated as a new window
        year_of_plenty = Toplevel(root)

        # what happens when 'X' on the top bar is clicked
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
        Label(year_of_plenty, text="         ", font=("Times New Roman", 10), padx=10, pady=10).grid(row=0, column=0,
                                                                                                     columnspan=1)

        # A Label widget to show in toplevel
        Label(year_of_plenty, text="Take all of the selected resource\nfrom the opponent", font=("Times New Roman", 10),
              padx=10, pady=10).grid(row=0, column=1,
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
            if updated_nodes.turn % 2 != 0:
                buy_development_card.cards_player_1.monopoly -= 1
                monopoly_amount.set('Monopoly' + ' (' + str(buy_development_card.cards_player_1.monopoly) + ')')

                if v.get() == 'Brick':

                    monopoly_brick = Player_2.brick
                    Player_1.brick += monopoly_brick
                    Player_2.lumber = 0

                    brick.set(Player_1.brick)
                    brick2.set(Player_2.brick)

                    year_of_plenty.destroy()
                    player1_roll_dice['state'] = 'disable'
                    player1_trade['state'] = 'normal'
                    player1_use_dev_card['state'] = 'normal'
                    player1_build['state'] = 'normal'
                    player1_end_turn['state'] = 'normal'
                    player1_confirm['state'] = 'disable'
                    player1_cancel['state'] = 'disable'

                elif v.get() == 'Lumber':

                    monopoly_lumber = Player_2.lumber
                    Player_1.lumber += monopoly_lumber
                    Player_2.lumber = 0

                    lumber.set(Player_1.lumber)
                    lumber2.set(Player_2.lumber)

                    year_of_plenty.destroy()
                    player1_roll_dice['state'] = 'disable'
                    player1_trade['state'] = 'normal'
                    player1_use_dev_card['state'] = 'normal'
                    player1_build['state'] = 'normal'
                    player1_end_turn['state'] = 'normal'
                    player1_confirm['state'] = 'disable'
                    player1_cancel['state'] = 'disable'

                elif v.get() == 'Wheat':

                    monopoly_hay = Player_2.hay
                    Player_1.hay += monopoly_hay
                    Player_2.hay = 0

                    hay.set(Player_1.hay)
                    hay2.set(Player_2.hay)

                    year_of_plenty.destroy()
                    player1_roll_dice['state'] = 'disable'
                    player1_trade['state'] = 'normal'
                    player1_use_dev_card['state'] = 'normal'
                    player1_build['state'] = 'normal'
                    player1_end_turn['state'] = 'normal'
                    player1_confirm['state'] = 'disable'
                    player1_cancel['state'] = 'disable'

                elif v.get() == 'Sheep':

                    monopoly_sheep = Player_2.sheep
                    Player_1.sheep += monopoly_sheep
                    Player_2.sheep = 0

                    sheep.set(Player_1.sheep)
                    sheep2.set(Player_2.sheep)

                    year_of_plenty.destroy()
                    player1_roll_dice['state'] = 'disable'
                    player1_trade['state'] = 'normal'
                    player1_use_dev_card['state'] = 'normal'
                    player1_build['state'] = 'normal'
                    player1_end_turn['state'] = 'normal'
                    player1_confirm['state'] = 'disable'
                    player1_cancel['state'] = 'disable'

                elif v.get() == 'Rock':

                    monopoly_rock = Player_2.rock
                    Player_1.rock += monopoly_rock
                    Player_2.rock = 0

                    rock.set(Player_1.rock)
                    rock2.set(Player_2.rock)

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

            if updated_nodes.turn % 2 == 0:
                buy_development_card.cards_player_2.monopoly -= 1
                monopoly_amount2.set('Monopoly' + ' (' + str(buy_development_card.cards_player_2.monopoly) + ')')
                if v.get() == 'Brick':

                    monopoly_brick = Player_1.brick
                    Player_2.brick += monopoly_brick
                    Player_1.brick = 0

                    brick.set(Player_1.brick)
                    brick2.set(Player_2.brick)

                    year_of_plenty.destroy()
                    player1_roll_dice['state'] = 'disable'
                    player1_trade['state'] = 'normal'
                    player1_use_dev_card['state'] = 'normal'
                    player1_build['state'] = 'normal'
                    player1_end_turn['state'] = 'normal'
                    player1_confirm['state'] = 'disable'
                    player1_cancel['state'] = 'disable'

                elif v.get() == 'Lumber':

                    monopoly_lumber = Player_1.lumber
                    Player_2.lumber += monopoly_lumber
                    Player_1.lumber = 0

                    lumber.set(Player_1.lumber)
                    lumber2.set(Player_2.lumber)

                    year_of_plenty.destroy()
                    player1_roll_dice['state'] = 'disable'
                    player1_trade['state'] = 'normal'
                    player1_use_dev_card['state'] = 'normal'
                    player1_build['state'] = 'normal'
                    player1_end_turn['state'] = 'normal'
                    player1_confirm['state'] = 'disable'
                    player1_cancel['state'] = 'disable'

                elif v.get() == 'Wheat':

                    monopoly_hay = Player_1.hay
                    Player_2.hay += monopoly_hay
                    Player_1.hay = 0

                    hay.set(Player_1.hay)
                    hay2.set(Player_2.hay)

                    year_of_plenty.destroy()
                    player1_roll_dice['state'] = 'disable'
                    player1_trade['state'] = 'normal'
                    player1_use_dev_card['state'] = 'normal'
                    player1_build['state'] = 'normal'
                    player1_end_turn['state'] = 'normal'
                    player1_confirm['state'] = 'disable'
                    player1_cancel['state'] = 'disable'

                elif v.get() == 'Sheep':

                    monopoly_sheep = Player_1.sheep
                    Player_2.sheep += monopoly_sheep
                    Player_1.sheep = 0

                    sheep.set(Player_1.sheep)
                    sheep2.set(Player_2.sheep)

                    year_of_plenty.destroy()
                    player1_roll_dice['state'] = 'disable'
                    player1_trade['state'] = 'normal'
                    player1_use_dev_card['state'] = 'normal'
                    player1_build['state'] = 'normal'
                    player1_end_turn['state'] = 'normal'
                    player1_confirm['state'] = 'disable'
                    player1_cancel['state'] = 'disable'

                elif v.get() == 'Rock':

                    monopoly_rock = Player_1.rock
                    Player_2.rock += monopoly_rock
                    Player_1.rock = 0

                    rock.set(Player_1.rock)
                    rock2.set(Player_2.rock)

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


    if updated_nodes.turn % 2 != 0:
        if buy_development_card.cards_player_1.monopoly == 0:
            player1_road_building_card.place_forget()

            player1_monopoly_card.place_forget()
            player1_knight_card.place_forget()
            player1_year_of_plenty_card.place_forget()
            messagebox.showinfo("", ('You do not own any cards of this type!'))

        else:
            player1_knight_card.place_forget()
            player1_year_of_plenty_card.place_forget()
            player1_build_road.place_forget()
            player1_build_settlement.place_forget()
            player1_build_city.place_forget()
            player1_buy_dev_card.place_forget()
            player1_road_building_card.place_forget()
            player1_monopoly_card.place_forget()

            player2_knight_card.place_forget()
            player2_year_of_plenty_card.place_forget()
            player2_road_building_card.place_forget()
            player2_monopoly_card.place_forget()

            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'disable'
            player1_use_dev_card['state'] = 'disable'
            player1_build['state'] = 'disable'
            player1_end_turn['state'] = 'disable'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'
            create_monopoly_window()


    elif updated_nodes.turn % 2 == 0:
        if buy_development_card.cards_player_2.monopoly == 0:
            player1_road_building_card.place_forget()
            player1_monopoly_card.place_forget()
            player1_knight_card.place_forget()
            player1_year_of_plenty_card.place_forget()
            player2_road_building_card.place_forget()

            player2_monopoly_card.place_forget()
            player2_knight_card.place_forget()
            player2_year_of_plenty_card.place_forget()
            messagebox.showinfo("", ('You do not own any cards of this type!'))

        else:
            player2_knight_card.place_forget()
            player2_year_of_plenty_card.place_forget()
            player1_build_road.place_forget()
            player1_build_settlement.place_forget()
            player1_build_city.place_forget()
            player1_buy_dev_card.place_forget()
            player2_road_building_card.place_forget()
            player2_monopoly_card.place_forget()

            player2_knight_card.place_forget()
            player2_year_of_plenty_card.place_forget()
            player2_road_building_card.place_forget()
            player2_monopoly_card.place_forget()

            player1_roll_dice['state'] = 'disable'
            player1_trade['state'] = 'disable'
            player1_use_dev_card['state'] = 'disable'
            player1_build['state'] = 'disable'
            player1_end_turn['state'] = 'disable'
            player1_confirm['state'] = 'disable'
            player1_cancel['state'] = 'disable'
            create_monopoly_window()

def end_turn():
    global roll_counter

    player2_knight_card.place_forget()
    player2_year_of_plenty_card.place_forget()
    player2_road_building_card.place_forget()
    player2_monopoly_card.place_forget()

    player1_knight_card.place_forget()
    player1_year_of_plenty_card.place_forget()
    player1_road_building_card.place_forget()
    player1_monopoly_card.place_forget()

    player1_build_road.place_forget()
    player1_build_settlement.place_forget()
    player1_build_city.place_forget()
    player1_buy_dev_card.place_forget()

    player1_trade_bank.place_forget()
    player1_trade_merchant.place_forget()

    counter = False
    counter_dev_card = False

    player1_roll_dice['state'] = 'normal'
    player1_trade['state'] = 'disable'
    player1_use_dev_card['state'] = 'disable'
    player1_build['state'] = 'disable'
    player1_end_turn['state'] = 'disable'
    player1_confirm['state'] = 'disable'
    player1_cancel['state'] = 'disable'

    if updated_nodes.turn % 2 != 0:

        player1_name.place_forget()
        player1_hay_score.place_forget()
        player1_rock_score.place_forget()
        player1_sheep_score.place_forget()
        player1_brick_score.place_forget()
        player1_lumber_score.place_forget()

        player2_name.place(x=70, y=20)
        player2_hay_score.place(x=100, y=127)
        player2_rock_score.place(x=240, y=127)
        player2_sheep_score.place(x=360, y=127)
        player2_brick_score.place(x=100, y=172)
        player2_lumber_score.place(x=240, y=172)

    else:

        player2_name.place_forget()
        player2_hay_score.place_forget()
        player2_rock_score.place_forget()
        player2_sheep_score.place_forget()
        player2_brick_score.place_forget()
        player2_lumber_score.place_forget()

        player1_name.place(x=70, y=20)
        player1_hay_score.place(x=100, y=127)
        player1_rock_score.place(x=240, y=127)
        player1_sheep_score.place(x=360, y=127)
        player1_brick_score.place(x=100, y=172)
        player1_lumber_score.place(x=240, y=172)

    updated_nodes.turn += 1
    roll_counter = 0

    if updated_nodes.turn == 2:
        player1_roll_dice['state'] = 'disable'

        settlement_graph.create_graph()
        messagebox.showinfo('', 'Player 2, it\'s your turn to pick a settlement location. Since you\'re second in line, you will go twice.')

    elif updated_nodes.turn == 3:
        player1_roll_dice['state'] = 'disable'

        settlement_graph.create_graph()
        messagebox.showinfo('', 'Player 1, it\'s your turn again to pick a settlement location.')


#########################################################          prepare the main window              #####################################################


root = Tk()
root.geometry('1350x850')
root.resizable(False, False)  # not resizable in both directions
root.title('Settlers of Catan')
# root.state('zoomed')
root.configure(bg='lightskyblue')

# frame for the board
board_frame = Frame(root, width=1200, height=1000, bg='lightskyblue', highlightbackground=None, borderwidth=0,
                    highlightcolor=None, highlightthickness=0)
# board_frame.grid(column=1, columnspan=3, row=0, rowspan=3, padx=0, pady=13)
board_frame.place(x=290, y=-20)

########################################################            Scoreboard                  ###############################################################################3


score_label = Label(root, width=10, height=2, bg='lightskyblue', text='Total Score:',
                    font=('Times New Roman', 20, 'italic', 'bold'))
score_label.place(x=70, y=640)
#
player_1_score_label = Label(root, width=7, height=2, bg='lightskyblue', text='Player 1:',
                             font=('Times New Roman', 16, 'italic'))
player_1_score_label.place(x=22, y=690)

player_2_score_label = Label(root, width=7, height=2, bg='lightskyblue', text='Player 2:',
                             font=('Times New Roman', 16, 'italic'))
player_2_score_label.place(x=22, y=740)

score_player_1 = StringVar()
score_player_1.set(str(Player_1.score) + ' Points')

# player 1 - score label
player1_score = Label(root, width=10, height=1, bg='lightskyblue', textvariable=score_player_1,
                      font=('Times New Roman', 16, 'italic'))
player1_score.place(x=125, y=700)

score_player_2 = StringVar()
score_player_2.set(str(Player_2.score) + ' Points')

# player 2 - score label
player1_score = Label(root, width=10, height=1, bg='lightskyblue', textvariable=score_player_2,
                      font=('Times New Roman', 16, 'italic'))
player1_score.place(x=125, y=750)



###################################################             Menu Player 1                   #############################################################################


# name of player 1
player1_name = Label(root, width=20, height=2, bg='lightskyblue', text='Player 1\'s Turn',
                     font=('Times New Roman', 20, 'italic', 'bold'))
player1_name.place(x=70, y=20)

# player 1 - resources label
player1_resource = Label(root, width=9, height=2, bg='lightskyblue', text='Resources:',
                         font=('Times New Roman', 16, 'italic'))
player1_resource.place(x=25, y=70)

# player 1 - hay
player1_hay = Label(root, width=5, height=2, bg='lightskyblue', text='Wheat:', font=('Times New Roman', 15, 'italic'))
player1_hay.place(x=25, y=115)

hay = StringVar()
hay.set(Player_1.hay)
# player 1 - displays the current number of hay cards
player1_hay_score = Label(root, width=3, height=1, bg='white', textvariable=hay, font=('Times New Roman', 15, 'italic'))
player1_hay_score.place(x=100, y=127)

# player 1 - rock
player1_rock = Label(root, width=5, height=2, bg='lightskyblue', text='Rock:', font=('Times New Roman', 15, 'italic'))
player1_rock.place(x=160, y=115)

rock = StringVar()
rock.set(Player_1.rock)
# player 1 - displays the current number of rock cards
player1_rock_score = Label(root, width=3, height=1, bg='white', textvariable=rock,
                           font=('Times New Roman', 15, 'italic'))
player1_rock_score.place(x=240, y=127)

# player 1 - sheep
player1_sheep = Label(root, width=5, height=2, bg='lightskyblue', text='Sheep:', font=('Times New Roman', 15, 'italic'))
player1_sheep.place(x=290, y=115)

sheep = StringVar()
sheep.set(Player_1.sheep)

# player 1 - displays the current number of sheep cards
player1_sheep_score = Label(root, width=3, height=1, bg='white', textvariable=sheep,
                            font=('Times New Roman', 15, 'italic'))
player1_sheep_score.place(x=360, y=127)

# player 1 - brick
player1_brick = Label(root, width=5, height=2, bg='lightskyblue', text='Brick:', font=('Times New Roman', 15, 'italic'))
player1_brick.place(x=25, y=160)

brick = StringVar()
brick.set(Player_1.brick)
# player 1 - displays the current number of brick cards
player1_brick_score = Label(root, width=3, height=1, bg='white', textvariable=brick,
                            font=('Times New Roman', 15, 'italic'))
player1_brick_score.place(x=100, y=172)

# player 1 - lumber
player1_lumber = Label(root, width=6, height=2, bg='lightskyblue', text='Lumber:',
                       font=('Times New Roman', 15, 'italic'))
player1_lumber.place(x=160, y=160)

lumber = StringVar()
lumber.set(Player_1.lumber)

# player 1 - displays the current number of lumber cards
player1_lumber_score = Label(root, width=3, height=1, bg='white', textvariable=lumber,
                             font=('Times New Roman', 15, 'italic'))
player1_lumber_score.place(x=240, y=172)

# player 1 - Roll dice button
player1_roll_dice = Button(root, width=20, height=1, bg='white', text='Roll dice',
                           font=('Times New Roman', 15, 'italic'), command=roll_dice, state='normal')
player1_roll_dice.place(x=25, y=220)
# player1_roll_dice.bind('<Button-1>', roll_dice)

# player 1 - 'dummy' (empty) result of the first roll
player1_roll_1_empty = Label(root, width=3, height=1, bg='white', text=' ', font=('Times New Roman', 30))
player1_roll_1_empty.place(x=25, y=270)

# player 1 - displays the result of the other roll
player1_roll_2_empty = Label(root, width=3, height=1, bg='white', text=' ', font=('Times New Roman', 30))
player1_roll_2_empty.place(x=115, y=270)

# player 1 - trade button
player1_trade = Button(root, width=20, height=1, bg='white', text='Trade', font=('Times New Roman', 15, 'italic'),
                       command=trade, state='disable')
player1_trade.place(x=25, y=340)

# trade with merchant button - submenu of "Trade" button!
player1_trade_merchant = Button(root, width=20, height=1, bg='white', text='Merchant',
                                font=('Times New Roman', 15, 'italic'), command=trade_merchant)

# trade with bank button - submenu of "Trade" button!
player1_trade_bank = Button(root, width=20, height=1, bg='white', text='Bank', font=('Times New Roman', 15, 'italic'),
                            command=trade_bank)

# player 1 - use development card button
player1_use_dev_card = Button(root, width=20, height=1, bg='white', text='Play Development Card',
                              font=('Times New Roman', 15, 'italic'), command=dev_card, state='disable')
player1_use_dev_card.place(x=25, y=390)

# player 1 - build button
player1_build = Button(root, width=20, height=1, bg='white', text='Build / Buy', font=('Times New Roman', 15, 'italic'),
                       command=click_build, state='disable')
player1_build.place(x=25, y=440)

# button for building settlement - submenu of "build" button!
player1_build_settlement = Button(root, width=20, height=1, bg='white', text='Settlement',
                                  font=('Times New Roman', 15, 'italic'), command=change_view_settlement)

# build a city button - submenu of "build" button!
player1_build_city = Button(root, width=20, height=1, bg='white', text='Upgrade To a City',
                            font=('Times New Roman', 15, 'italic'), command=change_view_city)

# build a road button - submenu of "build" button!
player1_build_road = Button(root, width=20, height=1, bg='white', text='Road', font=('Times New Roman', 15, 'italic'),
                            command=build_road)

# buy a dev card button - submenu of "build" button!

player1_buy_dev_card = Button(root, width=20, height=1, bg='white', text='Buy a Development Card',
                              font=('Times New Roman', 15, 'italic'), command=buy_card)

# use a knight card button - submenu of "Play dev card" button! - replace the text with StrVar like in resources
knight_card_amount = StringVar()
knight_card_amount.set('Knight Card' + ' (' + str(buy_development_card.cards_player_1.knight) + ')')
player1_knight_card = Button(root, width=20, height=1, bg='white', textvariable=knight_card_amount, \
                             font=('Times New Roman', 15, 'italic'), command=knight_card)

# use a 'year of plenty' card button - submenu of "Play dev card" button!
year_of_plenty_amount = StringVar()
year_of_plenty_amount.set('Year of Plenty' + ' (' + str(buy_development_card.cards_player_1.year_of_plenty) + ')')
player1_year_of_plenty_card = Button(root, width=20, height=1, bg='white', textvariable=year_of_plenty_amount,
                                     font=('Times New Roman', 15, 'italic'), command=year_of_plenty)

# use a 'Road building' card button - submenu of "Play dev card" button!
road_building_amount = StringVar()
road_building_amount.set('Road Building' + ' (' + str(buy_development_card.cards_player_1.road_building) + ')')
player1_road_building_card = Button(root, width=20, height=1, bg='white', textvariable=road_building_amount,
                                    font=('Times New Roman', 15, 'italic'), command=road_building_dev_card)

# use a 'Monopoly' card button - submenu of "Play dev card" button!
monopoly_amount = StringVar()
monopoly_amount.set('Monopoly' + ' (' + str(buy_development_card.cards_player_1.monopoly) + ')')
player1_monopoly_card = Button(root, width=20, height=1, bg='white', textvariable=monopoly_amount,
                               font=('Times New Roman', 15, 'italic'), command=monopoly)

# player 1 - End Turn button
player1_end_turn = Button(root, width=20, height=1, bg='white', text='End Turn', font=('Times New Roman', 15, 'italic'),
                          command=end_turn, state='disable')
player1_end_turn.place(x=25, y=490)

# player 1 - Cancel button
player1_cancel = Button(root, width=3, height=1, bg='white', text=chr(10008), fg='red', font=('Times New Roman', 30), \
                        command=cancel_selection, state='disable')
player1_cancel.place(x=25, y=540)

# player 1 - Confirm button
player1_confirm = Button(root, width=3, height=1, bg='white', text=chr(10003), fg='green', font=('Times New Roman', 30),
                         state='disable', command=confirm_selection)
player1_confirm.place(x=115, y=540)

###################################################             Menu Player 2                   #############################################################################


# name of player 2
player2_name = Label(root, width=20, height=2, bg='lightskyblue', text='Player 2\'s Turn',
                     font=('Times New Roman', 20, 'italic', 'bold'))

hay2 = StringVar()
hay2.set(Player_2.hay)
# player 1 - displays the current number of hay cards
player2_hay_score = Label(root, width=3, height=1, bg='white', textvariable=hay2,
                          font=('Times New Roman', 15, 'italic'))

rock2 = StringVar()
rock2.set(Player_2.rock)
# player 1 - displays the current number of rock cards
player2_rock_score = Label(root, width=3, height=1, bg='white', textvariable=rock2,
                           font=('Times New Roman', 15, 'italic'))

sheep2 = StringVar()
sheep2.set(Player_2.sheep)

# player 1 - displays the current number of sheep cards
player2_sheep_score = Label(root, width=3, height=1, bg='white', textvariable=sheep2,
                            font=('Times New Roman', 15, 'italic'))

brick2 = StringVar()
brick2.set(Player_2.brick)
# player 1 - displays the current number of brick cards
player2_brick_score = Label(root, width=3, height=1, bg='white', textvariable=brick2,
                            font=('Times New Roman', 15, 'italic'))

# player 1 - lumber
lumber2 = StringVar()
lumber2.set(Player_2.lumber)

# player 1 - displays the current number of lumber cards
player2_lumber_score = Label(root, width=3, height=1, bg='white', textvariable=lumber2,
                             font=('Times New Roman', 15, 'italic'))

# player 1 - Roll dice button
player1_roll_dice = Button(root, width=20, height=1, bg='white', text='Roll dice',
                           font=('Times New Roman', 15, 'italic'), command=roll_dice, state='normal')
player1_roll_dice.place(x=25, y=220)
# player1_roll_dice.bind('<Button-1>', roll_dice)

# player 1 - 'dummy' (empty) result of the first roll
player1_roll_1_empty = Label(root, width=3, height=1, bg='white', text=' ', font=('Times New Roman', 30))
player1_roll_1_empty.place(x=25, y=270)

# player 1 - displays the result of the other roll
player1_roll_2_empty = Label(root, width=3, height=1, bg='white', text=' ', font=('Times New Roman', 30))
player1_roll_2_empty.place(x=115, y=270)

# player 1 - trade button
player1_trade = Button(root, width=20, height=1, bg='white', text='Trade', font=('Times New Roman', 15, 'italic'),
                       command=trade, state='disable')
player1_trade.place(x=25, y=340)

# trade with merchant button - submenu of "Trade" button!
player1_trade_merchant = Button(root, width=20, height=1, bg='white', text='Merchant',
                                font=('Times New Roman', 15, 'italic'), command=trade_merchant)

# trade with bank button - submenu of "Trade" button!
player1_trade_bank = Button(root, width=20, height=1, bg='white', text='Bank', font=('Times New Roman', 15, 'italic'),
                            command=trade_bank)

# player 1 - use development card button
player1_use_dev_card = Button(root, width=20, height=1, bg='white', text='Play Development Card',
                              font=('Times New Roman', 15, 'italic'), command=dev_card, state='disable')
player1_use_dev_card.place(x=25, y=390)

# player 1 - build button
player1_build = Button(root, width=20, height=1, bg='white', text='Build / Buy', font=('Times New Roman', 15, 'italic'),
                       command=click_build, state='disable')
player1_build.place(x=25, y=440)

# button for building settlement - submenu of "build" button!
player1_build_settlement = Button(root, width=20, height=1, bg='white', text='Settlement',
                                  font=('Times New Roman', 15, 'italic'), command=change_view_settlement)

# build a city button - submenu of "build" button!
player1_build_city = Button(root, width=20, height=1, bg='white', text='Upgrade To a City',
                            font=('Times New Roman', 15, 'italic'), command=change_view_city)

# build a road button - submenu of "build" button!
player1_build_road = Button(root, width=20, height=1, bg='white', text='Road', font=('Times New Roman', 15, 'italic'),
                            command=build_road)

# buy a dev card button - submenu of "build" button!

player1_buy_dev_card = Button(root, width=20, height=1, bg='white', text='Buy a Development Card',
                              font=('Times New Roman', 15, 'italic'), command=buy_card)

# use a knight card button - submenu of "Play dev card" button! - replace the text with StrVar like in resources
knight_card_amount2 = StringVar()
knight_card_amount2.set('Knight Card' + ' (' + str(buy_development_card.cards_player_2.knight) + ')')
player2_knight_card = Button(root, width=20, height=1, bg='white', textvariable=knight_card_amount2, \
                             font=('Times New Roman', 15, 'italic'), command=knight_card)

# use a 'year of plenty' card button - submenu of "Play dev card" button!
year_of_plenty_amount2 = StringVar()
year_of_plenty_amount2.set('Year of Plenty' + ' (' + str(buy_development_card.cards_player_2.year_of_plenty) + ')')
player2_year_of_plenty_card = Button(root, width=20, height=1, bg='white', textvariable=year_of_plenty_amount2,
                                     font=('Times New Roman', 15, 'italic'), command=year_of_plenty)

# use a 'Road building' card button - submenu of "Play dev card" button!
road_building_amount2 = StringVar()
road_building_amount2.set('Road Building' + ' (' + str(buy_development_card.cards_player_2.road_building) + ')')
player2_road_building_card = Button(root, width=20, height=1, bg='white', textvariable=road_building_amount2,
                                    font=('Times New Roman', 15, 'italic'), command=road_building_dev_card)

# use a 'Monopoly' card button - submenu of "Play dev card" button!
monopoly_amount2 = StringVar()
monopoly_amount2.set('Monopoly' + ' (' + str(buy_development_card.cards_player_2.monopoly) + ')')
player2_monopoly_card = Button(root, width=20, height=1, bg='white', textvariable=monopoly_amount2,
                               font=('Times New Roman', 15, 'italic'), command=monopoly)

# player 1 - End Turn button
player1_end_turn = Button(root, width=20, height=1, bg='white', text='End Turn', font=('Times New Roman', 15, 'italic'),
                          command=end_turn, state='disable')
player1_end_turn.place(x=25, y=490)

# player 1 - Cancel button
player1_cancel = Button(root, width=3, height=1, bg='white', text=chr(10008), fg='red', font=('Times New Roman', 30), \
                        command=cancel_selection, state='disable')
player1_cancel.place(x=25, y=540)

# player 1 - Confirm button
player1_confirm = Button(root, width=3, height=1, bg='white', text=chr(10003), fg='green', font=('Times New Roman', 30),
                         state='disable', command=confirm_selection)
player1_confirm.place(x=115, y=540)

#######################################################################################################################################################################################################################
# creating instances of the Class 'Graph' with different settings in brackets to display different views
start_graph = Graph('normal')
merchant_graph = Graph('merchant')
settlement_graph = Graph('settlement')
city_graph = Graph('city')
confirm_settlement_graph = Graph('confirm_settlement')
confirm_city_graph = Graph('confirm_city')
road_graph = Graph('road')
confirm_road_graph = Graph('confirm_road')
confirm_road_graph_2 = Graph('confirm_road_2')
# draws the board where options to block opponent with knight card are shown
knight_card_graph = Graph('knight_card')
# graph with one node colored red (chosen by player who played the 'knight card')
confirm_knight_card_graph = Graph('confirm_knight_card')
# confirm_knight_card = Graph('confirm_knight_card')

# graph to be displayed after clicking the 'play  the 'road building' development card
confirm_road_graph_dev_card = Graph('confirm_road_dev_card')

# initializing the game by creating the 'start_graph'
start_graph.create_graph()
player1_roll_dice["state"] = "disabled"

if updated_nodes.turn == 1:
    messagebox.showinfo('', 'Welcome to Catan, Settlers.')
    messagebox.showinfo('', 'Player 1, choose the location for your first settlement and then build a road next to it.')
    settlement_graph.create_graph()
    player1_trade["state"] = "disabled"
    player1_use_dev_card["state"] = "disabled"
    player1_build["state"] = "disabled"
    player1_end_turn["state"] = "disabled"
    player1_roll_dice["state"] = "disabled"
    player1_cancel['state'] = 'disabled'
    player1_confirm['state'] = 'disabled'



# list to keep the coordinates when nodes on the graph are clicked
coordinates = []



root.mainloop()