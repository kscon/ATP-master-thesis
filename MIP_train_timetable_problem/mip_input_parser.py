from importlib.machinery import SourceFileLoader
import networkx as nx


# todo: make use of network utils
# input data gets prioritized
def prepare_input(filepath, input_data):
    data = None
    if input_data is not None:
        data = input_data
    elif filepath is not None:
        datafile = SourceFileLoader(filepath, "common_data/networks/" + filepath + ".py").load_module()
        data = datafile.data

    return data


def construct_network(data):
    block_graph_helper = nx.DiGraph()
    for n in data['nodes']:
        block_graph_helper.add_node(str(n), element_type=data['nodes_labels'][n])
    for e in data['edges']:
        block_graph_helper.add_edge(str(e[0]), str(e[1]), capacity=data['capacities'][e])

    # add waiting blocks
    for n in data['nodes']:
        if block_graph_helper.nodes[str(n)]['element_type'] == 'station' or \
                block_graph_helper.nodes[str(n)]['element_type'] == 'switch':
            new_node = str(n) + '#'
            block_graph_helper.add_node(str(n) + '#', element_type='waiting')
            node, neighbour, capacity = list(block_graph_helper.out_edges(str(n), 'capacity'))[0]
            block_graph_helper.remove_edge(node, neighbour)
            block_graph_helper.add_edge(str(n), new_node, capacity=capacity)
            block_graph_helper.add_edge(new_node, neighbour, capacity=capacity)

    # get layers (without capacity)
    current_node = data['start_node']
    layers = []
    edge_list = []
    while 1:
        if current_node == data['end_node']:
            layers.append([current_node])
            break
        layers.append([current_node])
        edge_list.append(list(block_graph_helper.out_edges(current_node, data='capacity'))[0])
        current_node = list(block_graph_helper.successors(current_node))[0]

    # add capacity
    for (u, v, c) in edge_list:
        u_list = [u_x for u_x in nx.nodes(block_graph_helper) if str(u) == str(u_x).split('_')[0]]
        v_list = [v_x for v_x in nx.nodes(block_graph_helper) if str(v) == str(v_x).split('_')[0]]

        # check if edge already has as many end nodes as the capacity dictates
        i = 1
        while len(v_list) != c:
            v_list.append(str(v_list[0]) + '_' + str(i))
            i += 1
        block_graph_helper.remove_edge(u, v)

        for p in range(max(len(u_list), len(v_list))):  # opening switches
            block_graph_helper.add_edge(u_list[p % len(u_list)], v_list[p % len(v_list)])

    # extend layers with capacity nodes
    for l in layers:
        assert len(l) == 1
        current_node = l[0]
        l.extend([nn for nn in nx.nodes(block_graph_helper) if
                  current_node != nn and str(current_node) == str(nn).split('_')[0]])

    # fetch data from constructed network necessary for the MIP
    data['edges'] = list(block_graph_helper.edges())
    data['layers'] = layers
    data['blocks'] = sorted(nx.nodes(block_graph_helper))
    data['stations'] = [str(a) for a in data['nodes_labels'].keys() if data['nodes_labels'][a] == 'station']
    data['station_blocks'] = {i: [p for l in layers for p in l if str(i) == str(p).split('_')[0]] for i in
                              data['stations']}

    return data


# construct arrival and departure times
def construct_train_data(data, operating_mode):
    A = {}
    D = {}
    M = {}

    L = ['existing_trains', 'new_trains_traveltimes']
    if operating_mode:
        L = ['existing_trains']

    # arrival and departure times for trains
    for s in L:
        for r in data[s]:
            for station in data[s][r]['arrival_times']:
                if station == data['end_node']:
                    A[r, data['end_node']] = data[s][r]['arrival_times'][data['end_node']]
                else:
                    for block_name in data['station_blocks'][station]:
                        A[r, block_name] = data[s][r]['arrival_times'][station]
            for station in data[s][r]['departure_times']:
                for block_name in data['station_blocks'][station]:
                    D[r, block_name] = data[s][r]['departure_times'][station]

    # map minimum traveltimes to blocks
    for s in L:
        for r in data[s]:
            for b in data['blocks']:
                M[r, b] = 0
            for (sb, eb) in data[s][r]['traveltimes']:
                if sb == eb:
                    block_list = [b for b in data['blocks'] if b.split('_')[0] == sb]
                    for b in block_list:
                        M[r, b] = data[s][r]['traveltimes'][(sb, eb)]
                else:
                    block_list = [b for b in data['blocks'] if '#' in b and b.split('#')[0] == sb]
                    if len(block_list) != 0:
                        for b in block_list:
                            M[r, b] = data[s][r]['traveltimes'][(sb, eb)]
                    else:
                        block_list = [b for b in data['blocks'] if b.split('_')[0] == sb]
                        for b in block_list:
                            M[r, b] = data[s][r]['traveltimes'][(sb, eb)]

    data['arrival_times'] = A
    data['departure_times'] = D
    data['minimum_traveltimes'] = M
    if operating_mode:
        data['trains'] = list(data['existing_trains'].keys())
    else:
        data['trains'] = list(data['existing_trains'].keys()) + list(data['new_trains_traveltimes'].keys())

    return data


# unparsed_data: optional, but can also be used
def parse_input(filepath, operating_mode, unparsed_data=None):
    data = prepare_input(filepath, unparsed_data)
    data = construct_network(data)
    data = construct_train_data(data, operating_mode)

    return data

# parse_input('4_blocks_1_stations_2_trains_48_time')
