import networkx as nx
from visualization import draw_tree_step

def prufer_to_tree_animated(prufer_sequence):
    m = len(prufer_sequence)
    n = m + 2
    degree = [1] * n

    for vertex in prufer_sequence:
        degree[vertex - 1] += 1

    leaf = min([i for i in range(n) if degree[i] == 1])
    tree = []
    G = nx.Graph()

    for vertex in prufer_sequence:
        tree.append((leaf + 1, vertex))
        G.add_edge(leaf + 1, vertex)

        degree[leaf] -= 1
        degree[vertex - 1] -= 1

        if degree[vertex - 1] == 1 and vertex - 1 < leaf:
            leaf = vertex - 1
        else:
            leaf = min([i for i in range(n) if degree[i] == 1])

        draw_tree_step(G)

    remaining = [i for i in range(n) if degree[i] == 1]
    tree.append((remaining[0] + 1, remaining[1] + 1))
    G.add_edge(remaining[0] + 1, remaining[1] + 1)

    draw_tree_step(G)
    return tree
