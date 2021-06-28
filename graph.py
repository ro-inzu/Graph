class Graph(object):
    def __init__(self, graph_dict):
        if graph_dict is None:
            graph_dict = []
        self.graph_dict = graph_dict

    # Get the keys of the dictionary
    def get_vertices(self):
        return list(self.graph_dict.keys())

    def edges(self):
        return self.find_edges()

    # Find the distinct list of edges
    def find_edges(self):
        edge_name = []
        for vertex in self.graph_dict:
            for next_vertex in self.graph_dict[vertex]:
                if {next_vertex, vertex} not in edge_name:
                    edge_name.append({vertex, next_vertex})
        return edge_name

    def depth_first_search(self, visited: list, graph: dict, node: str):
        if not graph:
            return

        if node not in visited:
            print(node, end=' ')
            visited.append(node)

            for neighbour in graph[node]:
                self.depth_first_search(visited, graph, neighbour)

    @staticmethod
    def breadth_first_search(visited: list, graph: dict, node: str, queue: list):
        if not graph:
            return

        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
