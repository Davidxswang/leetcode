"""
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
 

Constraints:

0 <= low <= high <= 10^9
"""

# time complexity: O(1), space complexity: O(1)

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high:
            return low % 2
        
        if low % 2 == 0 and high % 2 == 0:
            high -= 1
        elif low % 2 == 1 and high % 2 == 1:
            high += 1
        
        return (high - low + 1) // 2
