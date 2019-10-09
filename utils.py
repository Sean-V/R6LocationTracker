import cv2
import sys
from maps import *
import stringdist
import numpy as np
#create a list of accepted symbols
accepted_symbols = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3']

#create function that grabs all callouts for a given map
#input: map
#output: list of all string locations plus their callouts
def get_map_strings():
    strings = []
    for location in nx.nodes(coastline):
        strings.append(location)
    return strings

#define a function to sanitize OCR output
#input: output from OCR model and what map the player is on
#output: sanitized text
def clean(output):
    result =  "".join([symbol for symbol in output if symbol in accepted_symbols])
    #define an algorithm to check likely matching string for result
    strings = get_map_strings()
    matching_list = [(string, stringdist.levenshtein(result, string)) for string in strings]
    min_match = min(matching_list, key = lambda pairs: pairs[1])
    best_match = min_match[0] if min_match[1] <= 3 else None
    return best_match

#define a function to process an image before throwing it into OCR
#input: image, bound for determining white and black pixels
#output: black and white image that OCR should be able to better perform on
def process_image(image, bound):
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[x][y] > bound:
                image[x][y] = 0
            else:
                image[x][y] = 255
    return image

#define a function that determines where to crop image
#input: resolution and aspect ratio
#output: list of containers
def get_containers(resolution, aspect):
    if resolution[0]/resolution[1] == 1920/1080:
        res_scale = resolution[0]/1920
    else:
        print('Incompatibile resolution found!')
        sys.exit(0)
    if aspect == [3,2]:
        location = (np.array([1310, 945, 170, 25])*(res_scale)).astype(int)
        callout1 = (np.array([1310, 970, 170, 25])*(res_scale)).astype(int)
        callout2 = (np.array([1310, 992, 170, 22])*(res_scale)).astype(int)
    elif aspect == [4,3]:
        location = (np.array([1350, 945, 200, 25])*(res_scale)).astype(int)
        callout1 = (np.array([1350, 970, 200, 25])*(res_scale)).astype(int)
        callout2 = (np.array([1350, 992, 200, 22])*(res_scale)).astype(int)
    elif aspect == [5,4]:
        location = (np.array([1380, 945, 230, 25])*(res_scale)).astype(int)
        callout1 = (np.array([1380, 970, 230, 25])*(res_scale)).astype(int)
        callout2 = (np.array([1380, 992, 230, 22])*(res_scale)).astype(int)
    elif aspect == [16,9]:
        location = (np.array([1250, 945, 180, 25])*(res_scale)).astype(int)
        callout1 = (np.array([1250, 970, 180, 25])*(res_scale)).astype(int)
        callout2 = (np.array([1250, 992, 180, 22])*(res_scale)).astype(int)
    elif aspect == [16,10]:
        location = (np.array([1285, 945, 200, 25])*(res_scale)).astype(int)
        callout1 = (np.array([1285, 970, 200, 25])*(res_scale)).astype(int)
        callout2 = (np.array([1285, 992, 200, 22])*(res_scale)).astype(int)
    else:
        print('Incompatibile resolution or aspect ratio found!')
        sys.exit(0)
    return location, callout1, callout2
