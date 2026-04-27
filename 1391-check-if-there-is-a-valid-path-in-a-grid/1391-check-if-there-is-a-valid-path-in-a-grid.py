class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        # Directions: up, right, down, left
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # For each street type, which directions are allowed
        moves = {
            1: [3, 1],  # left, right
            2: [0, 2],  # up, down
            3: [3, 2],  # left, down
            4: [1, 2],  # right, down
            5: [3, 0],  # left, up
            6: [1, 0],  # right, up
        }

        visited = [[False] * n for _ in range(m)]
        q = deque([(0, 0)])
        visited[0][0] = True

        while q:
            r, c = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            for d in moves[grid[r][c]]:
                nr, nc = r + dirs[d][0], c + dirs[d][1]

                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    # Opposite direction
                    opposite = (d + 2) % 4

                    # Next cell must connect back
                    if opposite in moves[grid[nr][nc]]:
                        visited[nr][nc] = True
                        q.append((nr, nc))

        return False