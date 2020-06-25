"""
https://leetcode.com/problems/gray-code/
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
"""

# time complexity: O(2^n), space complexity: O(1)
# The solution is provided by @zkf85 in the discussion area. 
# The idea is inspired by @yuyibestman in the discussion area.
# The main idea comes from the symmetricity here: 00,01,11,10 -> (000,001,011,010)(110,111,101,100) the first part actually is from the last call which is n-1, the second part actually is build by put a one in the highest digit.
# the code is very self-explanatary

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        for i in range(n):
            l = len(result)
            for j in range(l-1, -1, -1):
                result.append(result[j] | 1<<i)
        return result
