import matplotlib.pyplot as plt


def get_graph_data():

    num_nodes = int(input("Enter the number of nodes: "))

    edges = []

    for i in range(num_nodes):

        x = float(input(f"Enter x-coordinate of node {i+1}: "))

        y = float(input(f"Enter y-coordinate of node {i+1}: "))

        edges.append((x, y))


    num_edges = int(input("Enter the number of edges: "))

    connections = []

    for i in range(num_edges):

        node1 = int(input(f"Enter the index of the first node for edge {i+1} (1-indexed): ")) - 1

        node2 = int(input(f"Enter the index of the second node for edge {i+1} (1-indexed): ")) - 1

        connections.append((node1, node2))


    return edges, connections


def plot_graph(edges, connections):

    plt.figure(figsize=(8, 8))

    for edge in edges:

        plt.scatter(edge[0], edge[1], c='b', marker='o')

    for connection in connections:

        node1 = connection[0] - 1

        node2 = connection[1] - 1

        if 0 <= node1 < len(edges) and 0 <= node2 < len(edges):

            plt.plot([edges[node1][0], edges[node2][0]], [edges[node1][1], edges[node2][1]], c='b')

        else:

            print(f"Warning: Edge {connection} is out of range. Skipping...")


    plt.xlabel('X')

    plt.ylabel('Y')

    plt.title('Graph')

    plt.grid(True)

    plt.show()


def main():

    edges, connections = get_graph_data()

    plot_graph(edges, connections)


if __name__ == "__main__":

    main()