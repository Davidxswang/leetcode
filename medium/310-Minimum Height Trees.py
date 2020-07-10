"""
https://leetcode.com/problems/minimum-height-trees/
For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""

# time complexity: O(E), space complexity: O(E+V), where E is the number of edges and V is the number of vertices.
# this is inspired by @dietpepsi in the discussion area.
# the key idea is to remove all the leaves in every cycle, until we have 2 or 1 node left. The remaining nodes are the result to return.
# two things we need to be careful with:
# 	1. we need to use a new container to record the leaves after current cycle
#	2. actually, in the last cycle, the leaves container can contain: either one single node with no neighbor anymore, or two nodes each having a neighbor of the other node	

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 0:
            return []
        if n == 1:
            return [0]
        
        adjacency = [set() for i in range(n)]
        for i,j in edges:
            adjacency[i].add(j)
            adjacency[j].add(i)
        
        leaves = set(i for i in range(n) if len(adjacency[i]) == 1)

        while n > 2:
            n -= len(leaves)
            newleaves = set()
            for leaf in leaves:
                neighbor = adjacency[leaf].pop()
                adjacency[neighbor].remove(leaf)
                if len(adjacency[neighbor]) == 1:
                    newleaves.add(neighbor)
            leaves = newleaves
        
        return list(leaves)
