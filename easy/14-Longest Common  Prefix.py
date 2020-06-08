"""
https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

# the method I use is to to what is the shortest length of the strings
# so as to make sure I only check first a couple of letters
# then I go through the strings, check every letter, if I found a letter mismatch, the program ends
# time complexity: O(nm) where n is # of strings, m is the length of the shortest string
# space complexity: O(1)
# there are other methods in the solution of the problem, but the best time and space complexity is the following one
# to use divide and conquer is fancy but I think it unnecessary to do so in this problem
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return ""
        shortest_str = len(strs[0])
        for i in range(1,len(strs)):
            if len(strs[i]) < shortest_str:
                shortest_str = len(strs[i])
        s = ""
        for i in range(shortest_str):
            current = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] == current:
                    continue
                else:
                    return s
            s += current
        return s

