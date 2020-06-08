"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.
"""

# time complexity: O(n), space complexity: O(1), where n is the larger length of the two strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        if len1 != len2:
            len1, len2 = (len1, len2) if len1 > len2 else (len2, len1)
            # get the greatest common denominator, len1 > len2 now
            while len2 != 0:
                len1, len2 = len2, len1 % len2
        # len1 is the gcd now
        for i in range(len1, 0, -1):
            if len1 % i == 0:
                pattern = str1[:i]
                if pattern * (len(str1) // len(pattern)) == str1 and pattern * (len(str2) // len(pattern)) == str2:
                    return pattern
        return ""

