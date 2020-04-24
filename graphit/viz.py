import matplotlib.pyplot as plt
from graphit.graphcore import Graph


def show(graph, markersize=20, annotate=True, edge_colors=None, vertex_colors=None):
    data = [[edges.v1.x, edges.v1.y, edges.v2.x, edges.v2.y] for edges in graph.edges]
    edge_color = 'b'
    vertex_color = 'b'
    for i, edge in enumerate(data):
        if edge_colors is not None:
            edge_color = edge_colors[i]

        plt.plot((edge[0], edge[2]), (edge[1], edge[3]),
                 markersize=markersize, color=edge_color, markerfacecolor=vertex_color)

    for i, v in enumerate(graph.vertices):
        if vertex_colors is not None:
            vertex_color = vertex_colors[i]
        plt.scatter(v.x, v.y, s=markersize*20, color=vertex_color)

    if annotate:
        for vertex in graph.vertices:
            plt.annotate(vertex.id, (vertex.x, vertex.y))

    plt.show()


if __name__ == '__main__':
    pathname = './resources/claw.dat'
    g = Graph()
    g.read_dat(pathname)
    show(g)
