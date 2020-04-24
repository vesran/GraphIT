'''
This file holds all the necessary imports for the project.
It is the only file to execute.
The graphit package, resources folder, eventually test package and this file
should all be in the same folder.
'''

from graphit.graphic_sequence import print_is_graphic_sequence
# from graphit.induced_bipartite_subgraph import extract_bipartite_subgraph

if __name__ == '__main__':
    sequence = [5, 5, 5, 4, 2, 1, 1, 1]
    print_is_graphic_sequence(sequence)