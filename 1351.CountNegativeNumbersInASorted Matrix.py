class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        
        rows, cols = len(grid), len(grid[0])

        row, col = 0, cols - 1

        while row < rows and col >= 0:
            if grid[row][col] < 0:
                count += rows - row
                col -= 1
            else:
                row += 1
        
        return count
