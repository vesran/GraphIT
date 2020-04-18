
class Graph:

    def __init__(self):
        self.vertices = []
        self.edges = []
        self.num_edges = 0
        self.num_vertices = 0

    def read_dat(self, pathname):
        with open(pathname, 'r') as f:
            # Catch the numbers of edges and vertices
            first_line = f.readline()
            nums = first_line.split()
            self.num_vertices = int(nums[0])
            self.num_edges = int(nums[-1])

            # Get all lines to be read
            lines = f.readlines()

        for idt, line in enumerate(lines):
            data = line.split()

            if data[0].__contains__('.'):
                # Vertices position data
                vertex = Vertex(float(data[0]), float(data[-1]), idt)
                self.vertices.append(vertex)

            else:
                # Edges data
                v1 = None
                v2 = None
                for vertex in self.vertices:
                    if int(data[0]) == vertex.id:
                        v1 = vertex
                    if int(data[-1]) == vertex.id:  # Edge can be a loop
                        v2 = vertex

                edge = Edge(v1, v2)
                self.edges.append(edge)

        assert len(self.vertices) == self.num_vertices
        assert len(self.edges) == self.num_edges


class Vertex:

    def __init__(self, x, y, id):
        self.id = id
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<id={self.id}-({self.x}, {self.y})>'


class Edge:

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def __repr__(self):
        return f'{self.v1}--{self.v2}'


if __name__ == '__main__':
    pathname = './resources/claw.dat'
    g = Graph()
    g.read_dat(pathname)

    print(g.vertices)
    print(g.edges)
