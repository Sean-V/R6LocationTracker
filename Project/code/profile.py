#This file contains the profile class which will be used to keep track of player data.

from maps import coastline, border, kafedostoyevsky, clubhouse, villa, consulate, bank
import os
import pickle
import matplotlib.pyplot as plt
import networkx as nx
import sys
from utils import get_map

class Player():
    def __init__(self):
        #Ask for player's in game name to either load or create a profile
        self.alias = input('Enter your in game name for Rainbow Six Siege:\n')
        #Check if player file exists already
        if os.path.exists(f'profiles/{self.alias}.pickle'):
            player_file = open(f'profiles/{self.alias}.pickle', 'rb')
            self.player_data = pickle.load(player_file)
            #Player's resolution as given by tuple
            self.resolution = self.player_data['resolution']
            #Player's aspect ratio
            self.aspect_ratio = self.player_data['aspect_ratio']
            player_file.close()
        #Create a new user
        else:
            #Acquire player parameters through user input
            resolution = input('What is your resolution? (Compatibile resolutions include anything with the same ratio as 1920x1080)\n')
            if resolution not in ['1920x1080', '2560x1440']:
                print('Incompatibile resolution found!')
                sys.exit(0)
            aspect_ratio = input('What is your aspect ratio? (Compatibile aspect ratios include 3:2, 4:3, 5:4, 16:9, and 16:10)\n')
            if aspect_ratio not in ['3:2', '4:3', '5:4', '16:9', '16:10']:
                print('Incompatibile aspect ratio found!')
                sys.exit(0)
            #Player's resolution as given by tuple
            self.resolution = [int(element) for element in resolution.split('x')]
            #Player's aspect ratio
            self.aspect_ratio = [int(element) for element in aspect_ratio.split(':')]
            #Store new user
            self.player_data = {
                'resolution':self.resolution,
                'aspect_ratio':self.aspect_ratio,
                'COASTLINE':{'ATK':coastline.copy(), 'DEF':coastline.copy()},
                'BORDER':{'ATK':border.copy(), 'DEF':border.copy()},
                'KAFEDOSTOYEVSKY':{'ATK':kafedostoyevsky.copy(), 'DEF':kafedostoyevsky.copy()},
                'CLUBHOUSE':{'ATK':clubhouse.copy(), 'DEF':clubhouse.copy()},
                'VILLA':{'ATK':villa.copy(), 'DEF':villa.copy()},
                'CONSULATE':{'ATK':consulate.copy(), 'DEF':consulate.copy()},
                'BANK':{'ATK':bank.copy(), 'DEF':bank.copy()}
            }
            if not os.path.exists('profiles'):
                os.makedirs('profiles')
            player_file = open(f'profiles/{self.alias}.pickle', 'wb+')
            pickle.dump(self.player_data, player_file)
            player_file.close()

    #Define a function to store player data in a Player object
    #input: player object and data
    #output: appends new data to player's existing data
    def store_data(self):
        player_file = open(f'profiles/{self.alias}.pickle', 'wb+')
        pickle.dump(self.player_data, player_file)
        player_file.close()

    #Define a funtion that updates player data
    #input: path traveled variable to parse for location transitions
    #output: updates self.player_data with added map data
    def update_data(self, path_traveled, map_string, affiliation):
        #For now, we are going to update the weights between edges and specific nodes. Nodes will represent if a player was at a certain location while edges will represent movement between two locations.
        ## TODO: IDEA: Update each weight based on time factor in order to get a better idea of what areas players spend most of their time.
        for index in range(len(path_traveled)):
            #Update node_visited
            self.player_data[map_string][affiliation].nodes[path_traveled[index]]['node_visited'] += 1
            #Update edge_visited
            if index != len(path_traveled) - 1:
                #Use try except in order to skip location changes that are not valid.
                try:
                    self.player_data[map_string][affiliation][path_traveled[index]][path_traveled[index+1]]['edge_visited'] += 1
                except:
                    ## TODO: ACCURACY: Have some sort of correction or disregard method that is more extensive than what is currently in place.
                    pass

    #Define a function that outputs a visualization of the data.
    #input: map_string
    #output: visual of data
    def visualize_data(self, map_string, affiliation):
        #Define the map based on map_string
        map = self.player_data[map_string][affiliation]
        #Define colormap to store the colors of the nodes
        node_color_map = []
        #Calculate the mean value of the node_visited attribute
        mean_node_visited = sum([node[1]['node_visited'] for node in map.nodes(data=True)])//len(map.nodes())
        #Color nodes based on the mean plus/minus half the mean
        for node in map.nodes(data=True):
            if node[1]['node_visited'] <= mean_node_visited - (mean_node_visited//2):
                #Blue is lightly traveled
                node_color_map.append('blue')
            elif node[1]['node_visited'] <= mean_node_visited + (mean_node_visited//2):
                #Yellow is average traveled
                node_color_map.append('yellow')
            else:
                #Red is heavily traveled
                node_color_map.append('red')
        #Define colormap to store the colors of the edges
        edge_color_map = []
        #Calculate the mean value of the edge_visited attribute
        mean_edge_visited = sum([edge[-1]['edge_visited'] for edge in map.edges(data=True)])//len(map.edges())
        #Color edges based on the mean plus/minus half the mean
        for edge in map.edges(data=True):
            if edge[-1]['edge_visited'] <= mean_edge_visited - (mean_edge_visited//2):
                #Blue is lightly traveled
                edge_color_map.append('blue')
            elif edge[-1]['edge_visited'] <= mean_edge_visited + (mean_edge_visited//2):
                #Yellow is average traveled
                edge_color_map.append('yellow')
            else:
                #Red is heavily traveled
                edge_color_map.append('red')
        #Graph the map with the colored nodes and edges
        nx.draw(map, with_labels=True, node_size=100, font_size=8, node_color=node_color_map, edge_color=edge_color_map)
        plt.show()

    #Define a function that will take a player's current data dictionary and update it with new fields
    #input: player data
    #output: player data with added fields
    def add_fields(self):
        for key in self.player_data:
            #If map
            if type(self.player_data[key]) == type(dict()):
                default_map_data = get_map(key)
                default_node_attributes = list(default_map_data.node(data=True))[0][-1]
                default_edge_attributes = list(default_map_data.edges(data=True))[0][-1]
                for affiliation in self.player_data[key]:
                    player_node_attributes = list(self.player_data[key][affiliation].node(data=True))[0][-1]
                    player_edge_attributes = list(self.player_data[key][affiliation].edges(data=True))[0][-1]
                    #Nodes
                    for attribute in list(default_node_attributes.keys()):
                        if attribute not in list(player_node_attributes.keys()):
                            nx.set_node_attributes(self.player_data[key][affiliation], nx.get_node_attributes(default_map_data, attribute), attribute)
                    #Edges
                    for attribute in list(default_edge_attributes.keys()):
                        if attribute not in list(player_edge_attributes.keys()):
                            nx.set_edge_attributes(self.player_data[key][affiliation], nx.get_edge_attributes(default_map_data, attribute), attribute)
