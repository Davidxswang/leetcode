"""
https://leetcode.com/problems/search-insert-position/
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""


# it is pretty simple, since the array is monotonically increasing, we should check == first
# if not, check <, move toward the end if yes
# if found a nums[i] > target, it indicates that the target is >num[i-1] and target is < nums[i], return i
# if in the end, nothing found, add this target at the end of the original list
# time complexity: O(n), space complexity: O(1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            if nums[i] < target:
                i += 1
                continue
            if nums[i] > target:
                return i
        return len(nums)