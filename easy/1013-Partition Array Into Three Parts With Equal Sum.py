"""
https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])



Example 1:

Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: A = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


Constraints:

3 <= A.length <= 50000
-10^4 <= A[i] <= 10^4
"""

# time complexity: O(n), space complexity: O(n)
# very good exercise of DP

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        left = [0] * len(A)  # from A[0] to this A[i] sum (from left to right)
        right = [0] * len(A)  # from A[-1] to this A[i] sum (from right to left)
        for i in range(len(A)):
            if i == 0:
                left[i] = A[i]
                right[~i] = A[~i]
            else:
                left[i] = left[i - 1] + A[i]
                right[~i] = right[~i + 1] + A[~i]
        total = sum(A)
        if total % 3 != 0:
            return False
        third = total // 3
        i = 0
        j = len(A) - 1
        while i + 1 < j:
            if left[i] == third and right[i + 1] == third * 2 and right[j] == third:
                return True
            if left[i] != third or right[i + 1] != third * 2:
                i += 1
            if right[j] != third or left[j - 1] != third * 2:
                j -= 1

        return False