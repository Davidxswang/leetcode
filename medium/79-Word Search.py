"""
https://leetcode.com/problems/word-search/
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""

# time complexity: O(m*n*3^l), space complexity: O(l) due to the call stack, where m and n are the height and width of the matrix and l is the length of the word

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if self.find(i, j, word, set()):
                    return True
        return False
    
    def find(self, i: int, j: int, word: str, history: set) -> bool:
        if not word:
            return True
        if self.board[i][j] != word[0]:
            return False
        history.add((i,j))
        if len(word) == 1:
            return True
        for row,column in (i-1,j), (i+1,j), (i,j-1), (i,j+1):
            if 0 <= row < self.m and 0 <= column < self.n and (row,column) not in history:
                if self.find(row, column, word[1:], history):
                    return True
        history.remove((i,j))
        return False
        
