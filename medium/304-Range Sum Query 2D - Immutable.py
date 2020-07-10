"""
https://leetcode.com/problems/range-sum-query-2d-immutable/
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

# time complexity: O(m*n) for init, O(1), space complexity: O(m*n)

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._matrix = matrix
        self.stat = []
        for i in range(len(matrix)):
            self.stat.append([0] * len(matrix[0]))
            for j in range(len(matrix[0])):
                self._fillValue(i, j)
    
    def _fillValue(self, i: int, j: int):
        if i == j == 0:
            self.stat[i][j] = self._matrix[i][j]
            return
        upstat = self.stat[i-1][j] if i > 0 else 0
        leftstat = self.stat[i][j-1] if j > 0 else 0
        upleftstat = self.stat[i-1][j-1] if i > 0 and j > 0 else 0
        self.stat[i][j] = upstat + leftstat - upleftstat + self._matrix[i][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        upstat = self.stat[row1-1][col2] if row1 > 0 else 0
        leftstat = self.stat[row2][col1-1] if col1 > 0 else 0
        upleftstat = self.stat[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return self.stat[row2][col2] - upstat - leftstat + upleftstat
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
