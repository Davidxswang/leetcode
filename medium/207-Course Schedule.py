"""

https://leetcode.com/problems/course-schedule/
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
"""


# time complexity: O(E), space complexity: O(E+V) where V is number of vertices and E is the number of edges
# This is inspired by the solution of problem 210 (https://leetcode.com/problems/course-schedule-ii/solution/) and @hnoss(https://leetcode.com/problems/course-schedule/discuss/58516/Easy-BFS-Topological-sort-Java/59977) in the discussion area.
# the main idea is to process each free courses (those don't have prerequisite). After learn the prerequisite courses, its control to the downstream courses can be removed. All the free courses due to this process should be moved to the free courses set until there is no free courses.
# If there is no free courses anymore, we need to check if there is remaining edges, if there is any remaining edges, it means all the rest of the courses have a cycle in it because all of them have incoming courses so we cannot start from either of them.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        
        return sum(incoming_edges) == 0
