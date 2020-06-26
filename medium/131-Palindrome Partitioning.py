"""
https://leetcode.com/problems/palindrome-partitioning/
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

# time complexity: O(2^n), space complexity: O(n)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def helper(templist, start):
            if start == len(s):
                result.append(templist)
            for i in range(start, len(s)):
                if isPalindrome(s[start:i+1]):
                    newlist = templist + [s[start:i+1]]
                    helper(newlist, i+1)
        
        def isPalindrome(string):
            i = 0
            j = len(string) - 1
            while i < j:
                if string[i] == string[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        
        helper([], 0)
        return result
