"""
https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.



Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").


Constraints:

1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j], words[i][j] are English lowercase letters.
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        count = [0] * 11
        for word in words:
            count[self.f(word)] += 1
        dp = [0] * 11
        for i in range(len(dp) - 2, 0, -1):
            dp[i] = dp[i + 1] + count[i + 1]
        result = []
        for query in queries:
            result.append(dp[self.f(query)])
        return result

    def f(self, string: str) -> int:
        currentletter = string[0]
        freq = 1
        for letter in string[1:]:
            if letter == currentletter:
                freq += 1
            elif letter < currentletter:
                currentletter = letter
                freq = 1
        return freq