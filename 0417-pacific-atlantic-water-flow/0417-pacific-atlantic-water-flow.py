class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Edge case: empty grid
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])

        # These sets will store cells reachable from each ocean
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            # Mark current cell as reachable from the ocean
            visited.add((r, c))

            # 4 possible directions (down, up, right, left)
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check:
                # 1. within bounds
                # 2. not already visited
                # 3. next height >= current height (IMPORTANT: reverse flow)
                if (0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):

                    # Continue DFS from neighbor
                    dfs(nr, nc, visited)

        #  Start DFS from Pacific Ocean borders
        # Top row (row = 0)
        for c in range(cols):
            dfs(0, c, pacific)

        # Left column (col = 0)
        for r in range(rows):
            dfs(r, 0, pacific)

        # Start DFS from Atlantic Ocean borders
        # Bottom row (row = rows-1)
        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        # Right column (col = cols-1)
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        # Intersection:
        # Cells that can reach BOTH oceans
        return list(pacific & atlantic) 