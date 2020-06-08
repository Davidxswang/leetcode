"""
https://leetcode.com/problems/single-number/
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

# Pretty easy. Using XOR because a ^ a will be 0, so all the numbers that appear twice will cancel out,
# only the number that appears once will remain in the result.
# time complexity: O(n), space complexity: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[0] = nums[0] ^ nums[i]
        return nums[0]