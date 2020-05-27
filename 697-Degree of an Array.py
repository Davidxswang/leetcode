"""
https://leetcode.com/problems/degree-of-an-array/
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""

# time complexity: O(n), space complexity: O(n)

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = dict()  # dic[5] = (6, 7, 10), means the element 5 shows up 6 times, starting from index 7 and ending at index 10
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [1, i, i]
            else:
                dic[nums[i]][0] += 1
                dic[nums[i]][2] = i

        maxfreq = 0
        length = 0
        for i in dic:
            if dic[i][0] > maxfreq:
                maxfreq = dic[i][0]
                length = dic[i][2] + 1 - dic[i][1]
            elif dic[i][0] == maxfreq and dic[i][2] + 1 - dic[i][1] < length:
                length = dic[i][2] + 1 - dic[i][1]

        return length