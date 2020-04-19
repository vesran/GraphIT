from graphit.graphcore import Graph


def is_bipartite(graph, X, Y):
    # Check there is an edge where both endpoints are in X or Y
    for edge in graph.edges:
        v1 = edge.v1
        v2 = edge.v2
        if (X.__contains__(v1) and X.__contains__(v2)) or (Y.__contains__(v1) and Y.__contains__(v2)):
            return False

    return True


def extract_bipartite_subgraph(graph):
    edge_threshold = int(graph.edges.__len__() / 2)
    X = graph.vertices[:int(len(graph.vertices)/2)]
    Y = graph.vertices[int(len(graph.vertices)/2):]

    print(is_bipartite(graph, X, Y))

    print(X)
    print(Y)
    print(edge_threshold)


if __name__ == '__main__':
    pathname = './resources/claw.dat'
    g = Graph()
    g.read_dat(pathname)
    extract_bipartite_subgraph(g)