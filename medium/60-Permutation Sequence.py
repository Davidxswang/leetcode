"""
https://leetcode.com/problems/permutation-sequence/
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""

# time complexity: O(n), space complexity: O(n)
# the key idea here is to find how to construct the result
# be careful with the range of k, we'd better pass k-1 to the inner call to avoid any trouble

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.result = []
        nums = [str(i) for i in range(1, n+1)]
        self.permute(k-1, nums)
        return ''.join(self.result)
    
    def permute(self, k: int, nums: List[int]) -> None:
        import math
        kfront = k // math.factorial(len(nums)-1)
        remainder = k % math.factorial(len(nums)-1)
        self.result.append(nums[kfront])
        nums.pop(kfront)
        if remainder == 0:
            self.result += nums
        else:
            self.permute(remainder, nums)
