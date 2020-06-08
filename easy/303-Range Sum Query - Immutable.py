"""
https://leetcode.com/problems/range-sum-query-immutable/
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""

# Brute force.
# time complexity: O(n) for each calling, space complexity: O(1)
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        result = 0
        while i <= j:
            result += self.nums[i]
            i += 1
        return result

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)



# When initiating the array nums, save partial sum of the previous array into an array. Save time by taking up more space.
# time complexity: O(1) for each calling, but O(n) for initiating, space complexity: O(n)
class NumArray:

    def __init__(self, nums: List[int]):
        self.prev = [0] * len(nums)
        self.nums = nums
        for i in range(0, len(nums)):
            if i == 0:
                self.prev[0] = nums[0]
            else:
                self.prev[i] = self.prev[i - 1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.prev[j] - self.prev[i] + self.nums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)