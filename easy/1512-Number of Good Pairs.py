"""
https://leetcode.com/problems/number-of-good-pairs/
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

# time complexity: O(n), space complexity: O(n)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        counter = dict()
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        result = 0
        for key, value in counter.items():
            if value >= 2:
                result += value * (value-1) / 2
        return int(result)
