"""
https://leetcode.com/problems/water-bottles/
Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Return the maximum number of water bottles you can drink.

 

Example 1:



Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.
Example 2:



Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.
Example 3:

Input: numBottles = 5, numExchange = 5
Output: 6
Example 4:

Input: numBottles = 2, numExchange = 3
Output: 2
 

Constraints:

1 <= numBottles <= 100
2 <= numExchange <= 100
"""

# for the first algorithm, it's simple and its time and space complexity are: O(log(n)) and O(1)
# for the second algorithm, it's based on the math behind it. It's provided by [@Weldcard](https://leetcode.com/problems/water-bottles/discuss/745231/Python-1-liner-with-math-explained/626712) in the discussion area.
# the basic idea is that:
# 	1. we have to have at least numExchange bottles to exchange the empty bottle for a bottle of water
#	2. for the result (total number of bottles of water we can drink), it's calculated by numBottles // (numExchange - 1) + numBottles
# therefore, based on 1 and 2, the result should be numBottles + (numBottles - 1) // (numExchange - 1)
# time complexity: O(1), space complexity: O(1)
