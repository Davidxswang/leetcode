"""
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
"""

# time complexity: O(klogk), space complexity: O(n1) where k is the requested length of result and n1 is the length of array 1
# the solution is inspired by @StefanPochmann in the discussion forum.
# we can think of the frontier between in-result and out-of-result elements in the priority queue or heap, each time we put a pair in the result, we can add the element to its right to the priority queue, and if the first element on one line gets selected into the result, we need to add its bottom neighbor to the priority queue as well.
# to make everything make sense, we need to think of the elements in an array:
#       2    4    6
# 1   [1,2] [1,4] [1,6]
# 3   [3,2] [3,4] [3,6]
# 5   [5,2] [5,4] [5,6]

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue = []
        def push(i, j):
            """
            i: the index of nums1
            j: the index of nums2
            """
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i]+nums2[j], i, j])
        
        result = []
        push(0, 0)
        
        while queue and len(result) < k:
            _, i, j = heapq.heappop(queue)
            result.append([nums1[i], nums2[j]])
            push(i, j+1)
            if j == 0:
                push(i+1, j)
        
        return result