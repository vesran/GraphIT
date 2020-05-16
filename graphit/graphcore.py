import random as rand

header_tex = '''\\documentclass {article}
\\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry}
\\usepackage{amsfonts,amssymb}
\\usepackage{tikz}
\\begin{document}
\\begin{center}
\\begin{tikzpicture}
\\tikzset{vertex/.style={draw,circle,minimum width=1.6 em,inner sep =0 pt}}
\\tikzset{edge/.style={color=black}}

'''

footer_tex = '''\\end{tikzpicture}
\\end{center}
\\end{document}
'''


class Graph:
    """
    Graph is a representation of a graph. It mainly contains a list of vertices and of edges.
    It is possible to import a graph from a file in a .dat format and to export it in a .tex file.
    It is also possible to generates a graph randomly.
    """

    def __init__(self):
        self.vertices = []
        self.edges = []
        self.num_edges = 0
        self.num_vertices = 0

    def read_dat(self, pathname):
        """ Reads the given file to build a graph.
        :param pathname: Filename in .dat format
        :return: None
        """
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
                v1.neighbors.append(v2)
                v2.neighbors.append(v1)

        assert len(self.vertices) == self.num_vertices
        assert len(self.edges) == self.num_edges

    def export2tex(self, dest_name='output.tex'):
        """ Export the graph to the specified output file.
        :param dest_name: Name of the output file in .tex format.
        :return: None
        """
        margin = 0
        with open(dest_name, 'w') as f:
            f.write(header_tex)

            # Write vertices
            for vertex in self.vertices:
                f.write(
                    f'\\node[ vertex ] ({vertex.id}) at ({vertex.x + margin} ,{vertex.y + margin}) {{}}; \\draw({vertex.id}) node {{${vertex.id}$ }};')
                f.write('\n')

            # Write edges
            f.write('% Edges')
            f.write('\n')
            for edge in self.edges:
                f.write(f'\\draw[ edge ] ({edge.v1.id}) -- ({edge.v2.id});')
                f.write('\n')

            f.write(footer_tex)

    def exportbipartite2tex(self, H, dest_name='output.tex'):
        """ Exports the graph in a .tex format with the subgraph H displayed in red.
        :param H: Bipartite subgraph of the actual graph.
        :param dest_name: The name of the output file.
        :return: None
        """
        margin = 0
        with open(dest_name, 'w') as f:
            f.write(header_tex)
            f.write("\\tikzset{Hedge/.style={line width=2pt,color=red}}")

            # Write vertices
            for vertex in self.vertices:
                f.write(
                    f'\\node[ vertex ] ({vertex.id}) at ({vertex.x + margin} ,{vertex.y + margin}) {{}}; \\draw({vertex.id}) node {{${vertex.id}$ }};')
                f.write('\n')

            # Write edges  and hedges

            for edge in self.edges:
                if edge in H.edges:
                    f.write(f'\\draw[ Hedge ] ({edge.v1.id}) -- ({edge.v2.id});')
                    f.write('\n')
                else:
                    f.write(f'\\draw[ edge ] ({edge.v1.id}) -- ({edge.v2.id});')
                    f.write('\n')

            f.write(footer_tex)

    def random_init(self, num_vertices, num_edges, loop=False, multiple_edges=False):
        """ Randomly init the graph after erasing its parameters.
        :param num_vertices: Number of vertices desired
        :param num_edges: Number of edges desired.
        :param loop: if False, graph is loopless
        :param multiple_edges: if False, graph has no multiple edges.
        :return: None
        """
        self.vertices, self.edges = [], []
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        for i in range(num_vertices):
            v = Vertex(rand.randint(0, num_vertices), rand.randint(0, num_vertices), i)
            self.vertices.append(v)
        for i in range(num_edges):
            v1 = rand.choice(self.vertices)
            if loop and multiple_edges:
                v2 = rand.choice(self.vertices)
            elif loop and not multiple_edges:
                ok_vertices = list(set(self.vertices) - set(v1.neighbors)) + [v1]
                v2 = rand.choice(ok_vertices)
            elif not loop and multiple_edges:
                v2 = rand.choice(list(set(self.vertices) - set([v1])))
            else:
                v2 = rand.choice(list(set(self.vertices) - set(v1.neighbors)))
            self.edges.append(Edge(v1, v2))
            v1.neighbors.append(v2)
            v2.neighbors.append(v1)


class Vertex:
    """
    Object representing a vertex in a graph. It contains a identity to be recognized and a position in a euclidean
    plan (x, y) as well as a list of vertex neighbors.
    """

    def __init__(self, x, y, id):
        self.id = id
        self.x = x
        self.y = y
        self.neighbors = []

    def __repr__(self):
        return f'<id={self.id}-({self.x}, {self.y})>'


class Edge:
    """
    Object representing an edge in a graph. It contains two endpoints which are two vertices.
    """

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def __repr__(self):
        return f'{self.v1}--{self.v2}'


if __name__ == '__main__':
    pathname = 'C:/Johana/Theorie des graphes/GraphIT-master/GraphIT-master/resources/bipartite1.dat'
    g = Graph()
    g.read_dat(pathname)

    # g.random_init(10, 15)

    g.export2tex('C:/Johana/Theorie des graphes/GraphIT-master/GraphIT-master/resources/ouputbipartite1.tex')
