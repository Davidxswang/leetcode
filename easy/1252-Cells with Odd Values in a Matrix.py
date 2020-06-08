"""
https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.

 

Example 1:


Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
Example 2:


Input: n = 2, m = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
 

Constraints:

1 <= n <= 50
1 <= m <= 50
1 <= indices.length <= 100
0 <= indices[i][0] < n
0 <= indices[i][1] < m

"""
# time complexity: O(n), space complexity: O(n+m)

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row = [0] * n
        column = [0] * m
        for r,c in indices:
            row[r] += 1
            column[c] += 1
        odd = 0
        oddrow = 0
        oddcolumn = 0
        for r in row:
            if r % 2 == 1:
                odd += m
                oddrow += 1
        for c in column:
            if c % 2 == 1:
                odd += n
                oddcolumn += 1
        odd -= 2 * (oddrow * oddcolumn)
        return odd
