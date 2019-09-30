import sys
from PIL import ImageGrab
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
location, callout1, callout2 = get_containers(player.resolution, player.aspect)

while True:
    #get frame from the game
    image = np.array(ImageGrab.grab(bbox=(0, 0, player.resolution[0], player.resolution[1])))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #crop current frame into subset frames
    crop_image_location = image[location[1]:location[1]+location[3], location[0]:location[0]+location[2]]
    crop_image_callout1 = image[callout1[1]:callout1[1]+callout1[3], callout1[0]:callout1[0]+callout1[2]]
    crop_image_callout2 = image[callout2[1]:callout2[1]+callout2[3], callout2[0]:callout2[0]+callout2[2]]
    #define bound for processing
    bound = np.max(image) - np.mean(image)
    #process subset frames
    proc_image_location = process_image(crop_image_location.copy(), bound)
    proc_image_callout1 = process_image(crop_image_callout1.copy(), bound)
    proc_image_callout2 = process_image(crop_image_callout2.copy(), bound)
    cv2.imshow('image', proc_image_location)
    cv2.waitKey(1000)
    cv2.imshow('image', proc_image_callout1)
    cv2.waitKey(1000)
    cv2.imshow('image', proc_image_callout2)
    cv2.waitKey(1000)
    #store result of OCR processing for each subset frame
    text_location = (image_to_string(proc_image_location, lang='eng')).upper()
    text_callout1 = (image_to_string(proc_image_callout1, lang='eng')).upper()
    text_callout2 = (image_to_string(proc_image_callout2, lang='eng')).upper()
    text_callout = text_callout1 + text_callout2
    text = text_location + text_callout
    print(clean(text, 'COASTLINE'))
    print('------------')
