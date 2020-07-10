"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""

# time complexity: O(n), space complexity: O(n)
# this is inspired by @npvinhphat in the discussion area.
# So the key here is to use separate storage to track the best possible profit under different states: today rest, today buy, today sell.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        rest_profit = 0                 # the remaining money I will have if I rest in day i
        buy_profit = -prices[0]         # the remaining money I will have if I buy in day i
        sell_profit = -prices[0]        # the remaining money I will have if I sell in day i
        
        for i in range(1, len(prices)):
            newrest_profit = max(rest_profit, sell_profit)      # either I sold on day i-1 and rest today, or I rested on day i-1 and rest today again
            newbuy_profit = max(rest_profit-prices[i], buy_profit)  # either I bought before yesterday, and doing nother today, or I rested yesterday and buy today
            newsell_profit = buy_profit + prices[i]             # I bought before yesterday, and I sell today
            rest_profit, buy_profit, sell_profit = newrest_profit, newbuy_profit, newsell_profit
        
        return max(rest_profit, sell_profit)
