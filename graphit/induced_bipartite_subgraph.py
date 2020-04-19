from graphit.graphcore import Graph
from graphit.viz import show


def is_bipartite(graph, X, Y):
    # Check there is an edge where both endpoints are in X or Y
    for edge in graph.edges:
        v1 = edge.v1
        v2 = edge.v2
        if (X.__contains__(v1) and X.__contains__(v2)) or (Y.__contains__(v1) and Y.__contains__(v2)):
            return False

    return True


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
    edge_threshold = int(graph.edges.__len__() / 2)
    X = graph.vertices[:int(len(graph.vertices)/2)]
    Y = graph.vertices[int(len(graph.vertices)/2):]

    i = 1
    while _count_bipartite_edges(graph, X, Y) < edge_threshold:
        print(f"######### Iteration {i} ################")
        print(X)
        print(Y)
        print(_count_bipartite_edges(graph, X, Y))
        i += 1
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
    H = Graph()
    H.vertices = X + Y
    H.edges = _extract_bipartite_edges(graph, X, Y)
    return H



if __name__ == '__main__':
    pathname = './resources/one.dat'
    g = Graph()
    g.read_dat(pathname)
    # show(g)
    H = extract_bipartite_subgraph(g)
    show(H) # TODO : add colors parameters
