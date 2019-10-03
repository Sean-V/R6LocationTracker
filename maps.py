#this file contain the map dictionary. The structure of this dictionary is as follows:
import networkx as nx
import matplotlib.pyplot as plt
coastline = nx.DiGraph()
coastline.add_node('COASTLINE')
coastline.add_edges_from([
    ('COASTLINE', 'EXTMAINENTRANCE'), ('COASTLINE', 'EXTPOOLSIDE'), ('COASTLINE', 'EXTRUINS'),
    ('EXTMAINENTRANCE', 'EXTPOOL'), ('EXTMAINENTRANCE', 'EXTBACKALLEY'), ('EXTMAINENTRANCE', 'EXTGARAGEROOF'), ('EXTMAINENTRANCE', 'EXTSOUTHPROMENADE'), ('EXTMAINENTRANCE', 'EXTROOFTOP'), ('EXTMAINENTRANCE', '2FHALLWAY'), ('EXTMAINENTRANCE', '1FSERVICEENTRANCE'), ('EXTMAINENTRANCE', '2FPENTHOUSE'), ('EXTMAINENTRANCE', '1FMAINLOBBY'),
    ('EXTGARAGEROOF', 'EXTBACKALLEY'), ('EXTGARAGEROOF', 'EXTPOOL'), ('EXTGARAGEROOF', 'EXTMAINENTRANCE'),
    ('EXTBACKALLEY', 'EXTGARAGEROOF'), ('EXTBACKALLEY', 'EXTPOOL'), ('EXTBACKALLEY', 'EXTMAINENTRANCE')
])
nx.draw(coastline, pos=nx.planar_layout(coastline) , with_labels=True)
plt.show()
