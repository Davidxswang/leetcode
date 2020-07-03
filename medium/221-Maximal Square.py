"""
https://leetcode.com/problems/maximal-square/
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

# time complexity: O(m*n), space complexity: O(n)
# this is inspired by the solution provided by the problem.
# the main idea is to use a list to keep track of the result of last line. The key is the logic: cur[j] = min(left, top-left, top) + 1 if cur[j] == 1else 0
# The logic here make sure we don't need to do the work repeatedly.

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        temp = [int(i) for i in matrix[0]]
        maximal = max(temp)
        for i in range(1, len(matrix)):
            cur = [int(num) for num in matrix[i]]
            for j in range(1, len(matrix[0])):
                cur[j] = min(cur[j-1], temp[j-1], temp[j]) + 1 if cur[j] == 1 else 0
            maximal = max(cur + [maximal])
            temp = cur
        return maximal**2
