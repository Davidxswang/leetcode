"""
https://leetcode.com/problems/minimum-path-sum/
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

# time complexity: O(m*n), space complexity: O(n)
# this is very similar to 62 and 63, all dp problems

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        if m == 1:
            return sum(grid[0])
        if n == 1:
            return sum(grid[i][0] for i in range(m))
        
        row = [0] * n
        row[0] = grid[0][0]
        for i in range(1, n):
            row[i] = row[i-1] + grid[0][i]
        
        for i in range(1, m):
            temp = [0] * n
            temp[0] = row[0] + grid[i][0]
            for j in range(1, n):
                temp[j] = grid[i][j] + row[j] if row[j] <= temp[j-1] else temp[j-1] + grid[i][j]
            row = temp
        
        return row[-1]
