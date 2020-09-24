"""
https://leetcode.com/problems/reconstruct-itinerary/
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""

# time complexity: O(m), space complexity: O(m), where m is the number of edges
# first solution is by me, second is provided by @StefanPochmann in the discussion area
# both use backtracking but @StefanPochmann's way is much more efficient

from collections import defaultdict
import bisect
import copy

from collections import defaultdict
import bisect
import copy

class Solution:
    """
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        routes = defaultdict(list)
        
        counter = 0
        for start, end in tickets:
            routes[start].append([end, False])
            counter += 1
        
        for key in routes.keys():
            routes[key].sort(key=lambda x:x[0])
        
        start = 'JFK'
        
        result = self.recursive(start, routes, counter)
            
        return result
    
    
    def recursive(self, start, routes, counter):
        if counter != 0 and all([x[1] for x in routes[start]]):
            return None
        
        if counter == 0:
            return [start]
        
        for i in range(len(routes[start])):
            if not routes[start][i][1]:
                routes[start][i][1] = True
                new_result = self.recursive(routes[start][i][0], routes, counter-1)
                if new_result is not None:
                    return [start] + new_result
                else:
                    routes[start][i][1] = False
        return None
    """
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        
        print(targets)
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]