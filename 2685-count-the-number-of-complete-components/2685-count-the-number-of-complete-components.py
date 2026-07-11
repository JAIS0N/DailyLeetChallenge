class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        complete_components = 0

        def dfs(node):
            visited[node] = True

            node_count = 1
            degree_sum = len(graph[node])

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    child_nodes, child_degrees = dfs(neighbor)
                    node_count += child_nodes
                    degree_sum += child_degrees

            return node_count, degree_sum

        for node in range(n):
            if not visited[node]:
                nodes, degrees = dfs(node)

                if degrees == nodes * (nodes - 1):
                    complete_components += 1

        return complete_components
        