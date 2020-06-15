"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

# time complexity: O(logn), space complexity: O(logn) due to the call stack
# the first solution is posted by me, actually 3 passes, first to find one possible target, if found, second and third passes will try to find the leftmost and rightmost target.

# the second solution is inspired by @baby_groot in the discussion area. His (I assume it's he) code is very concise and elegant. The idea is to not stop and return when finding one target, instead, we should let the program narrow down until left and right points to the same element. In this case, either we have found the element, or there is no such target. If we have found such target, we can find leftmost one and the rightmost one. This is very smart. 

class Solution:
    """
    This is my solution, using 3 binary search, to find: one possible target, leftmost target, rightmost target
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        onepos = self.find(nums, 0, len(nums)-1, target)
        if onepos == -1:
            return [-1, -1]
        else:
            left = self.findleft(nums, 0, onepos, target)
            right = self.findright(nums, onepos, len(nums)-1, target)
            return [left, right]
    
    def findleft(self, nums: List[int], start: int, end: int, target: int) -> int:
        if nums[start] == target:
            return start
  
        mid = start + (end-start) // 2
        if nums[mid] == target and nums[mid-1] != target:
            return mid
        elif nums[mid] == target and nums[mid-1] == target:
            return self.findleft(nums, start, mid-1, target)
        else:
            return self.findleft(nums, mid+1, end, target)
    
    def findright(self, nums: List[int], start: int, end: int, target: int) -> int:
        if nums[end] == target:
            return end
        mid = start + (end - start) // 2
        if nums[mid] == target and nums[mid+1] != target:
            return mid
        elif nums[mid] == target and nums[mid+1] == target:
            return self.findright(nums, mid+1, end, target)
        else:
            return self.findright(nums, start, mid-1, target)
    
    def find(self, nums: List[int], start: int, end: int, target: int) -> int:
        if start > end: 
            return -1
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.find(nums, start+1, mid-1, target)
        else:
            return self.find(nums, mid+1, end-1, target)
    """
    
    # this is inspired by @baby_groot in the discussion area. very smart.
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        return [self.left(nums, target), self.right(nums, target)]
    
    def left(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = i + (j-i) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        return i if nums[i] == target else -1
    
    def right(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = i + (j - i) // 2 + 1
            # +1 is important here because if we don't plus one, when we calculate the mid, it will tend to close to i
            # in that case, if mid == i and nums[mid] <= target, then i = mid, this will create the dead loop
            # instead, if we make mid = i+1 when j-i<=1, then when nums[mid] <= target, this will let i = i+1, so this will not create a dead loop
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid
        return i if nums[i] == target else -1
        
        
