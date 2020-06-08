"""
https://leetcode.com/problems/pascals-triangle-ii/
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

# time complexity: O(k^2), space complexity: O(k)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        result = [1,1]
        while rowIndex >= 2:
            temp = [1,1]
            for i in range(len(result)-1):
                temp.insert(1+i,result[i]+result[i+1])
            result = temp
            rowIndex -= 1
        return result