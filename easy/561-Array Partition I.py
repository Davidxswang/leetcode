"""
https://leetcode.com/problems/array-partition-i/
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
"""

# time complexity: O(nlogn), space complexity: O(n)

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        self.sort(nums, 0, len(nums) - 1)
        return sum([nums[i] for i in range(0, len(nums), 2)])

    def sort(self, nums: List[int], start: int, end: int) -> None:
        if start >= end:
            return
        import random
        pivot = random.randrange(start, end + 1)
        nums[start], nums[pivot] = nums[pivot], nums[start]
        i = j = start + 1
        while j <= end:
            if nums[j] < nums[start]:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j += 1
        nums[start], nums[i - 1] = nums[i - 1], nums[start]
        self.sort(nums, start, i - 2)
        self.sort(nums, i, end)