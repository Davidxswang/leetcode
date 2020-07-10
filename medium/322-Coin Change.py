"""
https://leetcode.com/problems/coin-change/

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""

# time complexity: O(n*m), space complexity: O(n*m) where n is amount and m is the length of coins
# classic dynamic programming
# this is inspired by the solution page of the question

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCount = [0] + [amount // min(coins) + 1] * amount
        for coin in coins:
            for i in range(coin, len(minCount)):
                minCount[i] = min(minCount[i], minCount[i-coin] + 1)
        
        return minCount[-1] if minCount[-1] != amount // min(coins) + 1 else -1
