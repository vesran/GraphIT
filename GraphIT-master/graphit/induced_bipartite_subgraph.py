from graphit.graphcore import Graph


def _count_bipartite_edges(G, X, Y):
    cpt = 0
    for edge in G.edges:
        v1 = edge.v1
        v2 = edge.v2
        if (X.__contains__(v1) and Y.__contains__(v2)) or (X.__contains__(v2) and Y.__contains__(v1)):
            cpt += 1
    return cpt


def _extract_bipartite_edges(G, X, Y):
    bipartite_edges = []
    for edge in G.edges:
        v1 = edge.v1
        v2 = edge.v2
        if (X.__contains__(v1) and Y.__contains__(v2)) or (X.__contains__(v2) and Y.__contains__(v1)):
            bipartite_edges.append(edge)
    return bipartite_edges


def _count_subset_neighbors(v, X):
    return len(set(v.neighbors).intersection(X))


def extract_bipartite_subgraph(graph):
    edge_threshold = int(graph.edges.__len__() / 2) + 1
    X = graph.vertices[:int(len(graph.vertices)/2)]
    Y = graph.vertices[int(len(graph.vertices)/2):]

    i = 1
    print("toto")
    while _count_bipartite_edges(graph, X, Y) < edge_threshold:
        print(f"######### Iteration {i} ################")
        i += 1
        print("X",X)
        print("Y", Y)
        print(_count_bipartite_edges(graph, X, Y))
        # Find in X the best vertex to move
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
        print(f"Best score in X : {best_score_X} - {best_vertex_X}")
        print(f"Best score in Y : {best_score_Y} - {best_vertex_Y}")
        if best_score_X > best_score_Y:
            # Move X vertex to Y
            X.remove(best_vertex_X)
            Y.append(best_vertex_X)
        else:
            # Move vertex Y to X
            Y.remove(best_vertex_Y)
            X.append(best_vertex_Y)

    # Extract bipartite subgraph
    print("X",X)
    print("Y",Y)
    H = Graph()
    H.edges = _extract_bipartite_edges(graph, X, Y)
    H.vertices = X + Y
    return H, X, Y


if __name__ == '__main__':
    pathname = 'C:/Johana/Theorie des graphes/GraphIT-master/GraphIT-master/resources/bipartite1.dat'
    g = Graph()
    g.read_dat(pathname)

    #g.random_init(10, 13)
    H, X, Y = extract_bipartite_subgraph(g)

   
    g.exportbipartite2tex(H,'C:/Johana/Theorie des graphes/GraphIT-master/GraphIT-master/resources/bipartite1.tex')
