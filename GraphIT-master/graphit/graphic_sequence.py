from graphit.graphcore import Graph


def _is_graphic_sequence(sequence):
    sorted_sequence = sorted(sequence, reverse=True)
    print(sorted_sequence)
    if sum(sequence) % 2 != 0 or sum([1 if value < 0 else 0 for value in sequence]):
        return False

    steps = []
    states = []

    while sum(sorted_sequence) > 0:
        steps.append(sorted_sequence[0])
        sorted_sequence.pop(0)
        for i in range(steps[-1]):
            sorted_sequence[i] -= 1
        states.append(sorted_sequence)
        sorted_sequence = sorted(sorted_sequence, reverse=True)
        print(steps[-1])
        print(states[-1])

    return sum(sorted_sequence) == 0


def print_is_graphic_sequence(sequence):
    if _is_graphic_sequence(sequence):
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
    print_is_graphic_sequence(sequenced  )