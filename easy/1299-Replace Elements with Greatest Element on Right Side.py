"""
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
"""
# time complexity: O(n), space complexity: O(n)

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        if len(arr) == 2:
            return [arr[-1],-1]
        result = [0] * len(arr)
        result[-2:] = [arr[-1], -1]
        for i in range(len(arr)-3, -1, -1):
            result[i] = max(arr[i+1], result[i+1])
        return result
