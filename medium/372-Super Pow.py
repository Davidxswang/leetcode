"""
https://leetcode.com/problems/super-pow/
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

 

Example 1:

Input: a = 2, b = [3]
Output: 8
Example 2:

Input: a = 2, b = [1,0]
Output: 1024
Example 3:

Input: a = 1, b = [4,3,3,8,5,2]
Output: 1
Example 4:

Input: a = 2147483647, b = [2,0,0]
Output: 1198
 

Constraints:

1 <= a <= 231 - 1
1 <= b.length <= 2000
0 <= b[i] <= 9
b doesn't contain leading zeros.
"""

# time complexity: O(n), space complexity: O(1)
# the solution is inspired by @fentoyal in the discussion area.

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        result = 1
        
        for i in range(len(b)):
            result = ((result ** 10) % 1337) * (((a % 1337) ** b[i]) % 1337) % 1337
        
        return result