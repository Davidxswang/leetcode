"""
https://leetcode.com/problems/magic-squares-in-grid/
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).



Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        result = 0

        def check(r, c):
            l = []

            def suml(i, j, k):
                return l[i - 1] + l[j - 1] + l[k - 1]

            for row in range(-1, 2):
                for column in range(-1, 2):
                    l.append(grid[r + row][c + column])
            return sorted(l) == list(range(1, 10)) and (
                        suml(1, 5, 9) == suml(2, 5, 8) == suml(3, 5, 7) == suml(4, 5, 6) == suml(1, 2, 3) == suml(7, 8,
                                                                                                                  9) == suml(
                    1, 4, 7) == suml(3, 6, 9) == 15) and l[4] == 5

        for center_row in range(1, len(grid) - 1):
            for center_column in range(1, len(grid[0]) - 1):
                if check(center_row, center_column):
                    result += 1

        return result
