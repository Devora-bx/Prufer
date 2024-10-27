import networkx as nx
import matplotlib.pyplot as plt

def draw_tree_step(G):
    pos = nx.spring_layout(G)
    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')
    plt.pause(1)
    plt.draw()
