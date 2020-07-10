"""
https://leetcode.com/problems/maximum-product-of-word-lengths/
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
"""

# time complexity: O(n*m+n*n), space complexity: O(n*n) where n is the number of words, and m is the average length of each word
# this is provided by @agave in the discussion area.
# the key here is map the mask to the length of the longest word having this mask, so the max process is very easy using & and product.

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        unique_max = dict()
        for word in words:
            mask = 0
            for letter in set(word):
                mask |= (1 << (ord(letter) - ord('a')))
            unique_max[mask] = max(unique_max.get(mask, 0), len(word))
        return max([unique_max[i]*unique_max[j] for i in unique_max for j in unique_max if i & j == 0] or [0])
        
