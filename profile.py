import sys

#this file contains the profile class which will be used to keep track of player data
class Player():
    def __init__(self):
        #acquire player parameters
        resolution = input('What is your resolution? (Compatibile resolutions include anything with the same ratio as 1920x1080)\n')
        if resolution not in ['1920x1080', '2560x1440']:
            print('Incompatibile resolution found!')
            sys.exit(0)
        aspect_ratio = input('What is your aspect ratio? (Compatibile aspect ratios include 3:2, 4:3, 5:4, 16:9, and 16:10)\n')
        if aspect_ratio not in ['3:2', '4:3', '5:4', '16:9', '16:10']:
            print('Incompatibile aspect ratio found!')
            sys.exit(0)
        self.alias = 'Orami.CU' #player's in game name
        self.resolution = [int(element) for element in resolution.split('x')] #players resolution as given by tuple
        self.aspect = [int(element) for element in aspect_ratio.split(':')]  #player's aspect ratio
