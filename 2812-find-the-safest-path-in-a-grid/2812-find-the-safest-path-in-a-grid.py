from collections import deque
import heapq
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        # Step 1: distance of every cell from nearest thief
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # Step 2: maximum safeness path from (0, 0) to (n - 1, n - 1)
        max_heap = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]

        while max_heap:
            safety, r, c = heapq.heappop(max_heap)
            safety = -safety

            if visited[r][c]:
                continue

            visited[r][c] = True

            if r == n - 1 and c == n - 1:
                return safety

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    new_safety = min(safety, dist[nr][nc])
                    heapq.heappush(max_heap, (-new_safety, nr, nc))

        return 0