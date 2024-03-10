class Node:
    def __init__(self):
        self.name = ""
        self.distance = 0.0
        self.bootstrap = 0.0
        self.left = 0
        self.right = 0
        self.parent = 0

    def __repr__(self):
        return "node_" + self.name


def declare_new_tree_node(nodes, num_nodes):
    nodes[num_nodes] = Node()
    return (num_nodes, num_nodes + 1)


def scan_name_and_dist(i, l):
    name = ""
    number = ""

    while l[i] != ":" and i < len(l) and l[i] != ")" and l[i] != ";" and l[i] != ",":
        name += l[i]
        i += 1

    if l[i] != ":":
        distance = float(0)
        return (name, distance, i)
    else:
        i += 1

    while str.isdigit(l[i]) or l[i] == "e" or l[i] == "-" or l[i] == ".":
        number += l[i]
        i += 1

    number = float(number)
    return (name, number, i)


def newick_line2nodes(line):
    nodes = {}
    num_nodes = 0
    (N, num_nodes) = declare_new_tree_node(nodes, num_nodes)
    T = R = N

    c = pi = i = 0
    while (line[i]) != ";":
        c = line[i]
        i += 1
        if c == "(":
            (N, num_nodes) = declare_new_tree_node(nodes, num_nodes)
            nodes[N].parent = T

            if nodes[T].right == 0:
                nodes[T].right = N
            elif nodes[T].left == 0:
                nodes[T].left = N
            else:
                nodes[N].right = nodes[T].right
                nodes[nodes[T].right].parent = N

                nodes[N].left = nodes[T].left
                nodes[nodes[T].left].parent = N

                nodes[T].right = N

                (N, num_nodes) = declare_new_tree_node(nodes, num_nodes)

                nodes[T].left = N
                nodes[N].parent = T

            T = N
            lastc = 0

        elif c == ")":
            T = nodes[T].parent
            (nodes[T].name, nodes[T].distance, i) = scan_name_and_dist(i, line)
            if nodes[T].name and nodes[T].name[0]:
                nodes[T].bootstrap = float(nodes[T].name)
                nodes[T].name = ""
            lastc = 0

        elif c == ",":
            T = nodes[T].parent
            lastc += 1
        else:
            (N, num_nodes) = declare_new_tree_node(nodes, num_nodes)
            nodes[N].parent = T

            if nodes[T].right == 0:
                nodes[T].right = N
                nodes[N].left = nodes[T].left
                nodes[nodes[T].left].parent = N


                nodes[N].left = nodes[T].left
                nodes[nodes[T].left].parent = N

                nodes[T].right = N

                (N, num_nodes) = declare_new_tree_node(nodes, num_nodes)
                nodes[T].left = N
                nodes[N].parent = T

            T = N
            i = i - 1

            (nodes[T].name, nodes[T].distance, i) = scan_name_and_dist(i, line)
            lastc = 0

    T = nodes[T].parent

    if nodes[T].right == 0 and nodes[T].left != 0:
        T = nodes[T].left
    elif nodes[T].right != 0 and nodes[T].left == 0:
        T = nodes[T].right

    nodes[T].parent = -1
    # return (nodes, num_nodes)
    return nodes


def newick_file2nodes(newick_file):
    with open(newick_file) as f_newick:
        line = "".join(f_newick.read().splitlines())
    return newick_line2nodes(line)


print(newick_file2nodes('tree_abcdef.dnd'))