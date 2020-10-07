"""
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""

# time complexity: O(nlogn), space complexity: O(nlogn)

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counter = dict()
        for i in range(len(s)):
            if s[i] in counter:
                counter[s[i]] += 1
            else:
                counter[s[i]] = 1
        
        todelete = set(letter for letter in counter if counter[letter] < k)
        if not todelete:
            return len(s)
        
        list_s = [s[i] if s[i] not in todelete else '-' for i in range(len(s))]
        str_s = ''.join(list_s)
        tochoose = str_s.split('-')
        result = 0
        for i in range(len(tochoose)):
            if tochoose[i] and len(tochoose[i]) >= k:
                length = self.longestSubstring(tochoose[i], k)
                if length > result:
                    result = length
        
        return result