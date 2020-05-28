"""
https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:

Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
Example 2:

Input: L = 10, R = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
Note:

L, R will be integers L <= R in the range [1, 10^6].
R - L will be at most 10000.
"""

# time complexity: O(n), space complexity: O(1)
# There are two ways to count the 1s in the 2-based representation
# The second one is the most time-efficient. Other two ways are not as efficient as the second oe.
# This shwos that bin is really optimized by the python compiler.

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        result = 0
        for number in range(L, R + 1):
            #1 ones = sum(list(1 & (number>>i) for i in range(20)))
            #2 ones = bin(number).count('1')
            ones = 0
            while number > 0:
                if number & 1 == 1:
                    ones += 1
                number = number >> 1
            if ones in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
                result += 1

        return result