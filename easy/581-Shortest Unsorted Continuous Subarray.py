"""
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""

# Very good questions. Thanks to the solution!
# The first traverse is to find the the beginning and end of a reverse pair. A reverse pair is two nums such that nums[i] > nums[i+1].
# The second traverse is to find the min and max of the nums in nums[start] to nums[end]
# The third traverse is to find where the locations that min and max should be put if we were going to sort the array.
# Note in the 3rd traverse that we should find the element that nums[i] > min for start and nums[i] < max for end.
# Equality is excluded in both situations because first is the violation of the <= rule and second is to find the shortest subarray.

# time complexity: O(n), space complexity: O(1)

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = None
        end = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                start = i if start is None else start
                end = i + 1 if end is None or i + 1 > end else end
        if start is None:
            return 0

        minmin = nums[start]
        maxmax = nums[end]
        for i in range(start, end + 1):
            minmin = min(minmin, nums[i])
            maxmax = max(maxmax, nums[i])

        for i in range(len(nums)):
            start = min(i, start) if nums[i] > minmin else start
            end = max(i, end) if nums[i] < maxmax else end

        return end - start + 1