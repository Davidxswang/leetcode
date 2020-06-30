"""
https://leetcode.com/problems/number-of-islands/
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

# time complexity: O(n*m), space complexity: O(m*n) due to the call stack, where m and n are the height and width of the matrix

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(color, i, j):
            for row, col in (i-1, j),(i+1,j),(i,j-1),(i,j+1):
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == '1':
                    grid[row][col] = color
                    helper(color, row, col)
                    
        start = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = start
                    helper(start, i, j)
                    start += 1
                    #print(grid)
        return start - 2
                    
                    
        
        
