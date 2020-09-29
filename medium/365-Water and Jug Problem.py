"""
https://leetcode.com/problems/water-and-jug-problem/
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False
 

Constraints:

0 <= x <= 10^6
0 <= y <= 10^6
0 <= z <= 10^6
"""

# time complexity: O(logn), space complexity: O(1) where n is the max(x, y)
# the solution is inspired by https://www.math.tamu.edu/~dallen/hollywood/diehard/diehard.htm
# whether the answer is True depends on whether the greates common denominator of x and y can divide z

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x == z or y == z:
            return True
        if x == 0 or y == 0:
            return False
        
        if x+y < z:
            return False

        a = max(x, y)
        b = min(x, y)
        
        while b > 0:
            _, mod = divmod(a, b)
            a, b = b, mod
        
        return z % a == 0