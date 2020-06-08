"""
https://leetcode.com/problems/increasing-decreasing-string/
Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

 

Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
Example 3:

Input: s = "leetcode"
Output: "cdelotee"
Example 4:

Input: s = "ggggggg"
Output: "ggggggg"
Example 5:

Input: s = "spo"
Output: "ops"
 

Constraints:

1 <= s.length <= 500
s contains only lower-case English letters.
"""
# time complexity: O(n), space complexity: O(1)

class Solution:
    def sortString(self, s: str) -> str:
        freq = [0] * 26
        for letter in s:
            freq[ord(letter)-ord('a')] += 1
        length = len(s)
        result = ''
        while length > 0:
            for i in range(len(freq)):
                if freq[i] > 0:
                    result += chr(ord('a') + i)
                    freq[i] -= 1
                    length -= 1
            for i in range(len(freq)-1, -1, -1):
                if freq[i] > 0:
                    result += chr(ord('a') + i)
                    freq[i] -= 1
                    length -= 1
        return result
