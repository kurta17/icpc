"""
Comprehensive Graph Algorithms Implementation
==============================================
This file contains implementations of common graph algorithms.
"""

from collections import defaultdict, deque
import heapq


# ============================================================================
# 1. COUNTING CONNECTED COMPONENTS
# ============================================================================

def count_connected_components_dfs(n, edges):
    """
    Count connected components using DFS (iterative with stack)
    
    Args:
        n: number of nodes (1-indexed)
        edges: list of tuples [(u, v), ...]
    
    Returns:
        int: number of connected components
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    count = 0
    
    def dfs(start):
        stack = [start]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            count += 1
    
    return count


def count_connected_components_bfs(n, edges):
    """
    Count connected components using BFS (with queue)
    
    Args:
        n: number of nodes (1-indexed)
        edges: list of tuples [(u, v), ...]
    
    Returns:
        int: number of connected components
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    count = 0
    
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
    
    for i in range(1, n + 1):
        if not visited[i]:
            bfs(i)
            count += 1
    
    return count


# ============================================================================
# 2. SHORTEST PATH ALGORITHMS
# ============================================================================

def shortest_path_bfs(n, edges, start, end):
    """
    Find shortest path in unweighted graph using BFS
    
    Args:
        n: number of nodes (1-indexed)
        edges: list of tuples [(u, v), ...]
        start: starting node
        end: ending node
    
    Returns:
        tuple: (distance, path) or (float('inf'), []) if no path exists
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    distance = [float('inf')] * (n + 1)
    
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    
    while queue:
        node = queue.popleft()
        
        if node == end:
            # Reconstruct path
            path = []
            current = end
            while current != -1:
                path.append(current)
                current = parent[current]
            return distance[end], path[::-1]
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                parent[neighbor] = node
                queue.append(neighbor)
    
    return float('inf'), []


def dijkstra(n, edges, start):
    """
    Dijkstra's algorithm for shortest path in weighted graph
    
    Args:
        n: number of nodes (1-indexed)
        edges: list of tuples [(u, v, weight), ...]
        start: starting node
    
    Returns:
        dict: {node: (distance, path)}
    """
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    parent = [-1] * (n + 1)
    visited = [False] * (n + 1)
    
    # Min heap: (distance, node)
    heap = [(0, start)]
    
    while heap:
        d, node = heapq.heappop(heap)
        
        if visited[node]:
            continue
        
        visited[node] = True
        
        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))
    
    # Build result with paths
    result = {}
    for i in range(1, n + 1):
        if dist[i] != float('inf'):
            path = []
            current = i
            while current != -1:
                path.append(current)
                current = parent[current]
            result[i] = (dist[i], path[::-1])
    
    return result


def bellman_ford(n, edges, start):
    """
    Bellman-Ford algorithm (handles negative weights)
    
    Args:
        n: number of nodes (1-indexed)
        edges: list of tuples [(u, v, weight), ...]
        start: starting node
    
    Returns:
        tuple: (distances, has_negative_cycle)
        distances is a list where distances[i] = shortest distance from start to i
    """
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    
    # Relax edges n-1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
            if dist[v] != float('inf') and dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
    
    # Check for negative cycle
    has_negative_cycle = False
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            has_negative_cycle = True
            break
        if dist[v] != float('inf') and dist[v] + w < dist[u]:
            has_negative_cycle = True
            break
    
    return dist, has_negative_cycle


# ============================================================================
# 3. CONNECTIVITY CHECKS
# ============================================================================

def is_connected(n, edges):
    """
    Check if graph is connected
    
    Args:
        n: number of nodes (1-indexed)
        edges: list of tuples [(u, v), ...]
    
    Returns:
        bool: True if graph is connected
    """
    if n <= 1:
        return True
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    
    # BFS from node 1
    queue = deque([1])
    visited[1] = True
    count = 1
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                count += 1
                queue.append(neighbor)
    
    return count == n


def find_bridges(n, edges):
    """
    Find bridges (critical edges) in a graph
    
    Args:
        n: number of nodes (1-indexed)
        edges: list of tuples [(u, v), ...]
    
    Returns:
        list: list of bridge edges [(u, v), ...]
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    disc = [0] * (n + 1)  # Discovery time
    low = [0] * (n + 1)   # Lowest reachable
    parent = [-1] * (n + 1)
    bridges = []
    time = [0]
    
    def dfs(u):
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1
        
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                
                # If lowest reachable from v is higher than discovery of u
                if low[v] > disc[u]:
                    bridges.append((min(u, v), max(u, v)))
            
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    
    return bridges


# ============================================================================
# 4. PATHFINDING ALGORITHMS
# ============================================================================

