"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""

# time complexity: O(klogk), space complexity: O(k)
# it's similar to 373: Find K Pairs with Smallest Sums

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        """
        queue = []
        def push(i, j):
            if i < len(matrix) and j < len(matrix[0]):
                heapq.heappush(queue, [matrix[i][j], i, j])
        
        counter = 0
        push(0, 0)
        
        while counter < k:
            element, i, j = heapq.heappop(queue)
            push(i, j+1)
            if j == 0:
                push(i+1, j)
            counter += 1
        
        return element
        """
        
        return heapq.nsmallest(k, heapq.merge(*matrix))[-1]