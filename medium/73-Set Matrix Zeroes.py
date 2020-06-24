"""
https://leetcode.com/problems/set-matrix-zeroes/
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

# time complexity: O(m*n), space complexity: O(m+n)
# because I use two vars to store the row and column that should be set to 0, the worse case space complexity is O(m+n)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        column = set()
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in row or j in column:
                    matrix[i][j] = 0


# time complexity: O(m*n), space complexity: O(1)
# this is inspired by @mzchen in the discussion area
# main idea is to use the first row and first column to record whether this column or row needs to be set to 0
# tricky thing here is to distinguish between the original 0 and the indicator zero by a separate variable


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
       
        m = len(matrix)
        n = len(matrix[0])
        
        firstrowhaszero = False
        firstcolumnhaszero = False
        for i in range(m):
            if matrix[i][0] == 0:
                firstcolumnhaszero = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                firstrowhaszero = True
                break
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if firstcolumnhaszero:
            for i in range(m):
                matrix[i][0] = 0
        
        if firstrowhaszero:
            for j in range(n):
                matrix[0][j] = 0
