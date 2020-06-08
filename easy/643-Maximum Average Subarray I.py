"""
https://leetcode.com/problems/maximum-average-subarray-i/
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75


Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum = tempsum = sum(nums[:k])
        for i in range(k,len(nums)):
            tempsum += - nums[i-k] + nums[i]
            maxsum = tempsum if tempsum > maxsum else maxsum
        return maxsum / k