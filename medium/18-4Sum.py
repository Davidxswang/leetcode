"""
https://leetcode.com/problems/4sum/
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
# time complexity: O(n^3), space complexity: O(1)
# this is very similar to 3 sum:
#   1. sort the array, since the total time complexity is n^3, sorting will be a big part
#   2. fix a start position
#   3. fix a end position
#   4. solve it like 2 sum
# the trick is to early stop when the edge numbers are either too big or too small for 4 of the numbers to sum up to target
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        i = 0
        result = []
        while i < len(nums) - 3:
            if 4*nums[i] > target:
                break
            while i != 0 and nums[i] == nums[i-1]:
                i += 1
            j = len(nums) - 1
            while j >= i + 3:
                if 4 * nums[j] < target:
                    break
                while j!=len(nums)-1 and nums[j] == nums[j+1]:
                    j -= 1
                m = i + 1
                n = j - 1
                while m < n:
                    total = nums[i] + nums[m] + nums[n] + nums[j]
                    if total < target:
                        m += 1
                        while m < n and nums[m] == nums[m-1]:
                            m += 1
                    elif total > target:
                        n -= 1
                        while m < n and nums[n] == nums[n+1]:
                            n -= 1
                    else:
                        result.append([nums[i], nums[m], nums[n], nums[j]])
                        m += 1
                        n -= 1
                        while m < n and nums[m] == nums[m-1]:
                            m += 1
                        while m < n and nums[n] == nums[n+1]:
                            n -= 1
                j -= 1
            i += 1
        return result
