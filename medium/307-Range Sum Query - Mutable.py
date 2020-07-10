"""
https://leetcode.com/problems/range-sum-query-mutable/
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""


class NumArray:

# time complexity: O(n) for init, O(n) for update, O(1) for sum, space complexity: O(n)
    """
    def __init__(self, nums: List[int]):
        self._nums = nums
        self.stat = [0] * len(nums)
        if len(nums) == 0:
            return
        self.stat[0] = nums[0]
        for i in range(1, len(nums)):
            self.stat[i] = self._nums[i] + self.stat[i-1]
        
    def update(self, i: int, val: int) -> None:
        change = val - self._nums[i]
        self._nums[i] = val
        for j in range(i, len(self.stat)):
            self.stat[j] += change

    def sumRange(self, i: int, j: int) -> int:
        return self.stat[j] - self.stat[i] + self._nums[i]
    """

# this is provided by the solution of the question. 
# Basically, the idea is to use a binary tree to record the sum of different partition.
# time complexity: O(n) for init, O(logn) for update, O(logn) for sum, space complexity: O(n)
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * self.n * 2
        self._buildTree(nums)

    def _buildTree(self, nums: List[int]) -> None:
        for i in range(self.n, 2*self.n):
            self.tree[i] = nums[i-self.n]
        for i in range(self.n-1, -1 ,-1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]
            # here self.tree[0] == self.tree[1]
        
    def update(self, i: int, val: int) -> None:
        pos = i + self.n
        change = val - self.tree[pos]
        while pos > 0:
            # because self.tree[0] == self.tree[1] so we can stop when pos == 1
            self.tree[pos] += change
            pos //= 2

    def sumRange(self, i: int, j: int) -> int:
        result = 0
        left, right = i+self.n, j+self.n
        while left <= right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 0:
                result += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return result
        
        
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
