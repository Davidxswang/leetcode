"""
https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.



Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5


Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
"""

# time complexity: O(n), space complexity: O(n)
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dic = set()
        for i in A:
            if i in dic:
                return i
            else:
                dic.add(i)

# Another way is to check duplicate, there are N same numbers, and N unique numbers, if we ever find a duplicate, return
# If N same numbers distribute evenly, every two elements will have one of this number;
# If not distributed evenly, there will be two adjacent elements having the same value;
# Therefore, we can just check every adjacent 4 numbers.
# time complexity: O(n), space complexity: O(1)
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for diff in range(1, 4):
            for i in range(len(A)-diff):
                if A[i] == A[i+diff]:
                    return A[i]