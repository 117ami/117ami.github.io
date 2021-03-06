from graphviz import Digraph
'''More examples on how to draw graph can be found here:
https://graphviz.readthedocs.io/en/stable/examples.html#process-py
'''

f = Digraph(node_attr={
    'color': 'lightblue2',
    'style': 'filled'
},
            filename='dag.gv')

# use rankdir = 'LR' to show nodes from left to right (default is TB: top-bottom)
f.attr(size='8,5', rankdir='UD')
edges = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 6), (6, 4)]
edges = [(0, 1), (0, 2), (0, 4), (0, 8), (0, 16), (2, 3), (4, 5), (4, 6),
         (6, 7), (8, 9), (8, 10), (10, 11), (8, 12)]

for n in range(13):
    f.node(str(n), str(n))

f.node("16", "16")

for e in edges:
    u, v = str(e[1]), str(e[0])
    f.edge(v, u)

f.view()
f.render('fenwick_tree')
