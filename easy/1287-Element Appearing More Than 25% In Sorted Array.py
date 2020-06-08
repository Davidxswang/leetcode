"""
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
 

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l25 = len(arr) // 4
        for i in range(len(arr)-l25):
            if arr[i] == arr[i+l25]:
                return arr[i]
