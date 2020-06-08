"""
https://leetcode.com/problems/binary-number-with-alternating-bits/
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
"""

# time complexity: O(logn), space complexity: O(logn)

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # solution 1
        return bin(n).count('11') == 0 and bin(n).count('00') == 0


# time complexity: O(logn), space complexity: O(1)
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # solution 2
        prev = 0 if n % 2 == 1 else 1
        while n != 0:
            remainder = n % 2
            if remainder == prev:
                return False
            prev = remainder
            n //= 2

        return True