"""
https://leetcode.com/problems/unique-paths-ii/
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

# time complexity: O(m*n), space complexity: O(n)


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if m == 1:
            return 1 if sum(obstacleGrid[0]) == 0 else 0
        if n == 1:
            return 1 if sum(obstacleGrid[i][0] for i in range(m)) == 0 else 0
        
        row = [1] + [0] * (n-1) 
        for i in range(1, n):
            row[i] = 1 if row[i-1] == 1 and obstacleGrid[0][i] == 0 else 0


        for i in range(1, m):
            temp = [0] * n
            temp[0] = 1 if row[0] == 1 and obstacleGrid[i][0] == 0 else 0
            for j in range(1, n):
                temp[j] = 0 if obstacleGrid[i][j] == 1 else temp[j-1] + row[j]
            row = temp
        
        return row[-1]
