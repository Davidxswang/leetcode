"""
https://leetcode.com/problems/positions-of-large-groups/
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.



Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]


Note:  1 <= S.length <= 1000
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        length = 0
        starting = 0
        result = list()
        for i in range(len(S)):
            if i != len(S) - 1 and S[i] != S[i + 1] or i == len(S) - 1:
                length += 1
                if length >= 3:
                    result.append([starting, i])
                length = 0
                starting = i + 1
            else:
                length += 1

        return result