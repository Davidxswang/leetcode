"""
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


# divide and conquer
# every time divide the array into two parts, calculate the maximum subarray in each part(left and right), and the array that is across the middle element
# max(left sum, right sum, the sum across the middle element) is the result of that layer
# time complexity: O(nlogn), space complexity: O(nlogn)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        return self.divideconquer(nums, 0, len(nums) - 1)

    def divideconquer(self, nums: List[int], left: int, right: int) -> int:
        if left == right:
            return nums[left]
        middle = left + (right - left) // 2
        leftsum = self.divideconquer(nums, left, middle)
        rightsum = self.divideconquer(nums, middle + 1, right)
        acrosssum = self.acrosssum(nums, left, middle, right)
        return max(leftsum, rightsum, acrosssum)

    def acrosssum(self, nums: List[int], left: int, middle: int, right: int) -> int:
        leftmax = nums[middle]
        rightmax = nums[middle]
        leftsum = 0
        rightsum = 0

        i = middle
        while i >= left:
            leftsum += nums[i]
            leftmax = leftsum if leftsum > leftmax else leftmax
            i -= 1

        i = middle
        while i <= right:
            rightsum += nums[i]
            rightmax = rightsum if rightsum > rightmax else rightmax
            i += 1

        return leftmax + rightmax - nums[middle]





# Kadane's algorithm
# this uses dynamic algorithm, the core idea is that:
# when I am checking nums[i] and see if this should in the contiguous subarray, the rest of this subarray should not lower down the current element nums[i]
# which means, the rest of the subarray should not be lower than 0 (in this case, this value will not lower the nums[i] when previous + nums[i] = newresult)
# It's kind of like the Pareto principle: whatever value I am about to add to the current value, I should not make the current value worse
# time complexity: O(n), space complexity: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxsum, currentsum = nums[0], 0
        for i in range(len(nums)):
            currentsum = max(0, currentsum) + nums[i]
            maxsum = currentsum if currentsum > maxsum else maxsum
        return maxsum