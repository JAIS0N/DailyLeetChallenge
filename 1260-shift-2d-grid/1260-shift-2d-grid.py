class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        columns = len(grid[0])
        total_elements = rows * columns
        k %= total_elements

        shifted_grid = [[0] * columns for _ in range(rows)]

        for row in range(rows):
            for column in range(columns):
                current_index = row * columns + column
                shifted_index = (current_index + k) % total_elements
                shifted_row = shifted_index // columns
                shifted_column = shifted_index % columns
                shifted_grid[shifted_row][shifted_column] = grid[row][column]

        return shifted_grid
        