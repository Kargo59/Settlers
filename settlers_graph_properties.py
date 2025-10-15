
#initializes a dictionary that stores information about the nodes (if it's settlement / city)
class Graph_Properties:

    def __init__(self, turn):
        self.turn = turn
        # resources_list = ['wood', 'rock', 'wheat']
        # random.shuffle(resources_list)
        # hexagons_resources = ['A', 'B', 'C']
        #list to be used to create a dictionary with 'settlement' or 'city' or 'None' value for each node
        properties = [y for y in range(1, 60)]
        #should later make a list at the beginning with all the edges that are needed to create a graph in the 'Graph' class and in the dict below
        #list with edges to create a dictionary for roads

        roads = [(1, 2), (1, 6), (2, 3), (3, 4), (3, 15), (4, 5), (4, 18), (5, 6), (5, 7), (6, 10), (7, 8), (7, 20), (8, 9), (8, 11),\
                (9, 10), (9, 14), (11, 12), (11, 22), (12, 13), (12, 25), (13, 14), (15, 16), (16, 17), (16, 26),(17, 18), (17, 29), \
                 (18, 19), (19, 20), (19, 31), (20, 21), (21, 22), (21, 33), (22, 23), (23, 24), (23, 35), (24, 25), (24, 38), (26, 27), \
                 (27, 28), (28, 29), (28, 39), (29, 30), (30, 31), (30, 41), (31, 32), (32, 33),(32, 43), (33, 34), (34, 35), (34, 45),\
                 (35, 36), (36, 37), (36, 47), (37, 38), (39, 40), (40, 41), (40, 48), (41, 42), (42, 43), (42, 50), (43, 44), (44, 45),\
                 (44, 52), (45, 46), (46, 47), (46, 54), (48, 49), (49, 50),(50, 51), (51, 52), (52, 53), (53, 54)]

        mid_nodes_keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
        mid_nodes_values = ['None' for x in range(19)]
        self.dict_mid_nodes_for_robber = dict(zip(mid_nodes_keys, mid_nodes_values))




        self.dict_prop = dict.fromkeys(properties)
        self.dict_prop_roads = dict.fromkeys(roads)
        # self.dict_resources = dict(zip(hexagons_resources, resources_list))

        #creates bogus conditions after first rounds of settling so i can modify the graphs - remove later
        self.dict_prop[1] = 'settlement_player_1'
        self.dict_prop[11] = 'settlement_player_2'
        self.dict_prop_roads[1, 2] = 'road_player_1'
        self.dict_prop_roads[11, 12] = 'road_player_2'

        #creates a dictionary with hexagons as keys and randomly assigned colors as values
        colors_hexagons_keys = [x for x in range(1,20)]
        colors_hexagons_values = ['lime', 'yellow', 'yellow', 'yellow', 'yellow', 'forestgreen', 'dimgrey', 'red', 'red',\
                                  'forestgreen', 'lime', 'lime', 'lime', 'forestgreen', 'forestgreen', 'dimgrey', 'dimgrey', 'red', 'navajowhite']
        random.shuffle(colors_hexagons_values)
        colors_hexagons = dict(zip(colors_hexagons_keys, colors_hexagons_values))
        #print(colors_hexagons)


        #bogus dictionary with colors of the hexes (dependent on the resources associated with them)
        self.dict_hex_colors = colors_hexagons
        #print(self.dict_hex_colors)






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
            #print(updated_nodes.dict_prop)
        if updated_nodes.turn % 2 == 0:
            for r in updated_nodes.dict_prop:
                if r == key_city[0]:  # 'key settlement' is a list created within the Graph.create_graph
                    updated_nodes.dict_prop[r] = 'city_player_2'
            #print(updated_nodes.dict_prop)

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


    def assign_robber(self):
        print(key_knight_card)
        for n in updated_nodes.dict_mid_nodes_for_robber:
            print('\'' +n+'\'')
            # if ('\'' +n+'\'') == key_knight_card[0]:
            if n == str(key_knight_card[0]):
                print('ahahaha')
                updated_nodes.dict_mid_nodes_for_robber[n] = 'robber'
            else:
                print('blabla')
                updated_nodes.dict_mid_nodes_for_robber[n] = 'None'



updated_nodes = Graph_Properties(1)
