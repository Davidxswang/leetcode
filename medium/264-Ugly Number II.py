"""
https://leetcode.com/problems/ugly-number-ii/
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
"""

# time complexity: O(n), space complexity: O(n)
# this solution is inspired by @Dico in the discussion area.
# We know we need to add a number to the list and we know we need to use 2, 3 and 5 to multiply one of the number in the list and get a new number which is least among 2*(), 3*(), and 5*().
# The key here is to think of these 3 multiplication as three separate lines, and remember the pointer of the line for each one of them.
 

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 3:
            return n
        result = [1] * n
        pointer2, pointer3, pointer5 = 0, 0, 0
        for i in range(1, n):
            result[i] = min(result[pointer2]*2, result[pointer3]*3, result[pointer5]*5)
            if result[i] == result[pointer2]*2:
                pointer2 += 1
            if result[i] == result[pointer3]*3:
                pointer3 += 1
            if result[i] == result[pointer5]*5:
                pointer5 += 1
        return result[-1]
        
