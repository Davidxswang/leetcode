"""
https://leetcode.com/problems/consecutive-characters/
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1
 

Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.
"""
# time complexity: O(n), space complexity: O(1)
class Solution:
    def maxPower(self, s: str) -> int:
        current = s[0]
        count = 1
        maxi = 1
        for i in range(1, len(s)):
            if s[i] == current:
                count += 1
            else:
                current = s[i]
                count = 1
            maxi = max(maxi, count)
        return maxi
