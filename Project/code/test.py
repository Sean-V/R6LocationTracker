#This file will contain different tests to make sure the code works across different versions.

from utils import get_map_location_strings, clean, get_round_map_status
from maps import coastline, border, kafedostoyevsky, clubhouse, villa, consulate, bank, map_spawns
import networkx as nx
import random
import matplotlib.pyplot as plt

#Create a function that makes sure that for every edge, the inverse of that edge exists
#An error in assertion would be the result of inproper graphing of a map.
def test_paths(map):
    assert len([edge for edge in map.edges() if (edge[1], edge[0]) not in map.edges()]) == 0
#Run test by passing in a map
test_paths(coastline)
## TODO: TESTING: Add the rest of the maps once they are complete.

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
    assert len(get_map_location_strings(map)) == nodes_expected
#Run the test by passing in a map and the expected number of nodes.
test_get_map_strings(coastline, 37)
## TODO: TESTING: Add for each map and double check the coastline nodes_expected value by counting by hand.

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
    #nx.draw(coastline, with_labels=True, node_size=100, font_size=8, node_color=node_color_map, edge_color=edge_color_map)
    #plt.show()
#Run test
test_node_edge_visuals()

#Create a test that checks if all map spawns are unique. This is important because if they are, then we are able to differentiate between maps based on spawn.
def test_unique_spawns():
    all_spawns = sum([sum(list(dictionary.values()), []) for dictionary in list(map_spawns.values())], [])
    for index, spawn in enumerate(all_spawns):
        if spawn in all_spawns[index+1:]:
            return False
    return True

#Run test
assert test_unique_spawns() == True

#Create test asserions to see if the get_round_map_status function appears to work properly
assert get_round_map_status('EXTMAINENTRANCE') == ('COASTLINE', 'ATK')
assert get_round_map_status('2FTHEATER') == ('COASTLINE', 'DEF')
assert get_round_map_status('EXTVALLEY') == ('BORDER', 'ATK')
assert get_round_map_status('WRONGINPUT') == (None, None)

#Create a generic funtion that can be used to run test code to put in places that are not run easily.
def generic_test():
    pass
#Run generic test
generic_test()

## TODO: TESTING: Create specific test cases for certain paths traveled and provide correct data and updates for each instance. Ultimately, this test case will end up being all inclusive as to the workings of the program as a whole.
