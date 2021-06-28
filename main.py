from graph import Graph

# Using a Python dictionary to act as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

graph_obj = Graph(graph)
vertices = graph_obj.get_vertices()
print('vertices: {}'.format(vertices))
print('edges: {}'.format(graph_obj.edges()))

print('Depth first search:')
visited = []  # Set to keep track of visited nodes.
graph_obj.depth_first_search(visited, graph, 'A')

print('\nBreadth first search:')
visited = []  # List to keep track of visited nodes.
queue = []
graph_obj.breadth_first_search(visited, graph, 'A', queue)
