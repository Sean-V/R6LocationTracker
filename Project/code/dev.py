#This file will be used for developmental purposes. Ultimately, the purpose of this file is to act as the main.

import os
import cv2
from utils import clean, process_image, get_containers, is_player_alive, screen_capture, get_round_map_status, pre_clean
from profile import Player
import pytesseract
import numpy as np
from pytesseract import image_to_string
## TODO: USER: Change this pathing to be universal among users. It might be helpful to look at tesseract-OCR's installation manual and how they suggest setting the path.
pytesseract.pytesseract.tesseract_cmd = 'C:{}\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'.format(os.environ['HOMEPATH'])

## TODO: USER: Make some sort of GUI for the player to interact with where they can login and store their own profiles. For now we will just import a test player object to work with.
#For now we will incorporate a preliminary UI that will run in the terminal. This will be built in the Player class in profile.py. This will allow us to easily remove the UI later.
player = Player()

#Define some initial variables
#location, callout1, callout2, playerbox will contain coordinates needed to grab specific data from each screen
location, callout1, callout2, playerbox = get_containers(player.resolution, player.aspect_ratio)
#Path traveled will contain the path for any given round. This will be reinitialized every round.
path_traveled = []
map_string, affiliation = None, None

while True:
    #First we must get the frame from the game
    image = np.array(screen_capture(player.resolution))

    #Then we must find the indicators that tell us whether the player is alive. This information comes from an area we call the playerbox. The playerbox is the icon for the player found on the HUD. In this case we want to see if there is a white box surrounding this player icon. This tells us whether the player is still alive.
    crop_image_playerbox = image[playerbox[1]:playerbox[1]+playerbox[3], playerbox[0]:playerbox[0]+playerbox[2]]
    playerbox_indicators = [
        crop_image_playerbox[(crop_image_playerbox.shape[0]-1)][(crop_image_playerbox.shape[1]-1)],
        crop_image_playerbox[(crop_image_playerbox.shape[0]-1)][0],
        crop_image_playerbox[0][(crop_image_playerbox.shape[1]-1)],
        crop_image_playerbox[0][0]
    ]

    #Then for every frame of playerbox we get we must check if the player is alive
    player_alive = is_player_alive(playerbox_indicators)
    if player_alive:
        #If the player is alive then we can further process the frame. Before we can process the frame we will convert the image to grayscale. The processing of the frame will include defining three different boxes where text for the callouts will be located. We call these boxes location, callout1, and callout2. Once these boxes are grabbed, the image will be processed so that every pixel is either white (255) or black (0). This will make it easier for the OCR to classify text properly.
        #Convert image to grayscale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #location is the top line of each callout. this information includes floor number or whether the player is in the exterior portion of the map
        #callout1 is the location of the first line of a room or area
        #callout2 includes the second line of the room or area
        crop_image_location = image[location[1]:location[1]+location[3], location[0]:location[0]+location[2]]
        crop_image_callout1 = image[callout1[1]:callout1[1]+callout1[3], callout1[0]:callout1[0]+callout1[2]]
        crop_image_callout2 = image[callout2[1]:callout2[1]+callout2[3], callout2[0]:callout2[0]+callout2[2]]

        #cv2.imshow('location', crop_image_location)
        #cv2.waitKey(0)
        #cv2.imshow('callout_1', crop_image_callout1)
        #cv2.waitKey(0)
        #cv2.imshow('callout_2', crop_image_callout2)
        #cv2.waitKey(0)

        #Define bound for processing
        #Current method takes the max vlue of the pixel in the image and subtracts the mean of pixel values. this should theoretically make the text white and the background black but we end up swapping values in the function to make the text black and the background white.
        bound = np.max(image) - np.mean(image)
        #Process subset frames
        proc_image_location = process_image(crop_image_location.copy(), bound)
        proc_image_callout1 = process_image(crop_image_callout1.copy(), bound)
        proc_image_callout2 = process_image(crop_image_callout2.copy(), bound)

        #Now that our images have been processed, we can throw those images into the OCR to acquire our text. We will than perform some sanitization and correct error that is within reason.
        #Store result of OCR processing for each subset frame
        text_location = (image_to_string(proc_image_location, lang='eng')).upper()
        text_location = pre_clean(text_location)
        text_callout1 = (image_to_string(proc_image_callout1, lang='eng')).upper()
        text_callout2 = (image_to_string(proc_image_callout2, lang='eng')).upper()
        text_callout = text_location + text_callout1 + text_callout2
        #If map and affiliation not known, then we need to try to determine map and affiliation for round
        if (map_string, affiliation) == (None, None):
            map_string, affiliation, first_match = get_round_map_status(text_callout)
            #This takes caore of the first instance for adding to path path_traveled
            if first_match != None:
                path_traveled.append(first_match)
                print(path_traveled)
        #If map and affiliation are known then we can build paths
        if path_traveled:
            text = clean(text_callout, map_string)
            #Now that we have our text, we will check if a valid callout is constructed. If it is, we will check if a player has moved from their current position. If so, the callout will be added to a list that represents the path traveled.
            #Start storing location changes into a list
            current_pos = text
            #This takes care of every other relevant instance of changes in location
            if current_pos != None and path_traveled[-1] != current_pos:
                path_traveled.append(current_pos)
                print(path_traveled)
            ## TODO: ACCURACY: Make a better error handling system for if the program accidently skips over a room.

    #This next part will determine what to do when the player is deemed to not be alive.
    else:
        #If player is dead, we need to store path traveled data if data exists
        if len(path_traveled) > 0:
            #Perform updates to player_data
            player.update_data(path_traveled, map_string, affiliation)
            ## TODO: SCALABILITY: Currently this method is loading and updating the player's save file every round. This is inefficient, but will work for testing. Later on a method should be devised to update on a per game basis.
            player.store_data()
            print("Data saved to {} : {}".format(map_string, affiliation))
        #If the player is dead, we need to reset the path traveled variable
        path_traveled = []
        map_string, affiliation = None, None
