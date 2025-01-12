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
