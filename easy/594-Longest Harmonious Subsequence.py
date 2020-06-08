"""
https://leetcode.com/problems/longest-harmonious-subsequence/
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].


Note: The length of the input array will not exceed 20,000.
"""

# time complexity: O(n), space complexity: O(n)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dic = dict()
        for i in nums:
            dic[i] = 1 if i not in dic else dic[i]+1
        result = 0
        for key in list(dic.keys()):
            result = max(result, dic[key]+dic[key+1]) if key+1 in dic else result
        return result