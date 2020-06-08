"""
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
Given an array nums of integers, return how many of them contain an even number of digits.
 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
 

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10^5
"""

# time complexity: O(nlogm), space complexity: O(1), where n is the length of nums, and m is the largest number in nums
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            digit = 0
            while num > 0:
                digit += 1
                num //= 10
            result += 1 if digit % 2 == 0 else 0
        return result
