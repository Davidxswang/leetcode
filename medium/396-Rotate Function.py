"""
https://leetcode.com/problems/rotate-function/

Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 105.

Example:

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
"""

# time complexity: O(n), space complexity: O(n)

class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        """
        F(0) = X
        F(1) = F(0) + A[0] + A[1] + A[2] - (n-1)A[3]
        F(2) = F(1) + A[3] + A[0] + A[1] - (n-1)A[2]
        F(3) = F(2) + A[2] + A[3] + A[0] - (n-1)A[1]
        """
        if not A:
            return 0
        n = len(A)
        if n == 1:
            return 0
        
        F = [0] * n
        
        for i in range(n):
            F[0] += i * A[i]
        
        sum_a = sum(A)
        for i in range(1, n):
            F[i] = F[i-1] + sum_a - n*A[n-i]
        
        return max(F)