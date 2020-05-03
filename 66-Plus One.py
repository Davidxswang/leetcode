"""
https://leetcode.com/problems/plus-one/
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

# set addone = True
# from right to left, if addone then calculate the result on each digit, then check addone
# if addone after i < 0, add another lead digit 1 in the front
# time complexity: O(n), space complexity: O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        addone = True
        i = len(digits) - 1
        while i >= 0 and addone == True:
            digits[i] += 1
            if digits[i] > 9:
                digits[i] %= 10
            else:
                addone = False
            i -= 1
        if addone == True:
            digits.insert(0, 1)
        return digits