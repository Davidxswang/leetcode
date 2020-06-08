"""
https://leetcode.com/problems/largest-perimeter-triangle/
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.



Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8


Note:

3 <= A.length <= 10000
1 <= A[i] <= 10^6
"""

# time complexity: O(nlogn), space complexity: O(1)
# in a sorted (decending order) array, if A[i], A[j], and A[k] where i < j < k satisfy that A[i] < A[j]+A[k],
# then A[i],A[jj],A[kk], where i < jj < j, and jj < kk < k will satisfy this inequality as well.
# in other words, if A[i], A[i+1], A[i+2] doesn't meet A[i] < A[i+1]+A[i+2], any A[i], A[j], A[k], j > i+1, k > i+2 will not either.
# so the answer will reside in any adjacent triplet.

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(0, len(A)-2):
            if A[i] < A[i+1]+A[i+2]:
                return A[i]+A[i+1]+A[i+2]
        return 0