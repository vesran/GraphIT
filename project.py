"""
This file holds all the necessary imports for the project.
It is the only file to execute.
The graphit package, resources folder, eventually test package and this file
should all be in the same folder.
"""

import sys
import getopt

from graphit.graphic_sequence import print_is_graphic_sequence
from graphit.induced_bipartite_subgraph import export2tex_bipartite_subgraph


def usage():
    print("""
    It is RECOMMENDED to add option -v to display the actions done during the program.
    -- Check if a graph in a file is bipartite, run :
    
    \tpython project.py -b inputfile.dat,outputfile.dat 
    \tor
    \tpython project.py -b inputfile.dat,outputfile.dat -v
    
    -- Check if an integer sequence in a file is a graphic sequence, run :
    
    \tpython project.py -g myfile.dat
    \tor
    \tpython project.py -g myfile.dat -v
    
    -- Check if an integer sequence is a graphic sequence (no file), run :
    
    \tpython project.py -s 2,1,1
    \tor
    \tpython project.py -s 2,1,1 -v
    
    \tNote the your sequence must NOT contains spaces around commas.
    
    """)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "g:s:b:vh", ["graphic", "sequence=", "bipartite=", "verbose", "help"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    seq, bi, verbose = False, False, False
    filename_or_seq = []
    dest = './out_bipartite.tex'
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()

        elif opt in ('-g', '--graphic'):
            seq = True
            filename_or_seq = arg

        elif opt in ('-s', '--sequence'):
            seq = True
            filename_or_seq = [int(i) for i in arg.split(',')]

        elif opt in ('-b', '--bipartite'):
            bi = True
            if arg.__contains__(','):
                files = arg.split(',')
                filename_or_seq = files[0]
                dest = files[1]
            else:
                filename_or_seq = arg

        elif opt in ('-v', '--verbose'):
            verbose = True

    print_is_graphic_sequence(filename_or_seq, verbose=verbose) if seq else 0
    export2tex_bipartite_subgraph(filename_or_seq, dest_name=dest, verbose=verbose) if bi else 0


if __name__ == '__main__':
    main(sys.argv[1:])
