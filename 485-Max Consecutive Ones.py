"""
https://leetcode.com/problems/max-consecutive-ones/
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

# time complexity: O(n), space complexity: O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxones = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
            maxones = temp if temp > maxones else maxones
            if nums[i] == 0:
                temp = 0
        return maxones