"""
https://leetcode.com/problems/search-a-2d-matrix/
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""

# time complexity: O(logn), space complexity: O(logn) due to the call stack, where n is the total number of elements in matrix
# key here is to convert the index (from 0 to n-1) to location in the matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0] or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        self.m = len(matrix)
        self.n = len(matrix[0])
        return self.find(matrix, 0, self.m*self.n-1, target)
        
    def find(self, matrix: List[List[int]], start: int, end: int, target: int) -> bool:
        if start > end:
            return False
        
        row1, col1 = self.location(start)
        row2, col2 = self.location(end)
        
        if matrix[row1][col1] == target or matrix[row2][col2] == target:
            return True
        
        mid = start + (end-start) // 2
        rowm, colm = self.location(mid)
        if matrix[rowm][colm] == target:
            return True
        elif matrix[rowm][colm] < target:
            return self.find(matrix, mid+1, end-1, target)
        else:
            return self.find(matrix, start+1, mid-1, target)
        
        
        
    def location(self, number: int) -> tuple:
        return number // self.n, number % self.n
