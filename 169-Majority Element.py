"""
https://leetcode.com/problems/majority-element/
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

# Pretty easy.
# time complexity: O(n), space complexity: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = {}
        for i in nums:
            hashtable[i] = 1 if i not in hashtable else hashtable[i] + 1
            if hashtable[i] > len(nums) / 2:
                return i

# Another solution is inspired by the discussion area: Boyer-Moore Majority Vote Algorithm.
# A demo is here: http://www.cs.utexas.edu/~moore/best-ideas/mjrty/
# The main idea is that if the majority element exist than, the total number of majority numbers should be at least 1 larger than the sum of the number of other elements.
# So when we start traverse, we mark an element and a counter, start with the first element nums[0] and counter = 1.
#   If the counter is 0, we start the counter from 0 in the current element. (Because counter == 0 means that the number of this element is the same as the number of other elements before the number we are looking right now)
#   If we see the same number, counter ++
#   If we see a different number counter --
# time complexity: O(n), space complexity: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        number = 0
        counter = 0
        for i in range(len(nums)):
            if counter == 0:
                number = nums[i]
                counter = 1
            else:
                if nums[i] != number:
                    counter -= 1
                else:
                    counter += 1
        return number