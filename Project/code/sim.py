#This file is designed to simulate player movement. The purpose behind this file is to generate data for testing functionality of certain functions.

from profile import Player
import os

#Define a test player with default alias of 'Test', resolution of '1920x1080', and aspect ratio of '16:9'
player = Player('Orami.CU', '1920x1080', '3:2')
player.visualize_data('KAFEDOSTOYEVSKY', 'ATK', ['visited'])
