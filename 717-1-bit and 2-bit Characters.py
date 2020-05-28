"""
https://leetcode.com/problems/1-bit-and-2-bit-characters/
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input:
bits = [1, 1, 1, 0]
Output: False
Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
Note:

1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            if i != len(bits)-1 and i != len(bits)-2:
                if bits[i] == 0:
                    i += 1
                else:
                    i += 2
            elif i == len(bits) - 2:
                return bits[i] == 0
            else:
                return True