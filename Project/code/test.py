#This file will contain different tests to make sure the code works across different versions.

from utils import get_map_location_strings, clean, get_round_map_status, pre_clean
from maps import coastline, border, kafedostoyevsky, clubhouse, villa, consulate, bank, map_spawns
import networkx as nx
import random
import matplotlib.pyplot as plt

#Create a function that makes sure that for every edge, the inverse of that edge exists
#An error in assertion would be the result of inproper graphing of a map.
def test_paths(map):
    bad_edges = [edge for edge in map.edges() if (edge[1], edge[0]) not in map.edges()]
    if bad_edges:
        print(bad_edges)
    assert len(bad_edges) == 0
#Run test by passing in a map
test_paths(coastline)
test_paths(border)
test_paths(kafedostoyevsky)
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
test_get_map_strings(border, 47)
test_get_map_strings(kafedostoyevsky, 51)
## TODO: TESTING: Add for each map and double check nodes_expected by counting by hand

#Create a test that checks if the update_data function works for a player object. Note that this specific test is used to check for updates in node_visited and edge_visited.
#A failure in these assertions means that node_visited and edge_visited are not correctly being updated in player_data.
def test_update_data(affiliation):
    test_map_coastline = coastline.copy()
    path_traveled = ['EXTMAINENTRANCE', 'EXTPOOL', 'EXTRUINS', 'EXTROOFTOP', '1FCOURTYARD']
    for index in range(len(path_traveled)):
        test_map_coastline.nodes[path_traveled[index]][f'node_visited_{affiliation}'] += 1
        if index != len(path_traveled) - 1:
            test_map_coastline[path_traveled[index]][path_traveled[index+1]][f'edge_visited_{affiliation}'] += 1
    assert all(node[1][f'node_visited_{affiliation}'] == 1 for node in test_map_coastline.nodes(data=True) if node[0] in path_traveled)
    assert all(node[1][f'node_visited_{affiliation}'] == 0 for node in test_map_coastline.nodes(data=True) if node[0] not in path_traveled)
    test_map_coastline.nodes[path_traveled[-1]][f'deaths_{affiliation}'] += 1
    test_map_coastline[path_traveled[-2]][path_traveled[-1]][f'deaths_{affiliation}'] += 1
    assert test_map_coastline['EXTMAINENTRANCE']['EXTPOOL'][f'edge_visited_{affiliation}'] == 1
    assert test_map_coastline['EXTPOOL']['EXTRUINS'][f'edge_visited_{affiliation}'] == 1
    assert test_map_coastline['EXTRUINS']['EXTROOFTOP'][f'edge_visited_{affiliation}'] == 1
    assert test_map_coastline['EXTROOFTOP']['1FCOURTYARD'][f'edge_visited_{affiliation}'] == 1
    assert test_map_coastline['EXTROOFTOP']['1FCOURTYARD'][f'deaths_{affiliation}'] == 1
    assert test_map_coastline.nodes['1FCOURTYARD'][f'deaths_{affiliation}'] == 1
#Run tests
test_update_data('ATK')
test_update_data('DEF')

#Create a test to test the visualizer with node and edge data only.
#This test will be run and evaluated intuitively.
def test_node_edge_visuals(affiliation):
    #Change map to test for different maps
    test_map = coastline.copy()
    node_color_map = []
    for node in test_map.nodes(data=True):
        node[1][f'node_visited_{affiliation}'] = random.randint(0,100)
    mean_node_visited = sum([node[1][f'node_visited_{affiliation}'] for node in test_map.nodes(data=True)])//len(test_map.nodes())
    for node in test_map.nodes(data=True):
        if node[1][f'node_visited_{affiliation}'] <= mean_node_visited - (mean_node_visited//2):
            node_color_map.append('blue')
        elif node[1][f'node_visited_{affiliation}'] <= mean_node_visited + (mean_node_visited//2):
            node_color_map.append('yellow')
        else:
            node_color_map.append('red')
    edge_color_map = []
    for edge in test_map.edges(data=True):
        edge[-1][f'edge_visited_{affiliation}'] = random.randint(0,100)
    mean_edge_visited = sum([edge[-1][f'edge_visited_{affiliation}'] for edge in test_map.edges(data=True)])//len(test_map.edges())
    for edge in test_map.edges(data=True):
        if edge[-1][f'edge_visited_{affiliation}'] <= mean_edge_visited - (mean_edge_visited//2):
            edge_color_map.append('blue')
        elif edge[-1][f'edge_visited_{affiliation}'] <= mean_edge_visited + (mean_edge_visited//2):
            edge_color_map.append('yellow')
        else:
            edge_color_map.append('red')
    nx.draw(coastline, pos=nx.spring_layout(coastline), with_labels=True, node_size=100, font_size=8, node_color=node_color_map, edge_color=edge_color_map)
    plt.show()
#Run test
test_node_edge_visuals('ATK')
test_node_edge_visuals('DEF')

#Create a test that checks if all map spawns are unique. This is important because if they are, then we are able to differentiate between maps based on spawn.
def test_unique_spawns():
    all_spawns = sum([sum(list(dictionary.values()), []) for dictionary in list(map_spawns.values())], [])
    for index, spawn in enumerate(all_spawns):
        if spawn in all_spawns[index+1:]:
            return False
    return True

#Run test
assert test_unique_spawns() == True

#Create assertions for get_round_map_status function
assert get_round_map_status('EXTMAINENTRANCE') == ('COASTLINE', 'ATK', 'EXTMAINENTRANCE')
assert get_round_map_status('XTMAINENTRANC') == ('COASTLINE', 'ATK', 'EXTMAINENTRANCE')
assert get_round_map_status('2FTHEATER') == ('COASTLINE', 'DEF', '2FTHEATER')
assert get_round_map_status('2FTEATE') == ('COASTLINE', 'DEF', '2FTHEATER')
assert get_round_map_status('EXTVALLEY') == ('BORDER', 'ATK', 'EXTVALLEY')
assert get_round_map_status('EXTVAEY') == ('BORDER', 'ATK', 'EXTVALLEY')
assert get_round_map_status('EXT') == (None, None, None)
assert get_round_map_status('VALLEY') == (None, None, None)

#Test reconstruct path function for functionality.
def test_reconstruct_path(call1, call2):
    test_map_coastline = coastline.copy()
    call1_keys = set(test_map_coastline[call1].keys())
    call2_keys = set(test_map_coastline[call2].keys())
    call_intersect = call1_keys.intersection(call2_keys)
    if len(call_intersect) == 1:
        return call_intersect.pop()
    return None
assert test_reconstruct_path('1FSECURITYROOM', '1FOFFICE') == '1FSUNROOM'
assert test_reconstruct_path('EXTMAINENTRANCE', '1FCOURTYARD') == None
assert test_reconstruct_path('EXTMAINENTRANCE', 'EXTRUINS') == None

#Create a generic funtion that can be used to run test code to put in places that are not run easily.
def generic_test():
    pass
#Run generic test
generic_test()

## TODO: TESTING: Create specific test cases for certain paths traveled and provide correct data and updates for each instance. Ultimately, this test case will end up being all inclusive as to the workings of the program as a whole.
