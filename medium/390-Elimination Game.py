"""
https://leetcode.com/problems/elimination-game/
There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
"""

# time complexity: O(logn), space complexity: O(logn)

class Solution:
    def lastRemaining(self, n: int) -> int:
        """
        2, True -> 1
        2, False -> 0
        3, True -> 1
        3, False -> 1
        4, True -> 2, False -> 0
        4, False -> 2, True -> 1
        5, True -> 2, False -> 0
        5, False -> 2, True -> 1
        """
        def getIndex(current_len, toright):
            if current_len == 1:
                return 0
            if current_len % 2 == 0:
                if toright:
                    return 1 + 2 * getIndex(current_len // 2, not toright)
                else:
                    return 2 * getIndex(current_len // 2, not toright)
            else:
                return 1 + 2 * getIndex(current_len // 2, not toright)
        
        index = getIndex(n, True)
        
        return index+1
        

        
        