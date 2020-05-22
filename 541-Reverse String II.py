"""
https://leetcode.com/problems/reverse-string-ii/
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""

# time complexity: O(n), space complexity: O(n) if the list converted from s counts.
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        group = len(s) // (2*k)
        for i in range(group):
            start = i * 2 * k
            end = start + k - 1
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        left = len(s) % (2*k)
        start = group * 2 * k
        end = group * 2 * k + k - 1 if left >= k else len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        s = ''.join(s)
        return s