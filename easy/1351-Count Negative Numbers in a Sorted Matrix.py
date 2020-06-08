"""
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
"""

# time complexity: O(m*n), space complexity: O(n)

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        farthest = len(grid[0])
        for i in range(len(grid)):
            for j in range(min(len(grid[0]),farthest)):
                if grid[i][j] < 0:
                    result += len(grid[0])-j
                    farthest = j+1
                    break
        return result
