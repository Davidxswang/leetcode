"""
https://leetcode.com/problems/guess-number-higher-or-lower/
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6
"""

# Pretty easy.
# time complexity: O(logn), space complexity: O(1)

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            middle = low + (high - low) // 2
            g = guess(middle)
            if g == -1:
                high = middle - 1
            elif g == 1:
                low = middle + 1
            else:
                return middle