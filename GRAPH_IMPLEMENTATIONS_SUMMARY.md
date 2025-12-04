# Graph Problems Found in Your Repository

## Summary of Existing Implementations

### 1. **C. Rumor.py** - Connected Components with DFS
**Location:** `Educational Codeforces Round 33 (Rated for Div. 2)/C. Rumor.py`

**Algorithm:** Finding minimum cost in each connected component using iterative DFS

```python
from collections import defaultdict

n, m = map(int, input().split())
coins = list(map(int, input().split()))
graph = defaultdict(list)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(st, visited):
    stack = [st]
    mc = float('inf')
    while stack:
        node = stack.pop()
        if not visited[node-1]:
            visited[node-1] = True
            mc = min(mc, coins[node-1])
            for neigh in graph[node]:
                if not visited[neigh-1]:
                    stack.append(neigh)
    return mc

visited = [False] * n
ans = 0

for i in range(1, n+1):
    if not visited[i-1]:
        c = dfs(i, visited)
        ans += c

print(ans)
```

**Key Concepts:**
- Undirected graph representation using `defaultdict(list)`
- Iterative DFS using stack
- Connected components traversal
- Finding minimum value in each component

---

### 2. **Hello 2025/d.py** - Path Finding with Weight Tracking
**Location:** `Hello 2025/d.py`

**Algorithm:** Finding k-th largest edge weight on all paths between two nodes

```python
from collections import defaultdict

for _ in range(int(input())):
    n, m, q = map(int, input().split())
    
    graph = defaultdict(list)
    for __ in range(m):
        v, u, w = map(int, input().split())
        graph[v].append((u, w))
        graph[u].append((v, w))

    ans = []
    for __ in range(q):
        start, end, k = map(int, input().split())
        
        stack = [(start, [], set())]
        min_k_weight = float('inf')
        
        while stack:
            node, path_w, visited = stack.pop()
            if node == end:
                path_w.sort(reverse=True)
                if len(path_w) >= k:
                    min_k_weight = min(min_k_weight, path_w[k - 1])
                continue
            
            if node in visited:
                continue
            
            visited.add(node)
            
            for mez, weight in graph[node]:
                if mez not in visited:
                    stack.append((mez, path_w + [weight], visited.copy()))
        
        ans.append(min_k_weight)
    
    print(*ans)
```

**Key Concepts:**
- Weighted graph with adjacency list
- DFS with state tracking (node, path weights, visited set)
- Path enumeration between two nodes
- Finding k-th largest weight on paths

---

### 3. **D. Sakurako's Hobby.py** - Cycle Detection in Permutation
**Location:** `math/D. Sakurako's Hobby.py`

**Algorithm:** Finding cycles in a permutation graph

```python
t = int(input())
for _ in range(t):
    n = int(input())
    b = [0] * (n + 1)
    us = [0] * (n + 1)
    p = [k-1 for k in map(int, input().split())]
    s = input()

    cycle = []
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            cycle.append([i])
            visited[i] = True
            j = p[i]
            while j != i:
                cycle[-1].append(j)
                visited[j] = True
                j = p[j]

    for c in cycle:
        sz = sum(s[i] == '0' for i in c)
        for i in c:
            b[i] = sz

    print(" ".join(map(str, b[:-1])))
```

**Key Concepts:**
- Cycle detection in functional graph (permutation)
- Following pointers until returning to start
- Processing each cycle independently

---

## New Comprehensive Implementation

I've created a complete graph algorithms library in **`graph_algorithms.py`** with the following:

### Algorithms Included:

#### 1. **Connected Components**
- `count_connected_components_dfs()` - Using DFS with stack
- `count_connected_components_bfs()` - Using BFS with queue

#### 2. **Shortest Path**
- `shortest_path_bfs()` - Unweighted graphs (BFS)
- `dijkstra()` - Weighted graphs with non-negative weights
- `bellman_ford()` - Weighted graphs with negative weights

#### 3. **Connectivity**
- `is_connected()` - Check if graph is connected
- `find_bridges()` - Find critical edges (bridges)

#### 4. **Pathfinding**
- `find_all_paths_dfs()` - Find all paths between two nodes
- `has_path()` - Check if path exists

#### 5. **Cycle Detection**
- `has_cycle_undirected()` - Detect cycles in undirected graphs
- `has_cycle_directed()` - Detect cycles in directed graphs

---

## Common Patterns in Your Implementations

### 1. **Graph Representation**
```python
from collections import defaultdict
graph = defaultdict(list)

# Undirected edge
graph[u].append(v)
graph[v].append(u)

# Weighted edge
graph[u].append((v, weight))
graph[v].append((u, weight))
```

### 2. **DFS (Iterative)**
```python
def dfs(start):
    stack = [start]
    visited = set()
    
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
```

### 3. **BFS**
```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### 4. **Visited Tracking**
```python
# Using list (0-indexed)
visited = [False] * n

# Using set
visited = set()

# Using dictionary
visited = {}
```

---

## Quick Reference

### When to Use What:

| Problem Type | Algorithm | Time Complexity |
|-------------|-----------|----------------|
| Count components | DFS/BFS | O(V + E) |
| Shortest path (unweighted) | BFS | O(V + E) |
| Shortest path (weighted, positive) | Dijkstra | O((V + E) log V) |
| Shortest path (negative weights) | Bellman-Ford | O(VE) |
| Check connectivity | BFS/DFS | O(V + E) |
| Find all paths | DFS with backtracking | O(V!) |
| Cycle detection | DFS | O(V + E) |

---

## Practice Problems by Category

### Connected Components
- ✅ C. Rumor (Educational Round 33)

### Weighted Graphs
- ✅ Hello 2025/d.py (Path with k-th weight)

### Cycles
- ✅ D. Sakurako's Hobby (Permutation cycles)

---

## Run the Examples

To see all algorithms in action:
```bash
cd /Users/giorgikurtanidze/Documents/GitHub/icpc
python graph_algorithms.py
```

This will show examples of:
- Connected components counting
- Shortest path finding (BFS)
- Dijkstra's algorithm
- Connectivity checking
- Cycle detection
- Finding all paths
