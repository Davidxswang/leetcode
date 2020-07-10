"""
https://leetcode.com/problems/bulb-switcher/

There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.
"""

# time complexity: O(1), space complexity: O(1)
# this is inspired by @StefanPochmann in the discussion area.
# the idea is this:
# a bulb will be on after n round if and only if the bulb have been toggled odd times, e.g. on-off-on-off-on
# so bulb i (1<= i <= n) will be toggled how many times is the key
# As n is given fixed, for any number i, it will be toggled only in the round d if d is a factor of i. So how many times i will be toggled depends on how many factors it has.
# for a non-square number, factors come in pairs, e.g. 12 = 1*12 = 2*6 = 3*4;
# for a square number, factors come in pairs except one: e.g. 16 = 1*16 = 2*8 = 4*4, so bulb 16 will be toggled 5 times instead of 6.
# so the question is to count how many square numers <= n, e.g. n = 36, so 1, 4, 9, 16, 25, 36 are the numbers, so there will be 6 bulbs on after n cycles.

class Solution:
    def bulbSwitch(self, n: int) -> int:
        import math
        return int(math.sqrt(n))
