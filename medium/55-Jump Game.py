"""
https://leetcode.com/problems/jump-game/
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5
"""

# time complexity: O(n), space complexity: O(1)
# this is a very classic dynamic programming problem
# if from position A, one can just to the last element, then position A is good
# the last element is good
# from right to left, if the leftmost good element is within the jump range of the current element, current element is good as well
# we just need to check if position=0 is good

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastTrue = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if lastTrue <= nums[i]+i:
                lastTrue = i
        return lastTrue == 0
