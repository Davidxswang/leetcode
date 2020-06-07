"""
https://leetcode.com/problems/number-of-equivalent-domino-pairs/
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].



Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1


Constraints:

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9
"""

# time complexity: O(n), space complexity: O(n)

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = dict()
        for a, b in dominoes:
            index = max(a, b) * 10 + min(a, b)
            dic[index] = dic.get(index, 0) + 1
        return sum(dic[key] * (dic[key] - 1) // 2 for key in dic)
