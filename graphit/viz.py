# To delete

import matplotlib.pyplot as plt
from graphit.graphcore import Graph
import networkx as nx


def show(graph):
    G = nx.MultiGraph()
    for v in graph.vertices:
        G.add_node(v.id)
    for edge in graph.edges:
        G.add_edge(edge.v1.id, edge.v2.id)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color='r', node_size=200)
    nx.draw_networkx_labels(G, pos, node_color='r', node_size=100)
    ax = plt.gca()
    for e in G.edges:
        ax.annotate("",
                    xy=pos[e[0]], xycoords='data',
                    xytext=pos[e[1]], textcoords='data',
                    arrowprops=dict(arrowstyle="-", color="0.5",
                                    shrinkA=5, shrinkB=5,
                                    patchA=None, patchB=None,
                                    connectionstyle="arc3,rad=rrr".replace('rrr', str(0.15 * e[2])
                                                                           ),
                                    ),
                    )
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    pathname = './resources/claw.dat'
    g = Graph()
    g.read_dat(pathname)
    show(g)
