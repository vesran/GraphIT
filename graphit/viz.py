import matplotlib.pyplot as plt
from graphit.graphcore import Graph


def show(graph, markersize=20, annotate=True):
    data = [[edges.v1.x, edges.v1.y, edges.v2.x, edges.v2.y] for edges in graph.edges]
    for edge in data:
        plt.plot((edge[0], edge[2]), (edge[1], edge[3]), 'ro-', markersize=markersize)

    if annotate:
        for vertex in graph.vertices:
            plt.annotate(vertex.id, (vertex.x, vertex.y))
    plt.show()


if __name__ == '__main__':
    pathname = './resources/claw.dat'
    g = Graph()
    g.read_dat(pathname)
    show(g)
