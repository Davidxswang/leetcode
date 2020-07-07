"""
https://leetcode.com/problems/game-of-life/
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""

# time complexity: O(m*n), space complexity: O(1)
# the key here is to find a way to encode the future state and put it together with the current state. After calculating all the future states, we can substitute the current state with the future state.

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # by %2 we can get the current state
        # by // 2 we can get the next state, if next state is 1, we add 4, if next state is 0, we add 2
        
        def count(i, j):
            live = 0
            for row, col in (i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1):
                live += 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] & 1 == 1
            return live   
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                liveneighbor = count(i, j)
                livenow = board[i][j] & 1
                if livenow and liveneighbor < 2:
                    board[i][j] += 2
                elif livenow and liveneighbor in (2,3):
                    board[i][j] += 4
                elif livenow and liveneighbor > 3:
                    board[i][j] += 2
                elif not livenow and liveneighbor == 3:
                    board[i][j] += 4
                else:
                    board[i][j] += 2
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] //= 4
                
        
