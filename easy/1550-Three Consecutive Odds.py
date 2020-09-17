"""
https://leetcode.com/problems/three-consecutive-odds/
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 0
        while i < len(arr) - 2:
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True
            if arr[i+2] % 2 == 0:
                i += 3
                continue
            if arr[i+1] % 2 == 0:
                i += 2
                continue
            if arr[i] % 2 == 0:
                i += 1
                continue
        return False
            
