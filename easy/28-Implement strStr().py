"""
https://leetcode.com/problems/implement-strstr/
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""

# to implement it naively, we can just use brute force search
# time complexity: O(m*n), space complexity: O(1), where m and n are the length of the haystack and needle respectively

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) == 0 or len(needle) > len(haystack):
            return -1
        for i in range(0,len(haystack)-len(needle)+1):
            for j in range(0,len(needle)):
                if haystack[i+j] == needle[j]:
                    if j == len(needle)-1:
                        return i
                    else:
                        continue
                else:
                    break
        return -1


# to lower the time complexity, use KMP algorithm
# first part is to generate the partial match list, indicating if mismatch is found somewhere, where to start next
# "ababc" partial match list is [0,0,1,2,0], "ababa" partial match list is [0,0,1,2,3]
# the way to generate the partial match list is very similar to the main program:
#   if a match is found, needle pointer and haystack pointer both increment
#     if a mismatch is found:
#       if this is the first element of needle that is comparing with the element in haystack, haystack pointer ++
#       if this is not the first element of needle that is comparing with the element in haystack, look up the partial match list
#          e.g. the partial match list of last element(which is the last matching element) indicates 2, then haystack pointer stay where it is, but needle pointer moves to 2, to compare needle[2] with haystack[i]
# I think the best way to think about this is to think about the partial match list generating process using "ababa" and "ababc"
# time complexity: O(m+n), space complexity: O(n), where m and n are the # of elements in haystack and needle
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1
        partial_match = [0] * len(needle)
        i = 1
        j = 0
        while i < len(needle):
            if needle[i] == needle[j]:
                j += 1
                partial_match[i] = j
                i += 1
            else:
                if j != 0:
                    j = partial_match[j-1]
                else:
                    partial_match[i] = 0
                    i += 1
        print(partial_match)
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = partial_match[j-1]
        if j >= len(needle):
            return i-j
        else:
            return -1