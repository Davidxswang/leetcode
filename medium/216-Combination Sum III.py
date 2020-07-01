"""
https://leetcode.com/problems/combination-sum-iii/
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""

# time complexity: O(k!), space complexity: O(n)

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > 9:
            return []
        if n > sum(i for i in range(9, 9-k, -1)):
            return []
        
        self.result = []
        self.recursive([], 9, n, k)
        return self.result
    
    def recursive(self, temp: List[int], start: int, residual: int, num: int) -> None:
        if num == 0 and residual == 0:
            self.result.append(temp)
            return
        for i in range(start, 0, -1):
            if i <= residual:
                newtemp = temp+[i]
                self.recursive(newtemp, i-1, residual-i, num-1)
                
