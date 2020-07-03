"""
https://leetcode.com/problems/majority-element-ii/
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""

# time complexity: O(n), space complexity: O(1)
# this is provided by @orbuluh in the discussion area. 
# The idea here is very similar to the problem "Major Element". The core is to traverse twice.
# the first traversal is to find two candidates. Ideally, two candidates should be the remaining elements after being cancelling out by the non-candidate elements.

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2, counter1, counter2 = 0, 1, 0, 0
        for n in nums:
            if n == num1:
                counter1 += 1
            elif n == num2:
                counter2 += 1
            elif counter1 == 0:
                num1, counter1 = n, 1
            elif counter2 == 0:
                num2, counter2 = n, 1
            else:
                counter1 -= 1
                counter2 -= 1
        
        return [n for n in (num1, num2) if nums.count(n) > len(nums) // 3]
