import tkinter

from tkinter import messagebox
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from pathlib import Path

import random

#import modules to graph and to display the graph properly in Tkinter
from matplotlib import pyplot as plt
import networkx as nx
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as patches
from matplotlib.backend_bases import MouseButton





#creates a class 'Graph' as a blueprint for all the graphs that will be created
class Graph:

    def __init__(self, option):
        self.option = option

    def create_graph(self):
        global x
        global f
        coordinates = []
        f = plt.figure(figsize=(12, 9.9))
        a = f.add_subplot(1, 1, 1)
        plt.axis('off')

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
        G.add_node('A')

        # bottom row, second from the left tile

        G.add_edge(5, 7)
        G.add_edge(7, 8)
        G.add_edge(8, 9)
        G.add_edge(9, 10)
        G.add_edge(10, 6)
        G.add_node('B')

        # bottom row, second from the left tile

        G.add_edge(8, 11)
        G.add_edge(11, 12)
        G.add_edge(12, 13)
        G.add_edge(13, 14)
        G.add_edge(9, 14)
        G.add_node('C')


        # explicitly set positions
        pos = {
            # bottom row, first from the left
            1: (0, 0), 2: (-0.75, 1), 3: (-0.75, 2), 4: (0, 3), 5: (0.75, 2), 6: (0.75, 1), 'A': (0, 1.5), \
            # bottom row, second from the left
            7: (1.5, 3), 8: (2.25, 2), 9: (2.25, 1), 10: (1.5, 0), 'B': (1.5, 1.5), \
            # bottom row, third from the left
            11: (3, 3), 12: (3.75, 2), 13: (3.75, 1), 14: (3, 0), 'C': (3, 1.5), \

            }


        #list to store the settings to display the right colors of the nodes depending on the situation
        color_map = []

        # options for displaying the graph
        if self.__dict__['option'] == 'normal':
            # specifying different colors for the nodes that have letters assigned to them
            for node in G:
                if type(node) == int:
                    if updated_nodes.dict_prop[node] == 'settlement_player_1':
                        color_map.append('blue')
                    elif updated_nodes.dict_prop[node] == 'settlement_player_2':
                        color_map.append('violet')
                    else:
                        color_map.append('white')
                else:
                    color_map.append('yellow')

            options = {
                "font_size": 36,
                "node_size": 3000,
                #"node_color": "white",
                "edgecolors": "black",
                "linewidths": 5,
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
            x = ['normal']

        #graph drawing options for the case when a settlement is to be built
        if updated_nodes.turn % 2 != 0 or updated_nodes.turn % 2 == 0:
            if self.__dict__['option'] == 'settlement':
                edges_for_graphing = list(G.edges)
                #keys_list_settlement = list(updated_nodes.dict_prop)
                #print(keys_list_settlement)
                #print(edges_for_graphing[0][0])
                # specifying different colors for the nodes that have letters assigned to them
                if updated_nodes.turn != 0:
                    # print(updated_nodes.dict_prop)
                    # print(updated_nodes.dict_prop_roads)
                    # print(G.nodes)
                    # print(G.edges)
                    for node in G:
                        if type(node) == int:
                            if updated_nodes.dict_prop[node] == 'settlement_player_1':
                                #print(node)
                                color_map.append('blue')
                                # print(list(G.neighbors(node)))


                            elif updated_nodes.dict_prop[node] == 'settlement_player_2':
                                color_map.append('violet')

                            else:
                                color_map.append('white')
                        else:
                            color_map.append('yellow')


                    # for node in G:
                    #     if type(node) == int:
                    #         print(tuple(G.neighbors(node)))

                    print(list(enumerate(color_map)))
                    print(updated_nodes.dict_prop)

                    print(updated_nodes.dict_prop)
                    for edge in G.edges:
                        if updated_nodes.dict_prop_roads[edge] == 'road_player_1':
                            print(edge)
                            for element in edge:
                                if updated_nodes.dict_prop[element] != 'settlement_player_1' and updated_nodes.dict_prop[element] != 'city_player_1'\
                                and updated_nodes.dict_prop[element] != 'settlement_player_2' and updated_nodes.dict_prop[element] != 'city_player_2':
                                    neighbors_to_build_settlements = tuple(G.neighbors(element))
                                    print(neighbors_to_build_settlements)

                                    if len(neighbors_to_build_settlements) == 2:
                                        if updated_nodes.dict_prop[neighbors_to_build_settlements[0]] != 'settlement_player_1' and\
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[1]] != 'settlement_player_1':
                                            print(element)
                                            if element < 6:
                                                color_map[element - 1] = ('lightskyblue')
                                            elif element >= 6 and element < 11:
                                                color_map[element] = ('lightskyblue')
                                            else:
                                                color_map[element+1] = ('lightskyblue')
                                    elif len(neighbors_to_build_settlements) == 3:
                                        if updated_nodes.dict_prop[neighbors_to_build_settlements[0]] != 'settlement_player_1' and\
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[1]] != 'settlement_player_1' and \
                                        updated_nodes.dict_prop[neighbors_to_build_settlements[2]] != 'settlement_player_1':
                                            print(element)
                                            if element < 6:
                                                color_map[element-1] = ('lightskyblue')
                                            elif element >= 6 and element < 11:
                                                color_map[element] = ('lightskyblue')
                                            else:
                                                color_map[element+1] = ('lightskyblue')

                            print(list(enumerate(color_map)))

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

                options = {
                    "font_size": 36,
                    "node_size": 3000,
                    #"node_color": "blue",
                    "edgecolors": "black",
                    "linewidths": 5,
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
                options = {
                    "font_size": 36,
                    "node_size": 3000,
                    # "node_color": "blue",
                    "edgecolors": "black",
                    "linewidths": 5,
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
                        if node in updated_nodes.dict_prop:
                            if updated_nodes.dict_prop[node] == 'settlement_player_1':
                                color_map.append('green')
                            elif updated_nodes.dict_prop[node] == 'settlement_player_2':
                                color_map.append('violet')
                            else:
                                color_map.append('white')
                        else:
                            color_map.append('yellow')

                    options = {
                        "font_size": 36,
                        "node_size": 3000,
                        # "node_color": "blue",
                        "edgecolors": "black",
                        "linewidths": 5,
                        "width": 5,
                    }
                    edge_color_map = []
                    for edge in updated_nodes.dict_prop_roads:
                        if updated_nodes.dict_prop_roads[edge] == 'road_player_1':
                            edge_color_map.append('blue')
                        elif updated_nodes.dict_prop_roads[edge] == 'road_player_2':
                            edge_color_map.append('violet')
                        else:
                            edge_color_map.append('black')                    # 'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work

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
                        "font_size": 36,
                        "node_size": 3000,
                        # "node_color": "blue",
                        "edgecolors": "black",
                        "linewidths": 5,
                        "width": 5,
                    }
                    edge_color_map = ['black']
                    # 'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
                    x = ['city']


            elif self.__dict__['option'] == 'confirm_city':
                color_map = color_map_red
                options = {
                    "font_size": 36,
                    "node_size": 3000,
                    # "node_color": "blue",
                    "edgecolors": "black",
                    "linewidths": 5,
                    "width": 5,
                }
                edge_color_map = ['black']
                # 'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
                x = ['confirm_city']


            elif self.__dict__['option'] == 'road':
                for node in G:
                    if type(node) == int:
                        if updated_nodes.dict_prop[node] == 'settlement_player_1':
                            color_map.append('blue')
                        elif updated_nodes.dict_prop[node] == 'settlement_player_2':
                            color_map.append('violet')
                        else:
                            color_map.append('white')
                    else:
                        color_map.append('yellow')

                options = {
                    "font_size": 36,
                    "node_size": 3000,
                    # "node_color": "blue",
                    "edgecolors": "black",
                    "linewidths": 5,
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
                        else:
                            color_map.append('white')
                    else:
                        color_map.append('yellow')

                options = {
                    "font_size": 36,
                    "node_size": 3000,
                    # "node_color": "blue",
                    "edgecolors": "black",
                    "linewidths": 5,
                    "width": 5,
                }

                edge_color_map = edge_color_map_road
                #'x' is a parameter needed for the for the 'cancel selection' function outside of this class to work
                x = ['confirm_road']



        # draws the graph using matplotlib
        nx.draw_networkx(G, pos, edge_color=edge_color_map, node_color=color_map, **options, ax=a)

        # Set margins for the axes so that nodes aren't clipped
        # ax = plt.gca()
        # ax.margins(0.20)
        # plt.axis("off")

        # create matplotlib canvas using figure f / graph `G`  and assign to widget `board frame`
        self.canvas = FigureCanvasTkAgg(f, master=board_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()



        #function to get the coordinates when clicked on the graph
        def on_click(event):
            global color_map_red_old
            global color_map_red
            if event.button is MouseButton.LEFT and self.__dict__['option'] == 'settlement':
                global key_settlement
                x, y = event.x, event.y
                ax = event.inaxes  # the axes instance; is this expression necessary?
                #print('Coordinates: %f %f' % (event.xdata, event.ydata))
                #add a function here later that clears the list 'coordinates' if it is not empty
                coordinates.append(event.xdata)
                coordinates.append(event.ydata)
                self.clearPlotPage()
                # prints the list of nodes - I can use it later to select the node to be colored red - should it be highlighted here?
                #print(list(G.nodes))
                #print(pos)
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
                #print(positions)
                # breaking down the 'position' list of list into two lists: one with first elements of 'positions',
                # the other one with second elements of that list
                for x in positions:
                    positions_first_element.append(x[0])
                for x in positions:
                    positions_second_element.append(x[1])

                #print(positions_first_element)
                #print(positions_second_element)
                #find the nodes (in the dictionary 'pos') that are closest to the elements that were just clicked
                a = (min(positions_first_element, key=lambda x: abs(x - coordinates[0])))
                b = (min(positions_second_element, key=lambda x: abs(x - coordinates[1])))

                coordinates_tuple = (a, b)
                #creates a list needed to update the values for 'settlement' or 'city' within the 'Graph_Properties' class
                key_settlement = [w for w in pos if pos[w] == coordinates_tuple]



                # assigns the value 'red' in the color_map (which is used to color the nodes in the graph)
                # and leaves other values as they were
                color_map_red = ['red' if pos[i] == coordinates_tuple else 'white' if type(i) == int else 'yellow' for i in pos]
                #print(color_map_red)

                # create a list'color map red old' to compare it with the newly created color map red list - if they are not the same,
                # the player hasn't clicked the red node and the program will not allow it
                #will be used later for the case when the player builds a city
                color_map_red_old = color_map_red

                confirm_settlement_graph.create_graph()

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
                # find the nodes (in the dictionary 'pos') that are closest to the elements that were just clicked
                a = (min(positions_first_element, key=lambda x: abs(x - coordinates[0])))
                b = (min(positions_second_element, key=lambda x: abs(x - coordinates[1])))

                coordinates_tuple = (a, b)

                print(pos)
                print(positions)
                print(coordinates_tuple)
                positions_index = positions.index(coordinates_tuple)
                print(positions_index)

                # creates a list needed to update the values for 'settlement' or 'city' within the 'Graph_Properties' class
                key_city = [w for w in pos if pos[w] == coordinates_tuple]

                # assigns the value 'red' in the color_map (which is used to color the nodes in the graph)
                # and leaves other values as they were

                color_map_red = ['red' if pos[i] == coordinates_tuple else 'white' if type(i) == int else 'yellow' for i in pos]
                print(color_map_red_old)
                print(color_map_red)
                if color_map_red_old[positions_index] == 'red':
                    confirm_city_graph.create_graph()
                else:
                    city_graph.create_graph()


















            if event.button is MouseButton.LEFT and self.__dict__['option'] == 'road':
                global edge_color_map_road
                global key_edges
                x, y = event.x, event.y
                ax = event.inaxes  # the axes instance; is this expression necessary?
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
                a = (min(avg_first_element, key=lambda x: abs(x - coordinates[0])))
                b = (min(avg_second_element, key=lambda x: abs(x - coordinates[1])))

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

                index_edges = []

                for index, item in enumerate(final_list):
                    if item == 'True':
                        index_edges.append(index)

                #print(index_edges)

                key_edges = edges[index_edges[0]] # defines a variable used later to update dictionary with 'road' property
                #print(key_edges)



                edge_color_map_road = []

                if len(index_edges) == 0:
                    coord_edges = ['None']
                elif len(index_edges) > 0:
                    coord_edges = edges[index_edges[0]]

                for x in edges:
                    if x == coord_edges:
                        edge_color_map_road.append('red')
                    else:
                        edge_color_map_road.append('black')

                if coord_edges == ['None']:
                    edge_color_map_road = ['black']

                # in case a player clicked somewhere outside of graph - later make a pop up message saying 'didn't catch it, try again'
                #print(edge_color_map_road)



                confirm_road_graph.create_graph()

                # nx.draw_networkx(G, pos, node_color=color_map_red, **options, ax=a)
                #
                # self.canvas = FigureCanvasTkAgg(f, master=board_frame)
                # self.canvas.draw()
                # self.canvas.get_tk_widget().pack()



        #connect 'button press event' with on_click function, can later be disconnected with:
        #plt.disconnect(cid)
        cid = plt.connect('button_press_event', on_click)


    #clear the canvas to prepare for the next version of the graph
    def clearPlotPage(self):
        self.canvas.get_tk_widget().pack_forget()

    # cancels the action and goes back to the normal view
    def cancel_selection(self):
        self.clearPlotPage()
        start_graph.create_graph()


#initializes a dictionary that stores information about the nodes (if it's settlement / city)
class Graph_Properties:

    def __init__(self, turn):
        self.turn = turn
        resources_list = ['wood', 'rock', 'wheat']
        random.shuffle(resources_list)
        hexagons_resources = ['A', 'B', 'C']
        #list to be used to create a dictionary with 'settlement' or 'city' or 'None' value for each node
        properties = [y for y in range(1, 15)]
        #should later make a list at the beginning with all the edges that are needed to create a graph in the 'Graph' class and in the dict below
        #list with edges to reate a dictionary for roads
        roads = [(1, 2), (1, 6), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 10), (7, 8), (8, 9), (8, 11), (9, 10), (9, 14), (11, 12), (12, 13), (13, 14)]
        self.dict_prop = dict.fromkeys(properties)
        self.dict_prop_roads = dict.fromkeys(roads)
        self.dict_resources = dict(zip(hexagons_resources, resources_list))

        #creates bogus conditions after first rounds of settling so i can modify the graphs - remove later
        self.dict_prop[1] = 'settlement_player_1'
        self.dict_prop[11] = 'settlement_player_2'
        self.dict_prop_roads[1, 2] = 'road_player_1'
        self.dict_prop_roads[11, 12] = 'road_player_2'





    #prepares a dictionary to store information about the type of resource associated with a node -
    #probably move up outside of this function
    # def assign_resources_to_hexagons(self):
    #     random.shuffle(resources_list)
    #     list_for_resources_all = ['A', 'B', 'C']
    #     list_for_resources_selected = [x for x in list_for_resources_all if isinstance(x, str)]
    #     dict_resources = dict(zip(list_for_resources_selected, resources_list))
    #     print(dict_resources)



    #assigns a 'settlement' value to a node specified by a click within the 'Graph.onclick(confirm settlement)' function
    def assign_settlement_value(self):
        if updated_nodes.turn % 2 != 0:
            for r in updated_nodes.dict_prop:
                if r == key_settlement[0]:  # 'key settlement' is a list created within the Graph.create_graph
                    updated_nodes.dict_prop[r] = 'settlement_player_1'
            #print(updated_nodes.dict_prop)
        if updated_nodes.turn % 2 == 0:
            for r in updated_nodes.dict_prop:
                if r == key_settlement[0]:                                      #'key settlement' is a list created within the Graph.create_graph
                    updated_nodes.dict_prop[r] = 'settlement_player_2'
            #print(updated_nodes.dict_prop)


    #assigns a 'city' value to a node specified by a click within the 'Graph.onclick(confirm city)' function
    def assign_city_value(self):
        if updated_nodes.turn % 2 != 0:
            for r in updated_nodes.dict_prop:
                if r == key_city[0]:                                      #'key settlement' is a list created within the Graph.create_graph
                    updated_nodes.dict_prop[r] = 'city_player_1'
            print(updated_nodes.dict_prop)
        if updated_nodes.turn % 2 == 0:
            for r in updated_nodes.dict_prop:
                if r == key_city[0]:  # 'key settlement' is a list created within the Graph.create_graph
                    updated_nodes.dict_prop[r] = 'city_player_2'
            print(updated_nodes.dict_prop)

    #assigns a 'road' value to an edge specified by a click within the 'Graph.onclick(confirm road)' function
    def assign_road_value(self):
        if updated_nodes.turn % 2 != 0:
            for n in updated_nodes.dict_prop_roads:
                if n == key_edges:                                      #'key settlement' is a list created within the Graph.create_graph
                    updated_nodes.dict_prop_roads[n] = 'road_player_1'
        if updated_nodes.turn % 2 == 0:
            for n in updated_nodes.dict_prop_roads:
                if n == key_edges:  # 'key settlement' is a list created within the Graph.create_graph
                    updated_nodes.dict_prop_roads[n] = 'road_player_2'


updated_nodes = Graph_Properties(1)




#create a 'player' class (maybe store score, resources and so on in it later?)
class Player:
    def __init__(self, score):
        self.score = score

Player_1 = Player(0)
Player_2 = Player(0)



#create the class 'Build' for blueprints of settlements, cities
# and roads, and the functions associated with them
class Build(Player):
    def __init__(self, type):
        self.type = type






#Clears the canvas and plots a new graph - in order for it to work normally 'start_graph' has to be changed
#to something more general
def change_view_settlement():
    start_graph.clearPlotPage()
    settlement_graph.create_graph()

def change_view_city():
    start_graph.clearPlotPage()
    city_graph.create_graph()

#confirms selection based on the type of action performed. Later to also update the player's score, resources etc.
def confirm_selection():
    if x == ['settlement']:
        #dict_properties.update({1:'settlement'})
        settlement_graph.clearPlotPage()
        start_graph.create_graph()
    elif x == ['confirm_settlement']:
        confirm_settlement_graph.clearPlotPage()
        updated_nodes.assign_settlement_value()
        # print(updated_nodes.dict_prop)
        # for r in updated_nodes.dict_prop:
        #     if r == key_settlement:
        #         print(updated_nodes[r].dict_prop)
        #updated_nodes.dict_prop.update({1:'settlement'})
        print(updated_nodes.dict_prop)
        Player_2.score += 1
        #print(Player_2.score)
        start_graph.create_graph()
    elif x == ['confirm_city']:
        confirm_city_graph.clearPlotPage()
        updated_nodes.assign_city_value()
        # print(updated_nodes.dict_prop)
        # for r in updated_nodes.dict_prop:
        #     if r == key_settlement:
        #         print(updated_nodes[r].dict_prop)
        # updated_nodes.dict_prop.update({1:'settlement'})
        # print(updated_nodes.dict_prop)
        Player_2.score += 1
        print(Player_2.score)
        start_graph.create_graph()
    elif x == ['road']:
        road_graph.clearPlotPage()
        start_graph.create_graph()
    elif x == ['confirm_road']:
        confirm_road_graph.clearPlotPage()
        updated_nodes.assign_road_value()
        start_graph.create_graph()

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


def build_road():
    start_graph.clearPlotPage()
    road_graph.create_graph()


def end_turn():
    updated_nodes.turn += 1
    print(updated_nodes.turn)


#prepare the main window
root = Tk()
root.geometry('500x400')
root.title('Settlers of Catan')
root.state('zoomed')


#frame for the board
board_frame = Frame(root, width=1200, height=1000, highlightbackground='black', borderwidth=1, highlightcolor='black', highlightthickness=2)
board_frame.grid(column=0, row=0, rowspan=4, padx=10, pady=13)



#frame for player 1
player1_frame = Frame(root, width=650, height=485, highlightbackground='black', borderwidth=1, highlightcolor='black', highlightthickness=2)
player1_frame.grid(column=1, row=0, padx=10, pady=10)

#name of player 1
player1_name = Label(player1_frame, width = 70, bg='white', text='Player 1 name')
player1_name.grid(row=0, column=0, padx=10, pady=10)

#Player's 1 resources
player1_resources = Label(player1_frame, width=70, bg='white', text='Resources')
player1_resources.grid(row=1, column=0, padx=10, pady=10)

#Player's 1 Development Cards
player1_devcards = Label(player1_frame, width=70, bg='white', text='Development Cards')
player1_devcards.grid(row=2, column=0, padx=10, pady=10)

#Player's 1 Actions - change to a separate frame later!
player1_actions = Label(player1_frame, width=70, bg='white', text='Actions this turn')
player1_actions.grid(row=3, column=0, padx=10, pady=10)

#Player's 2 'Confirm Action' Button
player1_confirm_button = Button(player1_frame, width=70, bg='white', text='Confirm Action')
player1_confirm_button.grid(row=5, column=0, padx=10, pady=10)

#Player's 2 'Cancel Action' Button
player1_confirm_button = Button(player1_frame, width=70, bg='white', text='Cancel Action')
player1_confirm_button.grid(row=6, column=0, padx=10, pady=10)





#frame for player 2
player2_frame = Frame(root, width=650, height=585, highlightbackground='black', borderwidth=1, highlightcolor='black', highlightthickness=2)
player2_frame.grid(column=1, row=1, padx=10, pady=10)

#name of player 2
player2_name = Label(player2_frame, width = 70, bg='white', text='Player 2 name')
player2_name.grid(row=0, column=0, padx=10, pady=10)

#Player's 2 resources
player2_resources = Label(player2_frame, width=70, bg='white', text='Resources')
player2_resources.grid(row=1, column=0, padx=10, pady=10)

#Player's 2 Development Cards
player2_devcards = Label(player2_frame, width=70, bg='white', text='Development Cards')
player2_devcards.grid(row=2, column=0, padx=10, pady=10)

#Player's 2 Actions - change to a separate frame later!
player2_actions = Label(player2_frame, width=70, bg='white', text='Actions this turn')
player2_actions.grid(row=3, column=0, padx=10, pady=10)

#Player's 2 Button 'Build a settlement'
player2_build_settlement = Button(player2_frame, width=70, bg='white', text='Build settlement', command=change_view_settlement)
player2_build_settlement.grid(row=4, column=0, padx=10, pady=10)

#Player's 2 Button 'Upgrade to a city'
player2_build_settlement = Button(player2_frame, width=70, bg='white', text='Upgrade to a city', command=change_view_city)
player2_build_settlement.grid(row=5, column=0, padx=10, pady=10)

#Player's 2 Button 'Build a a Road'
player2_build_settlement = Button(player2_frame, width=70, bg='white', text='Build a road', command=build_road)
player2_build_settlement.grid(row=6, column=0, padx=10, pady=10)

#Player's 2 'Confirm Action' Button
player2_confirm_button = Button(player2_frame, width=70, bg='white', text='Confirm Action', command=confirm_selection)
player2_confirm_button.grid(row=7, column=0, padx=10, pady=10)

#Player's 2 'Cancel Action' Button
player2_confirm_button = Button(player2_frame, width=70, bg='white', text='Cancel Action', command=cancel_selection)
player2_confirm_button.grid(row=8, column=0, padx=10, pady=10)

#Player's 2 'End Turn' Button
player2_end_turn = Button(player2_frame, width=70, bg='white', text='End Turn', command=end_turn)
player2_end_turn.grid(row=9, column=0, padx=10, pady=10)

#creating instances of the Class 'Graph' with different settings in brackets to display different views
start_graph = Graph('normal')
settlement_graph = Graph('settlement')
city_graph = Graph('city')
confirm_settlement_graph = Graph('confirm_settlement')
confirm_city_graph = Graph('confirm_city')
road_graph = Graph('road')
confirm_road_graph = Graph('confirm_road')



#initializing the game by creating the 'start_graph'
start_graph.create_graph()

#list to keep the coordinates when nodes on the graph are clicked
coordinates = []


root.mainloop()