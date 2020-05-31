"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
"""

# time complexity: O(logn), space complexity: O(1)

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return self.find(A, 1, len(A) - 2)

    def find(self, A: List[int], start: int, end: int) -> int:
        if A[start - 1] < A[start] > A[start + 1]:
            return start
        elif A[end - 1] < A[end] > A[end + 1]:
            return end
        else:
            middle = start + (end - start) // 2
            if A[middle - 1] < A[middle] > A[middle + 1]:
                return middle
            elif A[middle] < A[middle + 1]:
                return self.find(A, middle + 1, end)
            else:
                return self.find(A, start, middle - 1)