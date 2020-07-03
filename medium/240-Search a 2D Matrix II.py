"""
https://leetcode.com/problems/search-a-2d-matrix-ii/
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
"""

# time complexity: O(mlogn), space complexity: O(m)

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows_to_search = []
        for i in range(len(matrix)):
            if matrix[i][0] == target or matrix[i][-1] == target:
                return True
            if matrix[i][0] < target < matrix[i][-1]:
                if self.search(matrix[i], 0, len(matrix[0])-1, target):
                    return True
        
        return False
    
    def search(self, line, start, end, target) -> bool:
        if start > end:
            return False
        mid = start + (end-start) // 2
        if target == line[start] or target == line[end] or target == line[mid]:
            return True
        if line[mid] < target:
            return self.search(line, mid+1, end, target)
        else:
            return self.search(line, start, mid-1, target)
