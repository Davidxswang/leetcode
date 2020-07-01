"""

https://leetcode.com/problems/kth-largest-element-in-an-array/
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

# time complexity: O(n), space complexity: O(logn)
# the average time complexity should be O(n), the worst is very hard to happend. Because we randomly select the pivot number every iteration
# in average, we split the problem into half and work on that half, so the symptotically time complexity should be O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 1:
            return max(nums)
        if k == len(nums):
            return min(nums)
        return self.find(nums, 0, len(nums)-1, k-1)
    
    def find(self, nums: List[int], start: int, end: int, target_index: int) -> int:
        if start == end:
            return nums[start]
        import random
        pivot = random.randrange(start, end+1)
        nums[start], nums[pivot] = nums[pivot], nums[start]
        i = j = start + 1
        while j <= end:
            if nums[j] >= nums[start]: 
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j += 1
        nums[start], nums[i-1] = nums[i-1], nums[start]
        if i-1 == target_index:
            return nums[target_index]
        elif i-1 > target_index:
            return self.find(nums, start, i-2, target_index)
        else:
            return self.find(nums, i, end, target_index)