def find_all_paths_dfs(n, edges, start, end):
    """
    Find all paths from start to end using DFS
    
    Args:
        n: number of nodes (1-indexed)
        edges: list of tuples [(u, v), ...]
        start: starting node
        end: ending node
    
    Returns:
        list: list of all paths [[node1, node2, ...], ...]
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    all_paths = []
    
    def dfs(node, path, visited):
        if node == end:
            all_paths.append(path[:])
            return
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                dfs(neighbor, path, visited)
                path.pop()
                visited.remove(neighbor)
    
    visited = {start}
    dfs(start, [start], visited)
    
    return all_paths


def has_path(n, edges, start, end):
    """
    Check if there exists a path from start to end
    
    Args:
        n: number of nodes (1-indexed)
        edges: list of tuples [(u, v), ...]
        start: starting node
        end: ending node
    
    Returns:
        bool: True if path exists
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        if node == end:
            return True
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return False


# ============================================================================
# 5. CYCLE DETECTION
# ============================================================================

def has_cycle_undirected(n, edges):
    """
    Detect cycle in undirected graph
    
    Args:
        n: number of nodes (1-indexed)
        edges: list of tuples [(u, v), ...]
    
    Returns:
        bool: True if cycle exists
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    
    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    
    for i in range(1, n + 1):
        if not visited[i]:
            if dfs(i, -1):
                return True
    
    return False


def has_cycle_directed(n, edges):
    """
    Detect cycle in directed graph
    
    Args:
        n: number of nodes (1-indexed)
        edges: list of directed tuples [(u, v), ...] (u -> v)
    
    Returns:
        bool: True if cycle exists
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * (n + 1)
    
    def dfs(node):
        color[node] = GRAY
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK
        return False
    
    for i in range(1, n + 1):
        if color[i] == WHITE:
            if dfs(i):
                return True
    
    return False


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("GRAPH ALGORITHMS EXAMPLES")
    print("=" * 60)
    
    # Example 1: Connected Components
    print("\n1. CONNECTED COMPONENTS")
    print("-" * 60)
    n = 7
    edges = [(1, 2), (2, 3), (4, 5), (6, 7)]
    print(f"Nodes: {n}, Edges: {edges}")
    print(f"Connected components (DFS): {count_connected_components_dfs(n, edges)}")
    print(f"Connected components (BFS): {count_connected_components_bfs(n, edges)}")
    
    # Example 2: Shortest Path (Unweighted)
    print("\n2. SHORTEST PATH (Unweighted)")
    print("-" * 60)
    n = 6
    edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (5, 6)]
    start, end = 1, 6
    dist, path = shortest_path_bfs(n, edges, start, end)
    print(f"Nodes: {n}, Edges: {edges}")
    print(f"Shortest path from {start} to {end}: {path}")
    print(f"Distance: {dist}")
    
    # Example 3: Dijkstra (Weighted)
    print("\n3. DIJKSTRA'S ALGORITHM (Weighted)")
    print("-" * 60)
    n = 5
    weighted_edges = [(1, 2, 4), (1, 3, 1), (3, 2, 2), (2, 4, 5), (3, 4, 8), (4, 5, 3)]
    start = 1
    result = dijkstra(n, weighted_edges, start)
    print(f"Nodes: {n}, Weighted Edges: {weighted_edges}")
    print(f"Shortest paths from node {start}:")
    for node, (dist, path) in sorted(result.items()):
        print(f"  To {node}: distance={dist}, path={path}")
    
    # Example 4: Connectivity
    print("\n4. CONNECTIVITY CHECK")
    print("-" * 60)
    n = 4
    edges = [(1, 2), (2, 3), (3, 4)]
    print(f"Nodes: {n}, Edges: {edges}")
    print(f"Is connected: {is_connected(n, edges)}")
    
    # Example 5: Cycle Detection
    print("\n5. CYCLE DETECTION")
    print("-" * 60)
    n = 4
    edges_with_cycle = [(1, 2), (2, 3), (3, 4), (4, 1)]
    edges_without_cycle = [(1, 2), (2, 3), (3, 4)]
    print(f"Nodes: {n}, Edges: {edges_with_cycle}")
    print(f"Has cycle: {has_cycle_undirected(n, edges_with_cycle)}")
    print(f"Edges: {edges_without_cycle}")
    print(f"Has cycle: {has_cycle_undirected(n, edges_without_cycle)}")
    
    # Example 6: All Paths
    print("\n6. FIND ALL PATHS")
    print("-" * 60)
    n = 4
    edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
    start, end = 1, 4
    all_paths = find_all_paths_dfs(n, edges, start, end)
    print(f"Nodes: {n}, Edges: {edges}")
    print(f"All paths from {start} to {end}:")
    for i, path in enumerate(all_paths, 1):
        print(f"  Path {i}: {' -> '.join(map(str, path))}")
    
    print("\n" + "=" * 60)
