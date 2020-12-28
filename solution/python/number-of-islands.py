"""
Number of Islands
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

"""

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        
        islands = 0
        
        for row in range(self.m):
            for col in range(self.n):
                # print("In numIslands:", row, col, islands, "\n", self.grid,"\n")
                
                if self.grid[row][col] == "1":
                    self.sink(row, col)
                    islands += 1
        
        # print("Final grid:\n", self.grid, "\n")

        return islands
    
    def sink(self, row, col):
        
        # print("In sink:", row, col, "\n", self.grid,"\n")

        # Marking land as visited.
        self.grid[row][col] = "-"
        
        if row-1 >= 0 and self.grid[row-1][col] == "1":
            self.sink(row-1, col)
        
        if col-1 >= 0 and self.grid[row][col-1] == "1":
            self.sink(row, col-1)
        
        if row+1 < self.m and self.grid[row+1][col] == "1":
            self.sink(row+1, col)
        
        if col+1 < self.n and self.grid[row][col+1] == "1":
            self.sink(row, col+1)
