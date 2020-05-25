"""
https://leetcode.com/problems/non-decreasing-array/
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).



Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.


Constraints:

1 <= n <= 10 ^ 4
- 10 ^ 5 <= nums[i] <= 10 ^ 5
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        breakrule = 0
        breakrule_location = -1
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                breakrule += 1
                breakrule_location = i
                if breakrule > 1:
                    return False
        if breakrule == 0:
            return True
        else:
            if breakrule_location == 0 or breakrule_location == len(nums)-2:
                return True
            else:
                if nums[breakrule_location-1] <= nums[breakrule_location+1] or nums[breakrule_location+2] >= nums[breakrule_location]:
                    return True
                else:
                    return False