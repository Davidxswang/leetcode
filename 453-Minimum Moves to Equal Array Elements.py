"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""

# Incrementing n-1 numbers by 1 is equivalent to decrementing 1 number by 1.
# time complexity: O(n), space complexity: O(1)
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum = nums[0]
        result = 0
        for i in range(len(nums)):
            if nums[i] < minimum:
                minimum = nums[i]
        for i in range(len(nums)):
            result += nums[i] - minimum
        return result