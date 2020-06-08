"""
https://leetcode.com/problems/palindrome-number/
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""


# this is very similar to 7-Reverse Integer if you deal with it in the similar way
# time complexity: O(log10(n)), space complexity: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        temp = x
        reverse = 0
        while temp > 0:
            reverse = reverse*10 + temp%10
            temp //= 10
        return True if reverse == x else False


# the solution to this problem gave another way of thinking: to only reverse half of the number
# this saves half of the time
# time complexity: O(log10(n)), space complexity: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x > 0 and x%10 == 0:
            return False
        reverse = 0
        while x > reverse:
            reverse = reverse*10 + x%10
            x //= 10
        return True if reverse == x or reverse//10 == x else False