class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        # Step 1: Apply gravity — stones fall to the right in each row
        for row in boxGrid:
            empty = n - 1  # rightmost available empty slot
            for j in range(n - 1, -1, -1):
                if row[j] == '#':
                    row[j] = '.'
                    row[empty] = '#'
                    empty -= 1
                elif row[j] == '*':
                    empty = j - 1  # reset: can't pass through obstacle
        
        # Step 2: Rotate 90° clockwise
        # Original [i][j] → Rotated [j][m-1-i]
        # New dimensions: n rows × m cols
        result = [['.' for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                result[j][m - 1 - i] = boxGrid[i][j]
        
        return result