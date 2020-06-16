"""
https://leetcode.com/problems/group-anagrams/
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

# time complexity: O(n), space complexity: O(n)
# the key idea here is to find a hash map to find the hash-equivalent word in the strs

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for word in strs:
            temp = ['0'] * 26
            for letter in word:
                index = ord(letter)-ord('a')
                temp[index] = str(int(temp[index])+1)
            index = ''.join(temp)
            dic.setdefault(index, []).append(word)
        return list(dic.values())
        
