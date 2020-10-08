"""
https://leetcode.com/problems/nth-digit/
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

"""

# time complexity: O(logn), space complexity: O(1)

class Solution:
    def findNthDigit(self, n: int) -> int:
        """
        1 <= n < 10^1 * 1: n
        1 <= n-(10^1 - 1) < (10^2 - 10^1)*2: n-(10^1) divmod 2 = 1,1 -> 10+1, 1, e.g., 13
        """
        
        # change n to 0-indexed
        n -= 1
        
        if 0 <= n < 10**1 - 1:
            # 0 - 8
            return n+1
        
        n -= (10**1 - 1 - 0) * 1
        cur_len = 2

        
        while n >= (10**cur_len - (10**(cur_len-1)))*cur_len:
            n -= (10**cur_len - 10**(cur_len-1)) * cur_len
            cur_len += 1
        
        # 0 <= n < (10**cur_len-1) * cur_len
        
        div, mod = divmod(n, cur_len)
        
        number = 10**(cur_len-1) + div
        return str(number)[mod]