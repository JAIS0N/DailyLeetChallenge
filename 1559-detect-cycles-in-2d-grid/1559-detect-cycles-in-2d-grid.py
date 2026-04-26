class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(r, c, prev_r, prev_c) -> bool:
            visited[r][c] = True
            
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                
                # Out of bounds or different character — skip
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if grid[nr][nc] != grid[r][c]:
                    continue
                
                # Skip the cell we just came from
                if nr == prev_r and nc == prev_c:
                    continue
                
                # Already visited → cycle found
                if visited[nr][nc]:
                    return True
                
                if dfs(nr, nc, r, c):
                    return True
            
            return False
        
        for r in range(m):
            for c in range(n):
                if not visited[r][c]:
                    if dfs(r, c, -1, -1):
                        return True
        
        return False
        