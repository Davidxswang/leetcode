"""
https://leetcode.com/problems/house-robber/
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

# I didn't come up with the solution. The solutions below are all inspired by @heroes3001 in the discussion area.
# So basically this is a dynamic programming problem.
# The core idea is that the current maximum profit is whether:
# from robbing current house + the maximum profit in house current-2 house. or
# from not robbing current house, i.e. the maximum profit in the current house == the maximum profit in the current-1 house
# whichever is larger should be the maximum profit in the current house.

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        profit = [0] * len(nums)
        profit[0] = nums[0]
        profit[1] = max(0 + nums[1], profit[0])
        i = 2
        while i < len(nums):
            profit[i] = max(profit[i - 2] + nums[i], profit[i - 1])
            i += 1
        return profit[-1]


# The upgraded version is to get rid of the list, using two variables instead.
# time complexity: O(n), space complexity: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # prev2, prev1, nums[i]
        prev2 = 0
        prev1 = 0
        for i in range(len(nums)):
            temp = prev1
            prev1 = max(prev2 + nums[i], prev1)
            prev2 = temp
        return prev1