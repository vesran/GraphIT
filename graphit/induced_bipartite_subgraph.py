from graphit.graphcore import Graph


def _count_bipartite_edges(G, X, Y):
    """ Counts the number of edges in G which starts has an endpoints in X and Y.
    :param G: Graph
    :param X: Vertex set from G
    :param Y: Vertex set from G
    :return: Integer
    """
    cpt = 0
    for edge in G.edges:
        v1 = edge.v1
        v2 = edge.v2
        if (X.__contains__(v1) and Y.__contains__(v2)) or (X.__contains__(v2) and Y.__contains__(v1)):
            cpt += 1
    return cpt


def _extract_bipartite_edges(G, X, Y):
    """ Extracts edges which have an endpoints in X and in Y.
    :param G: Graph
    :param X: Vertex set from G
    :param Y: Vertex set from G
    :return: List of edges extracted from G
    """
    bipartite_edges = []
    for edge in G.edges:
        v1 = edge.v1
        v2 = edge.v2
        if (X.__contains__(v1) and Y.__contains__(v2)) or (X.__contains__(v2) and Y.__contains__(v1)):
            bipartite_edges.append(edge)
    return bipartite_edges


def _count_subset_neighbors(v, X):
    """ Counts the number of neighbors of vertex v which are in X.
    :param v: A vertex
    :param X: Vertex set
    :return: Integer
    """
    return len(set(v.neighbors).intersection(X))


def extract_bipartite_subgraph(graph, verbose=False):
    """ Extracts a bipartite subgraph of the given graph with at least e(G)/2 edges.
    :param graph: Graph to extract the subgraph from.
    :param verbose: Boolean to display messages
    :return: tuple (subgraph, partite set X, partite set Y)
    """
    edge_threshold = int(graph.edges.__len__() / 2) + 1
    X = graph.vertices[:int(len(graph.vertices)/2)]
    Y = graph.vertices[int(len(graph.vertices)/2):]

    i = 1
    while _count_bipartite_edges(graph, X, Y) < edge_threshold:
        print(f"================ Iteration {i} ===================") if verbose else 0
        i += 1
        print("X", X) if verbose else 0
        print("Y", Y) if verbose else 0
        print(_count_bipartite_edges(graph, X, Y)) if verbose else 0
        # Find in X and Ythe best vertex to move
        best_vertex_X, best_vertex_Y = X[0], Y[0]
        best_score_X, best_score_Y = -10000, -10000
        for vertex in X:
            score = _count_subset_neighbors(vertex, X) - _count_subset_neighbors(vertex, Y)
            if score > best_score_X:
                best_score_X, best_vertex_X = score, vertex

        for vertex in Y:
            score = _count_subset_neighbors(vertex, Y) - _count_subset_neighbors(vertex, X)
            if score > best_score_Y:
                best_score_Y, best_vertex_Y = score, vertex

        # Move best vertex
        print(f"Edge gains X -> Y : {best_score_X} - {best_vertex_X}") if verbose else 0
        print(f"Edge gains Y -> X: {best_score_Y} - {best_vertex_Y}") if verbose else 0
        if best_score_X > best_score_Y:
            # Move X vertex to Y
            X.remove(best_vertex_X)
            Y.append(best_vertex_X)
        else:
            # Move vertex Y to X
            Y.remove(best_vertex_Y)
            X.append(best_vertex_Y)

    # Extract bipartite subgraph
    print("X", X) if verbose else 0
    print("Y", Y) if verbose else 0
    H = Graph()
    H.edges = _extract_bipartite_edges(graph, X, Y)
    H.vertices = X + Y
    return H, X, Y


def export2tex_bipartite_subgraph(pathname, dest_name='./out.tex', verbose=False):
    """ Extracts a bipartite subgraph from the graph described in the given file and export the same graph
    to a new file with the subgraph in red. Graph must be loopless, otherwise the algorithm stops.
    :param pathname: Initial graph file
    :param dest_name: Output file
    :param verbose: Boolean to display messages
    :return: None
    """
    g = Graph()
    g.read_dat(pathname)

    # Check if the given graph is loopless
    if any(edge.v1.id == edge.v2.id for edge in g.edges):
        print('The specified graph is not loopless. It might not contains a bipartite subgraph with e(G)/2 edges.')
        return

    # Extract bipartite graph
    H, X, Y = extract_bipartite_subgraph(g)
    print("Partite set X :", X) if verbose else 0
    print("Partite set Y :", Y) if verbose else 0
    print(f'Ratio of marked edges : {_count_bipartite_edges(g, X, Y)}/{g.num_edges}')
    print("File created :", dest_name)
    g.exportbipartite2tex(H, dest_name=dest_name)


if __name__ == '__main__':
    from graphit.viz import *
    pathname = './resources/hexa.dat'
    g = Graph()
    g.read_dat(pathname)

    # g.random_init(6, 4, loop=False, multiple_edges=True)
    H, X, Y = extract_bipartite_subgraph(g)
    # show(g)
    # g.exportbipartite2tex(H, './resources/bipartite_test.tex')

    export2tex_bipartite_subgraph(pathname, dest_name='./resources/out.tex', verbose=True)
