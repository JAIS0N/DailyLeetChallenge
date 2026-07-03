from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        max_cost = 0

        for u, v, cost in edges:
            graph[u].append((v, cost))
            indegree[v] += 1
            max_cost = max(max_cost, cost)

        queue = deque(i for i in range(n) if indegree[i] == 0)
        topo = []

        while queue:
            node = queue.popleft()
            topo.append(node)

            for nei, _ in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        def can(min_score: int) -> bool:
            inf = float("inf")
            dist = [inf] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == inf:
                    continue

                for v, cost in graph[u]:
                    if cost < min_score:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    new_cost = dist[u] + cost
                    if new_cost < dist[v]:
                        dist[v] = new_cost

            return dist[n - 1] <= k

        left, right = 0, max_cost
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if can(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer