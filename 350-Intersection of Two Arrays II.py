"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

# Using a hashmap like the problem 1.
# time complexity: O(n+m), space complexity: O(n), where n and m are the lengths of the arrays nums1 and nums2
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = dict()
        result = []
        for i in nums1:
            hashmap[i] = 1 if i not in hashmap else hashmap[i] + 1
        for i in nums2:
            if i in hashmap and hashmap[i] > 0:
                result.append(i)
                hashmap[i] -= 1
        return result

# Regarding the follow up questions:
# If the array is sorted, I can use double pointer solution which will save space.
# If nums1 is small, use nums1 to build up the hash table is better, because it saves space and time complexity remains the same.
# Use nums1 to build the hashtable and iterate through the nums2 by reading the element from the disk one by one.