"""
https://leetcode.com/problems/perfect-squares/
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

# time complexity: O(n^2), space complexity: O(n^0.5)
# this is inspired by @ChrisZhang12240 in the discussion area. The time complexity is inspired by @lnmlv in the discussion.
# actually there is a theorem: Lagrange's four-square theorem, stating that every natural number can be represented by the sum of four integer squares. Link: https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
# so the depth of the tree will be at most 4, the width of the tree will be at most sqrt(n)
# so the total number will be at most O(n^2)

class Solution:
    def numSquares(self, n: int) -> int:
        # if we use DP, the time limit excess will show up, so use BFS
        if n <= 0:
            return 0
        
        result = 1
        perfect_squares = []
        i = 1
        while i**2 <= n:
            if i**2 == n:
                return 1
            perfect_squares.append(i**2)
            i += 1
        
        unvisited_node_current_layer = set([n])

        while unvisited_node_current_layer:
            temp = set()
            
            for node in unvisited_node_current_layer:
                for square in perfect_squares:
                    if node == square:
                        return result
                    if node < square:
                        break
                    temp.add(node-square)
            
            unvisited_node_current_layer = temp
            result += 1
            
        
        return result
