"""
https://leetcode.com/problems/3sum-closest/
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""
# time complexity: O(n^2), space complexity: O(1)
# this is very close to the 3sum problem, and I got the inpiration from the solution provided by the problem set.
# The idea is to sort the list first and then fix one number and search the numbers after it, and log the best one we have got.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = pow(2,32)  # total - target
        i = 0
        while i < len(nums) - 2:
            low = i + 1
            high = len(nums) - 1
            while low < high:
                total = nums[i] + nums[low] + nums[high]
                newdiff = total - target
                if newdiff == 0:
                    return target
                if abs(newdiff) < abs(diff):
                    diff = newdiff
                if total < target:
                    low += 1
                else:
                    high -= 1
            i += 1
        return target + diff
