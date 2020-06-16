"""

https://leetcode.com/problems/spiral-matrix-ii/
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

# time complexity: O(n^2), space complexity: O(1)
# this is very similar to questions 54, the key is to find when to loop and when to stop

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        result = [[0]*n for i in range(n)]
        row, column = 0, 0
        step = (0, 1)
        current = 1
        up, down, left, right = 0, n-1, 0, n-1
        while up <= row <= down and left <= column <= right:
            result[row][column] = current
            current += 1
            if step == (0, 1) and column == right:
                step = (1, 0)
                up = row + 1
            elif step == (1, 0) and row == down:
                step = (0, -1)
                right = column - 1
            elif step == (0, -1) and column == left:
                step = (-1, 0)
                down = row - 1
            elif step == (-1, 0) and row == up:
                step = (0, 1)
                left = column + 1
            row += step[0]
            column += step[1]
        return result
