from graphit.graphcore import Graph
from graphit.graphic_sequence import print_is_graphic_sequence
from graphit.induced_bipartite_subgraph import extract_bipartite_subgraph, export2tex_bipartite_subgraph

if __name__ == '__main__':

    # Export the induced bipartite subgraph.
    pathname = './resources/hexa.dat'
    export2tex_bipartite_subgraph(pathname, dest_name='./resources/out.tex', verbose=True)

    # Display if the sequence is graphic (input as file or list)
    print_is_graphic_sequence('./resources/graphic_seq_false', verbose=True)
    # print_is_graphic_sequence([2, 1, 1], verbose=True)
