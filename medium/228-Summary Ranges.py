"""
https://leetcode.com/problems/summary-ranges/
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        if len(nums) == 1:
            return [str(nums[0])]
        
        result = []
        start = end = 0
        while end < len(nums):
            if end == len(nums)-1 or nums[end+1] - nums[end] > 1:
                # this is the end
                if start == end:
                    result.append(str(nums[start]))
                else:
                    result.append(str(nums[start]) + '->' + str(nums[end]))
                start = end + 1
            end += 1
        
        return result
