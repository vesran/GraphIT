# GraphIT

This is a project assignment for the Graph Theory course 
holds by A. Rossi at University Paris-Dauphine.

## Prerequisites

Python 3.x

No package have to be installed.

## Usage

Two features has been implemented :
* Extracting a bipartite subgraph from a graph in a 
````file.dat```` file.
* Checking whether a given integer sequence is graphic or not.

Download the project and, on command line, go inside the 
project folder. You should be at the same level than the 
```project.py``` file.

### Extract a bipartite subgraph

This feature illustrates the following theorem : 
given a loopless graph G, then G has a bipartite subgraph with 
at least **e(G)/2 edges**. The algorithm creates two 
groups X and Y of vertices from G and sends, at each iteration, 
the best vertex from one of the group to the other one to 
increase the number of edges linking X and Y until the bound 
is reached.

Extract a bipartite subgraph from a graph in a file, run :
    
    python project.py -b inputfile.dat,outputfile.dat 
or

    python project.py -b inputfile.dat,outputfile.dat -v
    
In a Python file :

```python
from graphit.induced_bipartite_subgraph import export2tex_bipartite_subgraph
pathname = './claw.dat'
export2tex_bipartite_subgraph(pathname, dest_name='./out.tex', verbose=True)
```
It writes a new file under the given output filename containg 
Latex code to draw the graph.

### Graphic sequence

We can check if a given sequence of integers is a graphic 
sequence (ie each integer represents a unique vertex degree in some 
graph) by taking the maximum **a** of the sequence and subtract 
1 to the **a** highest integer of the sequence without **a**. 
Iterating like so will lead us to a sequence of 0 if it is 
graphic or with negative integers if it is not. 

Check if an integer sequence in a file is a graphic sequence, run :
    
    python project.py -g myfile.dat
or

    python project.py -g myfile.dat -v
    
Check if an integer sequence is a graphic sequence (no file), run :
    
    python project.py -s 2,1,1,0
or
    
    python project.py -s 2,1,1,0 -v
    
Note the your sequence **must NOT contains spaces around commas**.

In a Python file :

```python
from graphit.graphic_sequence import print_is_graphic_sequence
pathname = './sequence.txt'
print_is_graphic_sequence(pathname, verbose=True)

# Equivalently
print_is_graphic_sequence([8, 5, 4, 3, 3, 1, 1, 1], verbose=True)
```

It only displays a message telling whether the sequence is 
graphic or not, like :

    The sequence is graphic.

For help, run :

    python project.py -h

## Files format

To extract bipartite subgraph, the file format is the same 
as described in the project's instructions.

For graphic sequences, each file contains one integer 
at each lines without commas nor any other characters.
If the sequence to check is ```8, 5, 4, 4, 3, 1, 1, 1, 0```, 
the file must look like :
```
8
5
4
4
3
1
1
1
0
```

## Architecture

The ```graphit``` package contains everything. The project 
is divided into 3 files.

```graphcore.py``` contains all objects relative to graphs.
Objects defined are :
* ```Graph```: contains a list of edges and vertices. It is undirected.
* ```Edge```: contains two vertices. It is undirected. 
* ```Vertex```: contains an identity, position (x, y) and its neighbors if any.

```induced_bipartite_suubgraph.py``` contains functions to 
extract a bipartite subgraph from a given graph. The main 
function to call is ```def export2tex_bipartite_subgraph(pathname, dest_name='./out.tex', verbose=False)```
which write a ```.tex``` file containing the initial graph 
and the bipartite subgraph in red.

```graphic_sequence.py``` contains functions check whether 
a sequence of integers is graphic or not. The main function is 
```print_is_graphic_sequence(sequence_or_file, verbose=False)```
which displays a message on command line telling if the sequence is
graphic or not.

## Authors

* **Johana Abizmil** - [link](https://github.com/Johanabiz)
* **Yves Tran** - [link](https://github.com/vesran)

