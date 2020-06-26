"""
https://leetcode.com/problems/word-ladder/
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

# time complexity: O(M*M*N), space complexity: O(M*M*N), where M is the length of each word, and n is the length of the list
# the solutions are provided by the solution article of the question.
# The main idea is to build a graph of connectivity which is 1 letter different from each other. When we build the graph, we should use an intermediate element which is one letter replaced by a generic "*". Then we should start from beginWord as a root node, using breadth first search to traverse the graph and see if we can reach the endWord. If so, we are good. If not, no solution.
# the second solution is faster because it uses bidirectional BFS, which using two BFS to search, one from the beginWord, the other from the endWord. If during the traversal, any element appears in both of the visited dictionaries, that element is the one we are looking for.

class Solution:
    """
    solution 1, BFS, 128,s
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        import collections
        if not wordList or endWord not in wordList:
            return 0
        
        L = len(beginWord)
        
        adjacency = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                adjacency[word[:i]+'*'+word[i+1:]].append(word)
        
        queue = collections.deque([(beginWord, 1)])
        visited = set([beginWord])
        while queue:
            current, level = queue.popleft()
            for i in range(L):
                tempword = current[:i] + '*' + current[i+1:]
                for eachword in adjacency[tempword]:
                    if eachword == endWord:
                        return level+1
                    if eachword not in visited:
                        visited.add(eachword)
                        queue.append((eachword, level+1))
                adjacency[tempword] = []
        return 0
    """
    
    """
    solution 2, 103ms, 95.15%
    """
    import collections
    def __init__(self):
        self.length = 0
        self.adjacency = collections.defaultdict(list)
    
    def visit(self, queue, visited, other_visited):
        if queue:
            current, level = queue.popleft()
        
        for i in range(self.length):
            tempword = current[:i] + '*' + current[i+1:]
            for word in self.adjacency[tempword]:
                if word in other_visited:
                    return level + other_visited[word]
                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word,level+1))
        return 0
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList:
            return 0
        
        self.length = len(beginWord)
        
        queue_begin = collections.deque([(beginWord, 1)])
        queue_end = collections.deque([(endWord, 1)])
        visited = {beginWord: 1}
        other_visited = {endWord: 1}
        
        for word in wordList:
            for i in range(self.length):
                tempword = word[:i] + '*' + word[i+1:]
                self.adjacency[tempword].append(word)
               
        answer = 0
        while queue_begin and queue_end:
            answer = self.visit(queue_begin, visited, other_visited)
            if answer:
                return answer
            answer = self.visit(queue_end, other_visited, visited)
            if answer:
                return answer
        
        return 0
                    
