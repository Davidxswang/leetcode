"""
https://leetcode.com/problems/rotate-array/
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0
"""

# I did't come up with this idea. Thanks to @danny6514 in the discussion area.
# This is genious, but very easy to interpret.
# To rotate, is to put the last few digits in the front.
# This can be thought as reverse the whole list first so that the few digits are in the front, but all the digits are in the wrong order.
# Then, reverse the first few digits that are supposed to move from the back to the front.
# At last, reverse the last few digits that are supposed to move from the front to the back.
# time complexity: O(n), space complexity: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        i = start
        j = end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1