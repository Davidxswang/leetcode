"""
https://leetcode.com/problems/surface-area-of-3d-shapes/
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.



Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46


Note:

1 <= N <= 50
0 <= grid[i][j] <= 50
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        surface = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    surface += 2 + 4 * grid[i][j]
                    for row, column in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                        if 0 <= row < len(grid) and 0 <= column < len(grid[0]):
                            surface -= min(grid[i][j], grid[row][column])

        return surface