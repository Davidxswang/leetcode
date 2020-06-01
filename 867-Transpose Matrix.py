"""
https://leetcode.com/problems/transpose-matrix/
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.





Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]


Note:

1 <= A.length <= 1000
1 <= A[0].length <= 1000
"""

# time complexity: O(n), space complexity: O(n)

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for column in range(len(A[0])):
            result.append([])
            for row in range(len(A)):
                result[-1].append(A[row][column])
        return result