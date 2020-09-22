"""
https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.

 

Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
Example 3:

Input: arr = [10,11,12]
Output: 66
 

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 1000
"""

# time complexity: O(n^2), space complexity: O(1)

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        i = 0
        factor = 0
        exclude = 0
        
        while 2 * i + 1 <= len(arr):
            sublen = 2 * i + 1
            factor += sublen
            if sublen > 1:
                for j in range(0, sublen-1):
                    exclude += (sublen - j - 1) * (arr[j] + arr[~j])
            i += 1
        
        return factor * sum(arr) - exclude   