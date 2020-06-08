"""
https://leetcode.com/problems/intersection-of-two-arrays/
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""

# Pretty easy if using python's built-in function.
# time complexity: O(n), space complexity:O(n)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# Another solution is to use hash table to traverse through the first array.
# Then look at each element in array 2 and see if this has appeared in array 1's hash table. If so, mark it.
# The marking process is to make sure the output is unique.
# time complexity: O(n), space complexity: O(n)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = dict()
        result = []
        for i in nums1:
            hashmap[i] = 1
        for i in nums2:
            if i in hashmap and hashmap[i] == 1:
                result.append(i)
                hashmap[i] = 2
        return result

