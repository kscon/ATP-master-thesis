import os
import itertools
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


# ten layout generator
#  mapping nodes to position in ten graph
def ten_layout_generator(G: nx.DiGraph):
    layers = {}
    for v in G.nodes():
        layer = G.nodes[v]['layer']
        layers[layer] = layers.get(layer, []) + [v]
    length = len(layers)
    layers = dict(sorted(layers.items())) # sorting by layer value to prevent positioning side effects
    pos = [np.array([i, 3 * j]) for i in range(0, length) for j in range(0, len(layers[0]))]
    pos_dict = dict(zip(np.array(list(layers.values())).reshape(-1), pos))
    return pos_dict


def draw_ten(G: nx.DiGraph, data, draw_aux=0, start_time=0, end_time=999, new_train_path=[]):
    assert 0 <= start_time <= end_time <= 999
    if (start_time - end_time > 35):
        print('Warning: printing more than 35 timesteps may influence readability.')
    print('plotting...', end=' ')
    node_list = [v for v in G.nodes() if start_time <= int(v.split('_')[-1]) <= end_time]

    plt.figure(figsize=(19.20, 10.80))

    if draw_aux == 1:
        draw_ten_before(G, node_list)
    else:
        draw_ten_after(G, node_list, new_train_path)

    plt.text(-1, -4, "time: " + str(start_time) + "-" + str(end_time))
    # plt.show()
    filename = data['filepath'].split('/')[-1]
    folder = 'output/' + data['filepath'] + '/'
    full_file_string = 'ten_' + filename + '_' + str(data['iteration_counter'])

    if not os.path.exists(folder):
        os.makedirs(folder)

    if draw_aux:
        plt.savefig(folder + full_file_string + '_before' + '.png', format='png')
        plt.savefig(folder + full_file_string + '_before' + '.pdf', format='pdf')
    else:
        plt.savefig(folder + full_file_string + '_after' + '.png', format='png')
        plt.savefig(folder + full_file_string + '_after' + '.pdf', format='pdf')
    plt.close()
    print('done!')


def draw_ten_before(G: nx.DiGraph, node_list):
    pos = ten_layout_generator(G)

    nx.draw_networkx_nodes(G, nodelist=node_list, pos=pos, node_size=100)
    nx.draw_networkx_labels(G, pos=pos, labels={n:n for n in node_list}, font_size=6)

    aux_edges = [(u, v) for (u, v, a) in G.edges.data('aux') if a is not None and u in node_list and v in node_list] \
                + [(u, v) for (u, v, f) in G.edges.data('flow') if f > 0 and u in node_list and v in node_list]
    edges = [(u, v) for (u, v) in G.edges if (u, v) not in aux_edges and u in node_list and v in node_list]
    nx.draw_networkx_edges(G, pos=pos, edgelist=edges, edge_color='k')
    nx.draw_networkx_edges(G, pos=pos, edgelist=aux_edges, edge_color='r')


def draw_ten_after(G: nx.DiGraph, node_list, new_train_path):
    pos = ten_layout_generator(G)
    nx.draw_networkx_nodes(G, nodelist=node_list, pos=pos, node_size=100)
    nx.draw_networkx_labels(G, pos=pos, labels={n:n for n in node_list}, font_size=6)

    edges = [(u, v) for (u, v, aux) in G.edges.data('aux') if aux != 1 and u in node_list and v in node_list]
    new_train_edges = [(u,v) for (u,v) in itertools.pairwise(new_train_path) if u in node_list and v in node_list]
    nx.draw_networkx_edges(G, pos=pos, edgelist=edges, edge_color='k')
    nx.draw_networkx_edges(G, pos=pos, edgelist=new_train_edges, edge_color='blue', width=2.0)
