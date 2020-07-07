"""
https://leetcode.com/problems/longest-increasing-subsequence/

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
# time complexity: O(n^2), space complexity: O(n)
# this is inspired by the solution provided by the question.
# dp
# the idea is to use a list longest to record say i-th element in nums, if as the last of the longest possible subsquence, how long the subsquence would be.
        """
        dp, longest[i] means if nums[i] is included in the longest increasing subsquence up until i, how long it is
        
        
        if not nums:
            return 0
        
        longest = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    longest[i] = max(longest[i], 1+longest[j])
        return max(longest)
        """
        

# time complexity: O(nlogn), space complexity: O(n)
# dp with binary search
# the key idea is to use a list to store the longest possible sequence, but the element in the list is not necessarily correct. Every element say record_long[i] in the list means the end of longest subsequence of length i+1
# this is inspired by @bolinq in the discussion area.
        import bisect
        record_long = []
        for num in nums:
            index = bisect.bisect_left(record_long, num)
            if index == len(record_long):
                record_long.append(num)
            else:
                record_long[index] = num
        
        return len(record_long)
