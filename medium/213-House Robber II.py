"""
https://leetcode.com/problems/house-robber-ii/
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""

# time complexity: O(n), space complexity: O(1)
# the key here is to traverse twice, one including the first house but excluding the last house, the other excluding the first house but including the last house.
# Solved by two traverse DP 

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        
        # rob from house 0
        prev1 = 0
        prev2 = nums[0]
        for i in range(1, len(nums)-1):
            cur = max(prev1+nums[i], prev2)
            prev1, prev2 = prev2, cur
        result1 = cur
        
        # rob from house 1
        prev1 = 0
        prev2 = nums[1]
        for i in range(2, len(nums)):
            cur = max(prev1+nums[i], prev2)
            prev1, prev2 = prev2, cur
        result2 = cur
        return max(result1, result2)
