"""
https://leetcode.com/problems/course-schedule-ii/
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""

# time complexity: O(E), space complexity: O(E+V) where E is the number of edges and V is the number of vertices.
# This is very similar to problem 207.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        
        adj_list = defaultdict(list)
        incoming_edges = [0] * numCourses
        
        for end, start in prerequisites:
            adj_list[start].append(end)
            incoming_edges[end] += 1
        
        freecourses = list(i for i in range(numCourses) if incoming_edges[i] == 0) # all the courses that don't have incoming edges -> no prerequisite courses
        
        learning_queue = list()    # learn prerequisite first, so prerequisite goes into the list first
        
        while freecourses:
            course = freecourses.pop()
            learning_queue.append(course)
            # set all its downstream courses to free courses and decrease their incoming edges
            for downstream in adj_list[course]:
                incoming_edges[downstream] -= 1
                if incoming_edges[downstream] == 0:
                    freecourses.append(downstream)
        
        return learning_queue if sum(incoming_edges) == 0 else []
