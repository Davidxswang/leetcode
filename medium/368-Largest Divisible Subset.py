"""
https://leetcode.com/problems/largest-divisible-subset/

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""

# time complexity: O(n^2), space complexity: O(n).
# first, we need to sort the list, so that we can go from the smallest to the largest.
# second, we use an array to make a link list, each element in the array will remember if this number is the end of a divisible subset, how long is this list, and which element is the previous element. The first element will record (1, its index). At the meanwhile, we tract the length of the longest subset and last index
# At last, we will go back from the index to the beginning of the list.
# The solution is provided by @amit_gupta10 in the discussion area.

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        nums.sort()
        
        endLen, endIndex = 1, 0
        dp = [(0, 0)] * len(nums)
        dp[0] = (1, 0)  # len, lastIndex
        
        for i in range(1, len(nums)):
            dp[i] = max((dp[j][0]+1, j) for j in range(i+1) if nums[i] % nums[j] == 0)
            if dp[i][0] > endLen:
                endLen, endIndex = dp[i][0], i
        
        result = []
        i = endLen
        while i >= 1:
            result.append(nums[endIndex])
            _, endIndex = dp[endIndex]
            i -= 1
        
        return result