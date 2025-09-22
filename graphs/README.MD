# Graph Data Structure Practice

This repository contains exercises and practice implementations for graph data structures in Python.

---

## Input File Format

Your graph input file must follow the structure below:

`
*vertices 8
1 A
2 B
3 C
4 D
5 E
6 F
7 G
8 H
*edges
8 3 1
8 4 5
8 5 6
3 6 3
3 4 1
3 7 1
5 1 1
4 2 1
`

### Vertices Section
- Starts with `*vertices <number_of_vertices>`
- Each line after represents a vertex with two values:
  1. **Vertex index** – a unique integer identifier starting from 1
  2. **Label/Placeholder** – a string representing the vertex

Example:

1 A
2 B
3 C
...

### Edges Section
- Starts with `*edges`
- Each line represents an edge with three values:
  1. **Start vertex index** – the source of the edge
  2. **End vertex index** – the destination of the edge
  3. **Weight** – numeric value representing cost, distance, or capacity

Example:

8 3 1 # Edge from vertex 8 to vertex 3 with weight 1
3 4 1 # Edge from vertex 3 to vertex 4 with weight 1

> Note: Your program can handle both directed and undirected graphs depending on how edges are processed.

---

## Usage

1. Prepare your input file following the format above.
2. Run your graph script, passing the file as an argument:

```bash

python3 graph_program.py input_file.txt

```

3. At some algorithms you'll need to specify a start vertice (e.g.. Dijkstra):

```bash

python3 graph_program.py input_file.txt 5

```

## Setting Up the Environment

It is recommended to use a **virtual environment** to keep dependencies isolated:

1. Create a virtual environment:

```bash

python3 -m venv venv

```
# Activate the environment

Linux / macOS:

```bash

source venv/bin/activate

```
Windows (PowerShell):

```bash
venv\Scripts\Activate.ps1
```