"""
https://leetcode.com/problems/unique-binary-search-trees/
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# time complexity: O(n^2), space complexity: O(n)
# basically, for each number, we need to let i (1<=i<=n) be root and see how many kinds of trees <i and how many kinds of trees >i can build and multiply-sum them together.

class Solution:
    def numTrees(self, n: int) -> int:
        if n < 1:
            return 0
        if n <= 2:
            return n
        number = [1] * (n+1)
        number[2] = 2
        for i in range(3, n+1):
            temp = 0
            for left in range(0, i):
                temp += number[left] * number[i-1-left]
            number[i] = temp
        return number[n]
