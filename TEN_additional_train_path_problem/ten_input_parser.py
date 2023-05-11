import networkx as nx
from importlib.machinery import SourceFileLoader


def read_input(filepath):
    datafile = SourceFileLoader(filepath, "common_data/networks/" + filepath + ".py").load_module()
    return datafile.data


def parse_input(filepath):
    data = read_input(filepath)

    G = nx.DiGraph()
    for n in data['nodes']:
        G.add_node(n, element_type=data['nodes_labels'][n])
    G.add_edges_from(data['edges'])

    data['graph'] = G

    data['trains'] = list(data['existing_trains'].keys()) + list(data['new_trains_traveltimes'].keys())

    # extract layers
    # data['layers'] = [[node] for node in data['nodes']]
    data['layers'] = []
    for b in data['nodes']:
        data['layers'].append([b])
        if (b, b) in list(data['capacities'].keys()):
            data['layers'].append([b+'#'])

    return data
