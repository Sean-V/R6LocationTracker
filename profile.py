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
