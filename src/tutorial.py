#1
# Contoh penggunaan
edges = [(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)]
graph = create_graph(edges)

# Menampilkan informasi tentang graf
print("Nodes:", graph.nodes())
print("Edges:", graph.edges())
 
 #2
 # Contoh penggunaan
edges = [(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)]
graph = nx.Graph()
graph.add_edges_from(edges)

# Menghitung derajat dari simpul tertentu
node = 2
degree = get_degree(graph, node)
print(f"Derajat simpul {node}: {degree}")

#3
# Contoh penggunaan
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
graph = nx.Graph()
graph.add_edges_from(edges)

# Traversal DFS mulai dari simpul 1
start_node = 1
dfs_result = dfs_traversal(graph, start_node)
print(f"DFS Traversal dari simpul {start_node}: {dfs_result}")

# 4
# Contoh penggunaan
if __name__ == "__main__":
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
    graph = nx.Graph()
    graph.add_edges_from(edges)

    # Traversal BFS mulai dari simpul 1
    start_node = 1
    bfs_result = bfs_traversal(graph, start_node)
    print(f"BFS Traversal dari simpul {start_node}: {bfs_result}")

# 5
# Contoh penggunaan
if __name__ == "__main__":
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 6), (5, 7)]
    graph = nx.Graph()
    graph.add_edges_from(edges)

    # Cari jalur terpendek dari simpul 1 ke 7
    source_node = 1
    target_node = 7
    shortest_path_result = find_shortest_path(graph, source_node, target_node)
    print(f"Jalur terpendek dari {source_node} ke {target_node}: {shortest_path_result}")

# 6
# Contoh penggunaan
if __name__ == "__main__":
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 6), (5, 7)]
    graph = nx.Graph()
    graph.add_edges_from(edges)

    # Visualisasikan graf
    visualize_graph(graph)
