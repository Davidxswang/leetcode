"""
https://leetcode.com/problems/largest-time-for-given-digits/
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.



Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""


Note:

A.length == 4
0 <= A[i] <= 9
"""

# time complexity: O(1), space complexity: O(1)
# the use of permutations function is beautiful

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = -1
        from itertools import permutations
        for i, j, k, m in permutations(A):
            hour = i * 10 + j
            minute = k * 10 + m
            time = hour * 100 + minute
            if 0 <= hour <= 23 and 0 <= minute <= 59 and time > ans:
                ans = time

        return '{:02}:{:02}'.format(*divmod(ans, 100)) if ans != -1 else ''