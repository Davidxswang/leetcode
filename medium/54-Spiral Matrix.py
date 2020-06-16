"""
https://leetcode.com/problems/spiral-matrix/
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

# time complexity: O(n*m), space complexity: O(1)
# the trick here is find the right loop condition, when to loop and when to stop
# this is very similar to question 59

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return [matrix[0][0]]
        row, column = 0, 0
        step = (0, 1)
        up, down, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        result = []
        while up <= row <= down and left <= column <= right:
            result.append(matrix[row][column])
            if step == (0, 1) and column == right:
                step = (1, 0)
                up = row+1
            elif step == (1, 0) and row == down:
                step = (0, -1)
                right = column-1
            elif step == (0, -1) and column == left:
                step = (-1, 0)
                down = row-1
            elif step == (-1, 0) and row == up:
                step = (0, 1)
                left = column + 1
            row += step[0]
            column += step[1]
        #result.append(matrix[up][left])
        return result
