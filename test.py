#This file will contain different tests to make sure the code works across different versions.

from maps import coastline

#Create a function that makes sure that for every edge, the inverse of that edge exists
def test_paths(map):
    assert len([edge for edge in map.edges() if (edge[1], edge[0]) not in map.edges()]) == 0
#Run test by passing in a map
check_paths(coastline)
