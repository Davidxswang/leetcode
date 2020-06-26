"""
https://leetcode.com/problems/triangle/
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

# time complexity: O(m), space complexity: O(n) where m is the total number of elements in triangle, n is the number of rows in triangle.
# classic dp problem

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cur = [triangle[-1][i] for i in range(len(triangle[-1]))]
        for i in range(len(triangle)-2, -1, -1):
            newcur = []
            for j in range(len(triangle[i])):
                newcur.append(triangle[i][j] + min(cur[j], cur[j+1]))
                #cur.pop(0) if we want to use this line, we can change min on the above line to min(cur[0], cur[1])
            cur = newcur
        return cur[0]
