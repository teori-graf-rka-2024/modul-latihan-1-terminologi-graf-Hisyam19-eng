import networkx as nx

def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    G = nx.Graph()  # Membuat objek graf kosong
    G.add_edges_from(edges)  # Menambahkan daftar sisi ke dalam graf
    return G

# 2
def get_degree(G: nx.Graph, node: int) -> int:
    """
    Menghitung derajat dari simpul tertentu dalam graf.

    Parameters:
        G (nx.Graph): Graf yang telah dibuat.
        node (int): Simpul yang ingin dihitung derajatnya.

    Returns:
        int: Derajat dari simpul tersebut.
    """
    if node not in G:
        raise ValueError(f"Simpul {node} tidak ada dalam graf.")
    
    return G.degree(node)

# 3
def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    """
    Melakukan pencarian secara Depth-First Search (DFS) mulai dari simpul tertentu.

    Parameters:
        G (nx.Graph): Graf yang telah dibuat.
        start (int): Simpul awal.

    Returns:
        list[int]: Urutan traversal berdasarkan DFS.
    """
    visited = []  # List untuk menyimpan simpul yang telah dikunjungi
    stack = [start]  # Menggunakan stack untuk DFS

    while stack:
        node = stack.pop()  # Ambil simpul terakhir dari stack
        if node not in visited:
            visited.append(node)  # Tandai simpul sebagai dikunjungi
            neighbors = list(G.neighbors(node))
            stack.extend(reversed(neighbors))  # Tambahkan tetangga ke stack
    
    return visited
# 4
from typing import List

def bfs_traversal(G: nx.Graph, start: int) -> List[int]:
    """
    Melakukan pencarian secara Breadth-First Search (BFS) mulai dari simpul tertentu.

    Parameters:
        G (nx.Graph): Graf yang telah dibuat.
        start (int): Simpul awal.

    Returns:
        List[int]: Urutan traversal berdasarkan BFS.
    """
    visited = []  # List untuk menyimpan simpul yang telah dikunjungi
    queue = [start]  # Menggunakan queue untuk BFS

    while queue:
        node = queue.pop(0)  # Ambil simpul pertama dari queue
        if node not in visited:
            visited.append(node)  # Tandai simpul sebagai dikunjungi
            neighbors = list(G.neighbors(node))
            queue.extend(neighbors)  # Tambahkan tetangga ke queue
    
    return visited
# 5
def find_shortest_path(G: nx.Graph, source: int, target: int) -> List[int]:
    """
    Mencari jalur terpendek antara dua simpul dalam graf.

    Parameters:
        G (nx.Graph): Graf yang telah dibuat.
        source (int): Simpul awal.
        target (int): Simpul tujuan.

    Returns:
        List[int]: Urutan simpul yang membentuk jalur terpendek dari source ke target.
    """
    try:
        shortest_path = nx.shortest_path(G, source=source, target=target, method='dijkstra')
        return shortest_path
    except nx.NetworkXNoPath:
        return []  # Jika tidak ada jalur antara source dan target
# 6
import matplotlib.pyplot as plt

def visualize_graph(G: nx.Graph) -> None:
    """
    Memvisualisasikan graf menggunakan matplotlib.

    Parameters:
        G (nx.Graph): Graf yang telah dibuat.

    Output:
        - Menampilkan visualisasi graf.
        - Menyimpan hasil visualisasi ke dalam file 'graph_visualization.png'.
    """
    plt.figure(figsize=(8, 6))  # Mengatur ukuran gambar
    pos = nx.spring_layout(G)   # Menentukan tata letak node
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=12)
    
    # Simpan visualisasi ke dalam file
    plt.savefig("graph_visualization.png")
    plt.show()  # Menampilkan graf
