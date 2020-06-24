"""
https://leetcode.com/problems/combinations/
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

# Three solutions are provided here. First is by me. The second and third one are inspired by @StefanPochmann in the discussion area.
# Basically, there are two ways, recursion and iteration. The first one and second one are recursion and the last one is iteration.  

class Solution:

    # this is recursion, from the beginning to the end.
    # time complexity: O(n!), space complexity: O(n)
    """
    Recursive method. It's very slow, around 600ms
    The reason why it's so slow is that it has many failed calls, only those successful ones resulting in being added to the result.
    
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0 or n < 1 or k > n:
            return []
        self.result = []
        self.n = n
        self.toadd = [i for i in range(1, n+1)]
        for i in range(self.n):
            self.recursive([self.toadd[i]], i+1, k-1)
        return self.result
    
    def recursive(self, result: List[int], start: int, k: int) -> None:
        if k == 0:
            self.result.append(result)
        
        for i in range(start, self.n):
            self.recursive(result+[self.toadd[i]], i+1, k-1)
    

    # this is recursion as well, but perfectly concise
    # time complexity: O((n-k+1)!), space complexity: O(n) due to the call stack 
    # this algorithm can ensure that every call is a successful call
    """
    This is fast, recursive around 100ms
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        return [pre+[i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]
    
    
    # this is iteration
    # time complexity: O(n!), space complexity: O(1) excluding the output space.
    """
    This is slow too, around 700ms.
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = [[]]
        for _ in range(k):
            result = [[i] + suf for suf in result for i in range(1, n+1 if not suf else suf[0])]
        return result
    

