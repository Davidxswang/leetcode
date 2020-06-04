"""
https://leetcode.com/problems/squares-of-a-sorted-array/submissions/
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.



Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if A[0] >= 0:
            return [A[i] ** 2 for i in range(len(A))]
        if A[-1] <= 0:
            return [A[~i] ** 2 for i in range(len(A))]

        i = 0
        j = len(A) - 1
        result = [0] * len(A)
        pointer = 0
        while i <= j:
            if abs(A[i]) >= abs(A[j]):
                result[pointer] = A[i] ** 2
                i += 1
            else:
                result[pointer] = A[j] ** 2
                j -= 1
            pointer += 1
        return result[::-1]

