"""
https://leetcode.com/problems/merge-sorted-array/
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""



# Pretty simple one. Pointer i goes from right to left in nums1, check the current last one element in nums1 and nums2
# Put in the position of pointer i whichever last element is larger in nums1 and nums2
# time complexity: O(m+n), space complexity: O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m - 1
        pointer2 = n - 1
        i = m + n - 1
        while i >= 0:
            if pointer1 >= 0 and pointer2 >= 0:
                if nums1[pointer1] >= nums2[pointer2]:
                    element = nums1[pointer1]
                    pointer1 -= 1
                else:
                    element = nums2[pointer2]
                    pointer2 -= 1
            elif pointer1 < 0:
                element = nums2[pointer2]
                pointer2 -= 1
            else:  # pointer2 < 0
                element = nums1[pointer1]
                pointer1 -= 1
            nums1[i] = element
            i -= 1