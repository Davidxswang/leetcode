"""
https://leetcode.com/problems/find-the-duplicate-number/
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

# time complexity: O(n), space complexity: O(1)
# the solution is provided by the solution of the question.
# the solution is to treat the nums list as the linked list and the numbers it stores are the pointers which point to the position of the next element.
# the question then becomes: find the start of the cycle of the linked list, which we can apply Floyd's Algorithm to solve.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        start = nums[0]
        incycle = fast
        while start != incycle:
            start = nums[start]
            incycle = nums[incycle]
        
        return start
        
