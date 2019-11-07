#This file contains the profile class which will be used to keep track of player data.

from maps import coastline
from os import path
import pickle

class Player():
    def __init__(self):
        #Ask for player's in game name to either load or create a profile
        self.alias = input('Enter your in game name for Rainbow Six Siege:\n')
        #Check if player file exists already
        if path.exists(f'profiles/{self.alias}.pickle'):
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
                'COASTLINE':coastline
            }
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
    def update_data(self, path_traveled, map_string):
        #For now, we are going to update the weights between edges and specific nodes. Nodes will represent if a player was at a certain location while edges will represent movement between two locations.
        ## TODO: IDEA: Update each weight based on time factor in order to get a better idea of what areas players spend most of their time.
        for index in range(len(path_traveled)):
            #Update node_visited
            self.player_data[map_string].nodes[path_traveled[index]]['node_visited'] += 1
            #Update edge_visited
            if index != len(path_traveled) - 1:
                #Use try except for now in order to skip location changes that are not valid.
                self.player_data[map_string][path_traveled[index]][path_traveled[index+1]]['edge_visited'] += 1
