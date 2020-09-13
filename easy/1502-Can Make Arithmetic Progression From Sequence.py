"""
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.

 

Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
 

Constraints:

2 <= arr.length <= 1000
-10^6 <= arr[i] <= 10^6
"""

# time complexity: O(n), space complexity: O(n)
# the basic idea is to calculate the progression difference between consecutive elements, then put every element into the right position, if two elements are in the same position, then the result is False. Be careful with the case where start == end.

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        start = min(arr)
        end = max(arr)
        if start == end:
            return True
        
        prog, remain = divmod(end - start, len(arr) - 1)
        if remain != 0:
            return False

        result = [None] * len(arr)
        for number in arr:
            index, remain = divmod(number - start, prog)
            if remain != 0:
                return False
            if result[index] is None:
                result[index] = number
            else:
                return False
        return True
