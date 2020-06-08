"""
https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.


Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.
Example 3:

Input: deck = [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].
Example 5:

Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].


Constraints:

1 <= deck.length <= 10^4
0 <= deck[i] < 10^4
"""

# time complexity: O(n^2), space complexity: O(n)

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False

        count = dict()
        for i in deck:
            count[i] = count.get(i, 0) + 1

        count = set(count.values())
        if min(count) < 2:
            return False

        for x in range(2, min(count) + 1):
            if min(count) % x == 0:
                flag = True
                for i in count:
                    if i % x != 0:
                        flag = False
                        break
                if flag:
                    return True

        return False

# There is a faster way, using greatest common denominator. This is provided by the solution.
# time complexity: O(n(logm)^2), space complexity: O(n), where n is the length of the list, m is the largest number of Ci where there are Ci cards written i on it.
# gcd is a (logm)^2 operation.
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from fractions import gcd
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2
