import sys
from PIL import ImageGrab, Image
import numpy as np
from utils import *
from profile import Player
from maps import *
import pytesseract
from pytesseract import image_to_string
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\svand\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

#import player
player = Player()

#define containers for cropped image locations
location, callout1, callout2, playerbox = get_containers(player.resolution, player.aspect)
path_traveled = []

while True:
    #get frame from the game
    image = np.array(ImageGrab.grab(bbox=(0, 0, player.resolution[0], player.resolution[1])))
    crop_image_playerbox = image[playerbox[1]:playerbox[1]+playerbox[3], playerbox[0]:playerbox[0]+playerbox[2]]
    #playerbox finds the white square around a player icon to tell if the player is still alive
    #get playerbox indicators
    playerbox_indicators = [
        crop_image_playerbox[(crop_image_playerbox.shape[0]-1)][(crop_image_playerbox.shape[1]-1)],
        crop_image_playerbox[(crop_image_playerbox.shape[0]-1)][0],
        crop_image_playerbox[0][(crop_image_playerbox.shape[1]-1)],
        crop_image_playerbox[0][0]
    ]
    #convert image to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #crop current frame into subset frames
    #location is the top line of each callout. this information includes floor number or whether the player is in the exterior portion of the map
    #callout1 is the location of the first line of a room or area
    #callout2 includes the second line of the room or area
    crop_image_location = image[location[1]:location[1]+location[3], location[0]:location[0]+location[2]]
    crop_image_callout1 = image[callout1[1]:callout1[1]+callout1[3], callout1[0]:callout1[0]+callout1[2]]
    crop_image_callout2 = image[callout2[1]:callout2[1]+callout2[3], callout2[0]:callout2[0]+callout2[2]]

    #define bound for processing
    #current method takes the max vlue of the pixel in the image and subtracts the mean of pixel values. this should theoretically make the text white and the background black but we end up swapping values in the function to make the text black and the background white
    bound = np.max(image) - np.mean(image)
    #process subset frames
    proc_image_location = process_image(crop_image_location.copy(), bound)
    proc_image_callout1 = process_image(crop_image_callout1.copy(), bound)
    proc_image_callout2 = process_image(crop_image_callout2.copy(), bound)

    #store result of OCR processing for each subset frame
    text_location = (image_to_string(proc_image_location, lang='eng')).upper()
    #1F is frequently read as TF by the OCR so we are going to preemptively alter this so that callouts like 1FHALLWAY and 2FHALLWAY do not get confused
    if text_location == "TF":
        text_location = "1F"
    text_callout1 = (image_to_string(proc_image_callout1, lang='eng')).upper()
    text_callout2 = (image_to_string(proc_image_callout2, lang='eng')).upper()
    text_callout = text_callout1 + text_callout2
    text = clean(text_location + text_callout)

    #start storing location changes into a list
    current_pos = text
    if len(path_traveled) == 0 and current_pos != None:
            path_traveled.append(current_pos)
    elif current_pos != None and path_traveled[-1] != current_pos:
        path_traveled.append(current_pos)

    #check if player is alive
    player_alive = is_player_alive(playerbox_indicators)

    #now that we have location grabbing, location adding, and whether the player is alive, we can get round-based data
    

    #TESTING
    #cv2.imshow('test1', crop_image_playerbox)
    #cv2.waitKey(0)
    #print(playerbox_indicators)
    print(current_pos)
    print(path_traveled)
    print(player_alive)
    print('------------')
