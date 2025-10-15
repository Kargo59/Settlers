import tkinter

from tkinter import messagebox
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from pathlib import Path

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
        global f
        coordinates = []
        f = plt.figure(figsize=(12, 9.9))
        a = f.add_subplot(1, 1, 1)
        plt.axis('off')

        G = nx.Graph()

        #first idea on how to change the node color based on the inner function 'onclick(event)
        if len(coordinates) == 0:
            G.add_edge(1,3)


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

        # options for displaying the graph
        if self.__dict__['option'] == 'normal':

            # specifying different colors for the nodes that have letters assigned to them
            color_map = []
            for node in G:
                if type(node) == int:
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

        #graph drawing options for the case when a settlement is to be built
        elif self.__dict__['option'] == 'settlement':

            # specifying different colors for the nodes that have letters assigned to them
            color_map = []
            for node in G:
                if type(node) == int:
                    color_map.append('blue')
                else:
                    color_map.append('yellow')

            options = {
                "font_size": 36,
                "node_size": 3000,
                #"node_color": "blue",
                "edgecolors": "black",
                "linewidths": 5,
                "width": 5,
            }

        # draws the graph using matplotlib
        nx.draw_networkx(G, pos, node_color=color_map, **options, ax=a)

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
            if event.button is MouseButton.LEFT and self.__dict__['option'] == 'settlement':
                x, y = event.x, event.y
                ax = event.inaxes  # the axes instance; is this expression necessary?
                print('Coordinates: %f %f' % (event.xdata, event.ydata))
                #add a function here later that clears the list 'coordinates' if it is not empty
                coordinates.append(event.xdata)
                coordinates.append(event.ydata)
                print(coordinates)
                self.clearPlotPage()
                # prints the list of nodes - I can use it later to select the node to be colored red - should it be highlighted here?
                print(list(G.nodes))
                print(pos)
                # highlights the node that was clicked by the player
                coordinates_tuple = tuple(coordinates)
                print(coordinates_tuple)
                print(pos.values())
                # finding the dictionary 'pos' values that are closest to the coordinates clicked by the player
                positions = []
                positions_first_element = []
                positions_second_element = []
                for value in iter(pos.values()):
                    positions.append(value)
                print(positions)
                # breaking down the 'position' list of list into two lists: one with first elements of 'positions',
                # the other one with second elements of that list
                for x in positions:
                    positions_first_element.append(x[0])
                for x in positions:
                    positions_second_element.append(x[1])

                print(positions_first_element)
                print(positions_second_element)
                #find the nodes (in the dictionary 'pos' that are closest to the elements that were just clicked
                a = (min(positions_first_element, key=lambda x: abs(x - coordinates[0])))
                b = (min(positions_second_element, key=lambda x: abs(x - coordinates[1])))

                coordinates_tuple = (a, b)
                print(coordinates_tuple)

                # assigns the value 'red' in the color_map (which is used to color the nodes in the graph
                # and leaves other values as they were
                # color_map = ['red' if pos[i] == coordinates_tuple else 'blue' if type(i) == int else 'yellow' for i in pos]
                # print(color_map)


                nx.draw_networkx(G, pos, node_color=color_map, **options, ax=a)

                self.canvas = FigureCanvasTkAgg(f, master=board_frame)
                self.canvas.draw()
                self.canvas.get_tk_widget().pack()



        #connect 'button press event' with on_click function, can later be disconnected with:
        #plt.disconnect(cid)
        cid = plt.connect('button_press_event', on_click)


    #clear the canvas to prepare for the next version of the graph
    def clearPlotPage(self):
        self.canvas.get_tk_widget().pack_forget()




#create a 'player' class (maybe store score, resources and so on in it later?)
class Player:
    def __init__(self, player_name):
        self.player_name = player_name



#create the class 'Build' for blueprints of settlements, cities
# and roads, and the functions associated with them
class Build(Player):
    def __init__(self, type):
        self.type = type


#defines what happens when we want to build a settlement: highlights the available spots
#and let's us build on them, changing the chosen node's properties
    def create_settlement(self):
        options = {
            "font_size": 36,
            "node_size": 3000,
            "node_color": "blue",
            "edgecolors": "black",
            "linewidths": 5,
            "width": 5,
        }





#Clears the canvas and plots a new graph - in order for it to work normally 'start_graph' has to be changed
#to something more general
def change_view_settlement():
    start_graph.clearPlotPage()
    settlement_graph.create_graph()



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
player1_actions.grid(row=3, column=0, rowspan=5, padx=10, pady=10)


#frame for player 2
player2_frame = Frame(root, width=650, height=485, highlightbackground='black', borderwidth=1, highlightcolor='black', highlightthickness=2)
player2_frame.grid(column=1, row=1, padx=10, pady=10)

#name of player 2
player2_name = Label(player2_frame, width = 70, bg='white', text='Player 2 name')
player2_name.grid(row=0, column=0, padx=10, pady=10)

#Player's 1 resources
player2_resources = Label(player2_frame, width=70, bg='white', text='Resources')
player2_resources.grid(row=1, column=0, padx=10, pady=10)

#Player's 1 Development Cards
player2_devcards = Label(player2_frame, width=70, bg='white', text='Development Cards')
player2_devcards.grid(row=2, column=0, padx=10, pady=10)

#Player's 1 Actions - change to a separate frame later!
player2_actions = Label(player2_frame, width=70, bg='white', text='Actions this turn')
player2_actions.grid(row=3, column=0, rowspan=5, padx=10, pady=10)

#Player's 2 Button Action - building a settlement
player2_build_settlement = Button(player2_frame, width=70, bg='white', text='Build settlement', command=change_view_settlement)
player2_build_settlement.grid(row=3, column=0, rowspan=5, padx=10, pady=10)

#creating instances of the Class 'Graph' with different settings in brackets to display different views
start_graph = Graph('normal')
settlement_graph = Graph('settlement')
confirm_settlement = Graph('confirm settlement')

#initializing the game by creating the 'start_graph'
start_graph.create_graph()

#list to keep the coordinates when nodes on the graph are clicked
coordinates = []


root.mainloop()