from Setup import Node, Colour
def Build_input(nodes):
    for i in range(1,16):
        n = Node(i)
        nodes.append(n)
    return nodes


def Set_up_forbidden_nodes(nodes, id, restrictions):
    nodes[id-1].neighbors = {i for i in restrictions}


def Build_Graph():
    nodes = []
    nodes = Build_input(nodes)
    Set_up_forbidden_nodes(nodes, 1, [5, 6])
    Set_up_forbidden_nodes(nodes, 2, [3, 5])
    Set_up_forbidden_nodes(nodes, 3, [2, 6, 7])
    Set_up_forbidden_nodes(nodes, 4, [7])
    Set_up_forbidden_nodes(nodes, 5, [1, 2, 6, 8, 9])
    Set_up_forbidden_nodes(nodes, 6, [1, 3, 5, 9, 10])
    Set_up_forbidden_nodes(nodes, 7, [3, 4, 10, 11, 12])
    Set_up_forbidden_nodes(nodes, 8, [5])
    Set_up_forbidden_nodes(nodes, 9, [5, 6, 10])
    Set_up_forbidden_nodes(nodes, 10, [6, 7, 9])
    Set_up_forbidden_nodes(nodes, 11, [7])
    Set_up_forbidden_nodes(nodes, 12, [7, 14])
    Set_up_forbidden_nodes(nodes, 13, [14, 15])
    Set_up_forbidden_nodes(nodes, 14, [12, 13, 15])
    Set_up_forbidden_nodes(nodes, 15, [13, 14])
    return nodes

# for node in nodes:
#     print(node)
