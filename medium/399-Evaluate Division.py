"""
https://leetcode.com/problems/evaluate-division/

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""

# time complexity: O(n), space complexity: O(m) where n is the number of nodes, and m is the number of edges

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        relations = dict()
        for (a, b), value in zip(equations, values):
            if a in relations:
                relations[a].append([b, value])
            else:
                relations[a] = [[b, value]]
            if b in relations:
                relations[b].append([a, 1/value])
            else:
                relations[b] = [[a, 1/value]]
        
        results = []
        visited = set()
        
        def go(a, b, temp):
            for i, (target, value) in enumerate(relations[a]):
                if target == b:
                    return temp * value
                else:
                    if target not in visited:
                        visited.add(target)
                        result = go(target, b, value)
                        if result is not None:
                            return temp * result
            return None
                
                
        for i, (a, b) in enumerate(queries):
            visited = set()
            if a not in relations:
                results.append(-1.0)
            else:
                visited.add(a)
                result = go(a, b, 1)
                if result is None:
                    results.append(-1.0)
                else:
                    results.append(result)
        
        return results
                