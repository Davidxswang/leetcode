"""
https://leetcode.com/problems/two-city-scheduling/
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.



Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.


Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
"""

# time complexity: O(nlogn), space complexity: O(n)
# this is provided by @logan138 in the discussion area.
# assume all the people have been sent to A, we need to calculate the refund of sending them to B for each one of them
# refund is: cost[i][0]-cost[i][1]

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        for i in range(len(costs)):
            costs[i].append(costs[i][0]-costs[i][1])
        costs.sort(key=lambda x:x[2])
        return sum(cost[0] for cost in costs) - sum(costs[i][2] for i in range(len(costs)//2,len(costs)))