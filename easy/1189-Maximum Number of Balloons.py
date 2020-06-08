"""
https://leetcode.com/problems/maximum-number-of-balloons/
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.



Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0


Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        sample = 'balon'
        freq = [0, 0, 0, 0, 0]
        for letter in text:
            pos = sample.find(letter)
            if pos != -1:
                freq[pos] += 1
        freq[2] //= 2
        freq[3] //= 2
        return min(freq)