"""
https://leetcode.com/problems/count-largest-group/
Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 

Return how many groups have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
Example 3:

Input: n = 15
Output: 6
Example 4:

Input: n = 24
Output: 5
 

Constraints:

1 <= n <= 10^4
"""

# time complexity: O(nlogn), space complexity: O(logn)
class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = dict()
        for i in range(1, n+1):
            temp = 0
            while i > 0:
                temp += i % 10
                i //= 10
            dic[temp] = dic.get(temp, 0) + 1
        length = 0
        count = 0
        for key, value in dic.items():
            if value == length:
                count += 1
            elif value > length:
                length = value
                count = 1
        return count
