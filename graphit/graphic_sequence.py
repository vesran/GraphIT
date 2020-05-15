from graphit.graphcore import Graph


def _is_graphic_sequence(sequence, verbose=False):
    sorted_sequence = sorted(sequence, reverse=True)
    print("---- Initial sequence :", sorted_sequence) if verbose else 0

    # The sequence is not graphic if the list is empty the sum is not even
    # or if there is a negative value or a vertex has more neighbors than vertices
    if len(sequence) == 0 or sum(sequence) % 2 != 0 \
            or any(x < 0 for x in sequence) \
            or max(sequence) > len(sequence):
        return False

    while sum(sorted_sequence) > 0:
        highest_degree_vertex = sorted_sequence.pop(0)

        if highest_degree_vertex > len(sorted_sequence):
            # A vertex has more neighbors than the number of available vertex
            return False

        for i in range(highest_degree_vertex):
            sorted_sequence[i] -= 1

        print("-------- Chosen int :", highest_degree_vertex, " -- ", sorted_sequence) if verbose else 0
        sorted_sequence = sorted(sorted_sequence, reverse=True)
        print("--------", sorted_sequence, "is the sorted sequence.") if verbose else 0

    # Returns True if there is no negative value (x < 0)
    return not any(x < 0 for x in sorted_sequence)


def print_is_graphic_sequence(sequence_or_file, verbose=False):
    # Handle file and list case in parameters
    if type(sequence_or_file) == str:
        # File as input
        filename = sequence_or_file
        with open(filename, 'r') as f:
            lines = f.readlines()
        sequence = [int(line) for line in lines]
    else:
        # List as input
        sequence = sequence_or_file

    if _is_graphic_sequence(sequence, verbose=verbose):
        print('The sequence is graphic')
    else:
        print('The sequence is not graphic')


if __name__ == '__main__':
    #G = Graph()
    #G.random_init(10, 14)
    #sequence = [v.neighbors.__len__() for v in G.vertices]
    #sequence[0] += -10
    #sequence = [7, 6, 6, 4, 3, 2, 1, 1]
    sequencea = [5, 5, 4, 3, 2, 2, 2, 1]
    sequenceb = [5, 5, 4, 4, 2, 2, 1, 1]
    sequencec = [5, 5, 5, 3, 2, 2, 1, 1]
    sequenced = [5, 5, 5, 4, 2, 1, 1, 1]
    print_is_graphic_sequence('./resources/graphic_seq_false', verbose=True)
