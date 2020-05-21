"""
https://leetcode.com/problems/island-perimeter/
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
"""

# time complexity: O(n), space complexity: O(1), where n is the number of elements in grid
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        landcell = 0
        minus = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    landcell += 1
                    if j > 0 and grid[i][j-1] == 1:
                        minus += 1
                    if j < len(grid[i])-1 and grid[i][j+1] == 1:
                        minus +=1
                    if i > 0 and grid[i-1][j] == 1:
                        minus += 1
                    if i < len(grid)-1 and grid[i+1][j] == 1:
                        minus += 1
        return landcell * 4 - minus