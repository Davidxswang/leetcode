"""
https://leetcode.com/problems/projection-area-of-3d-shapes/
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.



Example 1:

Input: [[2]]
Output: 5
Example 2:

Input: [[1,2],[3,4]]
Output: 17
Explanation:
Here are the three projections ("shadows") of the shape made with each axis-aligned plane.

Example 3:

Input: [[1,0],[0,2]]
Output: 8
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 14
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 21


Note:

1 <= grid.length = grid[0].length <= 50
0 <= grid[i][j] <= 50
"""

# time complexity: O(n), space complexity: O(n^0.5)
# DP

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        leftright = [0] * len(grid[0])
        frontback = [0] * len(grid)
        updown = 0

        for i in range(len(grid)):
            leftright[i] = grid[i][0]
        for i in range(len(grid[0])):
            frontback[i] = grid[0][i]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    updown += 1
                leftright[i] = max(leftright[i], grid[i][j])
                frontback[j] = max(frontback[j], grid[i][j])

        return updown + sum(frontback + leftright)

