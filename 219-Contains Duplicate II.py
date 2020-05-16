"""
https://leetcode.com/problems/contains-duplicate-ii/
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""


# Pretty easy.
# time complexity: O(n), space complexity: O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = dict()
        for i in range(len(nums)):
            if nums[i] in dic:
                if i - dic[nums[i]][-1] <= k:
                    return True
                else:
                    dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]
        return False