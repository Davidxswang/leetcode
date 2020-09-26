"""
https://leetcode.com/problems/top-k-frequent-elements/
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.

"""

# time complexity: O(nlogn), space complexity: O(n), worse case

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
        
        freq = [[f, n] for n, f in counter.items()]
        freq.sort(key=lambda x:x[0], reverse=True)
        
        return [f[1] for i, f in enumerate(freq) if i < k]