"""
https://leetcode.com/problems/pascals-triangle/
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

# time complexity: O(n^2), space complexity: O(n^2), where n is the numRows
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        result = [[1],[1,1]]
        while numRows >= 3:
            templist = [1,1]
            for i in range(len(result[-1])-1):
                templist.insert(1+i,result[-1][i]+result[-1][i+1])
            result.append(templist)
            numRows -= 1
        return result