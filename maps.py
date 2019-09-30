#this file contain the map dictionary. The structure of this dictionary is as follows:
maps = {
    'COASTLINE' : {
        'EXT' : {
            'MAINENTRANCE' : {
                'N' : ['EXT GARAGEROOF', 'EXT BACKALLEY'],
                'S' : [],
                'E' : [],
                'W' : ['EXT POOL', 'EXT SOUTHPROMENADE'],
                'visited' : 0
            },
            'GARAGEROOF' : {
                'N' : ['EXT BACKALLEY'],
                'S' : ['EXT MAINENTRANCE'],
                'E' : [],
                'W' : ['EXT POOL'],
                'visited' : 0
            },
            'BACKALLEY' : {
                'N' : [],
                'S' : ['EXT MAINENTRANCE', 'EXT GARAGEROOF'],
                'E' : [],
                'W' : ['EXT POOL'],
                'visited' : 0
            },
            'POOL' : {
                'N' : [],
                'S' : [],
                'E' : ['EXT BACKALLEY', 'EXT GARAGEROOF', 'EXT MAINENTRANCE'],
                'W' : [],
                'visited' : 0
            },
            'SOUTHPROMENADE' : {
                'N' : [],
                'S' : [],
                'E' : ['EXT MAINENTRANCE'],
                'W' : [],
                'visited' : 0
            },
        }
    },
    'BORDER' : {
        '' : {
            '' : {
                'N' : [],
                'S' : [],
                'E' : [],
                'W' : [],
                'visited' : 0
            }
        }
    },
    'CLUBHOUSE' : {
        '' : {
            '' : {
                'N' : [],
                'S' : [],
                'E' : [],
                'W' : [],
                'visited' : 0
            }
        }
    },
    'KAFEDOSTOYEVSKY' : {
        '' : {
            '' : {
                'N' : [],
                'S' : [],
                'E' : [],
                'W' : [],
                'visited' : 0
            }
        }
    },
    'VILLA' : {
        '' : {
            '' : {
                'N' : [],
                'S' : [],
                'E' : [],
                'W' : [],
                'visited' : 0
            }
        }
    },
    'BANK' : {
        '' : {
            '' : {
                'N' : [],
                'S' : [],
                'E' : [],
                'W' : [],
                'visited' : 0
            }
        }
    },
    'CONSULATE' : {
        '' : {
            '' : {
                'N' : [],
                'S' : [],
                'E' : [],
                'W' : [],
                'visited' : 0
            }
        }
    }
}
