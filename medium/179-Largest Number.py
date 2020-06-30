"""
https://leetcode.com/problems/largest-number/
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
"""

# time complexity: O(nlogn), space complexity: O(logn)
# this solution is provided by me.
# The main idea is to use a customized compare function to sort the array.
# If two strings are of the same length, which is larger is obvious.
# If two strings are not of the same length, we should compare the first few letters. If one string starts with the other string (a[:few digit] == b) then we should keep compare a[few digit:] with b until we find the result.

"""
import random

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sort(start, end):
            if start >= end:
                return
            pivot = random.randrange(start, end+1)
            nums[pivot], nums[start] = nums[start], nums[pivot]
            i = j = start + 1
            while j <= end:
                if not greaterthan(nums[start], nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                j += 1
            nums[start], nums[i-1] = nums[i-1], nums[start]
            sort(start, i-2)
            sort(i, end)
        
        def greaterthan(a, b):
            if len(a) == len(b):
                return a >= b
            shorter = min(len(a), len(b))
            if a[:shorter] != b[:shorter]:
                return a[:shorter] >= b[:shorter]
            return greaterthan(a[shorter:], b) if len(b) == shorter else greaterthan(a, b[shorter:])
        
        nums = [str(num) for num in nums]
        sort(0, len(nums)-1)
        return ''.join(nums) if nums[0] != '0' else '0'
"""

# this is provided by the solution set of the question. It's genious.
# time complexity: O(nlogn), space complexity: O(1)
# the trick here is to use the subclass to define the less than (<) logic and let the sort method to sort the string using < but it actually get the string ordered in a descending order.
# We can not just use reverse=True argument to reversely sort the string, because that will bring some problem when two strings start with the same prefix, like 30,3 and 3,30 in the example of the question.
# the logic of < is: if a+b > b+a, a should go first in the list because this will provide a larger final result. 

class SortableStr(str):
    def __lt__(a, b):
        return a+b > b+a

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = map(str, nums)
        result = ''.join(sorted(nums, key=SortableStr))
        return result if result[0] != '0' else '0'
