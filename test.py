#This file will contain different tests to make sure the code works across different versions.

from maps import coastline
from utils import *

#Create a function that makes sure that for every edge, the inverse of that edge exists
#An error in assertion would be the result of inproper graphing of a map.
def test_paths(map):
    assert len([edge for edge in map.edges() if (edge[1], edge[0]) not in map.edges()]) == 0
#Run test by passing in a map
test_paths(coastline)
## TODO: TESTING: Add the rest of the maps once they are complete.

#Create a function that checks if the get_containers function works. The input for this test should be a list of valid resolutions and a list of valid aspect ratios.
#A failure would result from mishandling of user-inputted data for resolution and aspect ratio.
def test_get_containers(resolutions, aspect_ratios):
    for resolution in resolutions:
        for aspect_ratio in aspect_ratios:
            assert get_containers(resolution, aspect_ratio)
#Run test by passing list of resolutions and aspect ratios
test_get_containers([[1920,1080], [1280,720], [2560,1440]], [[3,2], [4,3], [5,4], [16,9], [16,10]])
## TODO: TESTING: Note that we have not yet completely dealt with error handling of inproper inputs. This will be taked care of when making the UI. Therefore, we currently have no test for inproper inputs.

#Create a function that checks if the clean function works for text related to the OCR.
#A failed assertion will most likely be due to a failure in the bound variable or the lenience in error.
def test_clean():
    assert clean('2FHALLWAY', 'COASTLINE') == '2FHALLWAY'
    assert clean('FAQUARIUM', 'COASTLINE') == '2FAQUARIUM'
    assert clean('ETMAINENTRANC', 'COASTLINE') == 'EXTMAINENTRANCE'
    assert clean('THISPROJECTISAWESOME', 'COASTLINE') == None
#Run tests
test_clean()

#Create a test funtion that makes sure that each map has the correct number of nodes. To test this, we will be testing the functionality of the get_map_strings function.
#A failure in assertion here would be caused by incorrect graphing of a map or an incorrect grabbing of nodes.
def test_get_map_strings(map, nodes_expected):
    assert len(get_map_strings(map)) == nodes_expected
#Run the test by passing in a map and the expected number of nodes.
test_get_map_strings(coastline, 37)
## TODO: TESTING: Add for each map and double check the coastline nodes_expected value by counting by hand.

#Create a quick test function to make sure get_map returns the default state of a map.
def test_get_map():
    assert get_map('COASTLINE') == coastline
#Run tests
test_get_map()
## TODO: TESTING: Add the rest of the maps to this test.
