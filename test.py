#This file will contain different tests to make sure the code works across different versions.

from utils import *
import random
import matplotlib.pyplot as plt

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

#Create a test that checks if the update_data function works for a player object. Note that this specific test is used to check for updates in node_visited and edge_visited.
#A failure in these assertions means that node_visited and edge_visited are not correctly being updated in player_data.
def test_update_data():
    test_map_coastline = coastline
    path_traveled = ['EXTMAINENTRANCE', 'EXTPOOL', 'EXTRUINS', 'EXTROOFTOP', '1FCOURTYARD']
    for index in range(len(path_traveled)):
        test_map_coastline.nodes[path_traveled[index]]['node_visited'] += 1
        if index != len(path_traveled) - 1:
            test_map_coastline[path_traveled[index]][path_traveled[index+1]]['edge_visited'] += 1
    assert all(node[1]['node_visited'] == 1 for node in test_map_coastline.nodes(data=True) if node[0] in path_traveled)
    assert all(node[1]['node_visited'] == 0 for node in test_map_coastline.nodes(data=True) if node[0] not in path_traveled)
    assert test_map_coastline['EXTMAINENTRANCE']['EXTPOOL']['edge_visited'] == 1
    assert test_map_coastline['EXTPOOL']['EXTRUINS']['edge_visited'] == 1
    assert test_map_coastline['EXTRUINS']['EXTROOFTOP']['edge_visited'] == 1
    assert test_map_coastline['EXTROOFTOP']['1FCOURTYARD']['edge_visited'] == 1
#Run tests
test_update_data()

#Create a test to test the visualizer with node and edge data only.
#This test will be run and evaluated intuitively.
def test_node_edge_visuals():
    #Change map to test for different maps
    test_map = coastline
    node_color_map = []
    for node in test_map.nodes(data=True):
        node[1]['node_visited'] = random.randint(0,100)
    mean_node_visited = sum([node[1]['node_visited'] for node in test_map.nodes(data=True)])//len(test_map.nodes())
    for node in test_map.nodes(data=True):
        if node[1]['node_visited'] <= mean_node_visited - (mean_node_visited//2):
            node_color_map.append('blue')
        elif node[1]['node_visited'] <= mean_node_visited + (mean_node_visited//2):
            node_color_map.append('yellow')
        else:
            node_color_map.append('red')
    edge_color_map = []
    for edge in test_map.edges(data=True):
        edge[-1]['edge_visited'] = random.randint(0,100)
    mean_edge_visited = sum([edge[-1]['edge_visited'] for edge in test_map.edges(data=True)])//len(test_map.edges())
    for edge in test_map.edges(data=True):
        if edge[-1]['edge_visited'] <= mean_edge_visited - (mean_edge_visited//2):
            edge_color_map.append('blue')
        elif edge[-1]['edge_visited'] <= mean_edge_visited + (mean_edge_visited//2):
            edge_color_map.append('yellow')
        else:
            edge_color_map.append('red')
    nx.draw(coastline, with_labels=True, node_size=100, font_size=8, node_color=node_color_map, edge_color=edge_color_map)
    plt.show()
#Run test
test_node_edge_visuals()

## TODO: TESTING: Create specific test cases for certain paths traveled and provide correct data and updates for each instance. Ultimately, this test case will end up being all inclusive as to the workings of the program as a whole.
