"""
https://leetcode.com/problems/lexicographical-numbers/
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""

# time complexity: O(nlogn), space complexity: O(n)

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        import heapq
        
        queue = []
        for i in range(1, n+1):
            heapq.heappush(queue, [str(i), i])
        
        result = []
        while queue:
            _, num = heapq.heappop(queue)
            result.append(num)
        
        return result