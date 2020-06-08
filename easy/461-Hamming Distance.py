"""
https://leetcode.com/problems/hamming-distance/
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""
# time complexity: O(1), space complexity: O(1)
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        counter = 0
        for i in range(32):
            if xor & (1<<i):
                counter += 1
        return counter